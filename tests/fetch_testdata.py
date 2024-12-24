from typing import List, Any, Dict
import asyncio
import json
import os

import aiohttp

from cforces.client import Client


def custom_open(path: str, *args, **kwargs) -> Any:
    return open(os.path.join(os.path.dirname(__file__), path), *args, **kwargs)


async def fetch_hacks(client: Client, count: int) -> None:
    with custom_open("testdata/Hack_2050.json", "w") as file:
        json.dump(
            (
                await client.api_call(
                    "contest.hacks", {"contestId": 2050}, convert_case=False
                )
            )[:count],
            file,
        )


async def fetch_rating_changes(client: Client, count: int) -> None:
    with custom_open("testdata/RatingChange_2050.json", "w") as file:
        json.dump(
            (
                await client.api_call(
                    "contest.ratingChanges",
                    {"contestId": 2050},
                    convert_case=False,
                )
            )[:count],
            file,
        )


async def fetch_standings(client: Client, count: int) -> None:
    with custom_open("testdata/Standings_2050.json", "w") as file:
        data: Dict[str, Any] = await client.api_call(
            "contest.standings",
            {"contestId": 2050, "count": count},
            convert_case=False,
        )

        dump_data: List[Dict[str, Any]] = []
        for x in range(0, count):
            dump_data.append(
                {
                    "contest": data["contest"],
                    "rows": [data["rows"][x]],
                    "problems": data["problems"],
                }
            )
        del data

        json.dump(dump_data, file)


async def fetch_submissions(client: Client, count: int) -> None:
    with custom_open("testdata/Submission_2050.json", "w") as file:
        json.dump(
            await client.api_call(
                "contest.status",
                {"contestId": 2050, "count": count},
                convert_case=False,
            ),
            file,
        )


async def fetch_contests(client: Client, count: int) -> None:
    with custom_open("testdata/Contest_f" + str(count) + ".json", "w") as file:
        json.dump(
            (await client.api_call("contest.list", {}, convert_case=False))[:count],
            file,
        )


async def fetch_problemset_data(client: Client, count: int) -> None:
    data: List[List[Dict[str, Any]]] = await client.api_call(
        "problemset.problems", {}, convert_case=False
    )

    with custom_open("testdata/Problem_f" + str(count) + ".json", "w") as file:
        dump_data: List[Dict[str, Any]] = []
        for x in range(0, count):
            dump_data.append(data["problems"][x])
        json.dump(dump_data, file)

    with custom_open(
        "testdata/ProblemStatistics_f" + str(count) + ".json", "w"
    ) as file:
        dump_data: List[Dict[str, Any]] = []
        for x in range(0, count):
            dump_data.append(data["problemStatistics"][x])
        json.dump(dump_data, file)


async def fetch_users(client: Client, count: int) -> None:
    with custom_open("testdata/User_" + str(count) + ".json", "w") as file:
        data: List[Dict[str, Any]] = await client.api_call(
            "user.ratedList", {}, convert_case=False
        )

        dump_data: List[Dict[str, Any]] = []
        steps: int = int(len(data) / count)
        for x in range(0, len(data), steps):
            dump_data.append(data[steps])
        del data

        json.dump(dump_data, file)


async def fetch_recent_actions(client: Client, count: int) -> None:
    with custom_open(
        "testdata/RecentAction_f" + str(min(100, count)) + ".json", "w"
    ) as file:
        json.dump(
            await client.api_call(
                "recentActions", {"maxCount": min(100, count)}, convert_case=False
            ),
            file,
        )


async def fetch_comments(client: Client, _: int) -> None:
    with custom_open("testdata/Comment_131.json", "w") as file:
        json.dump(
            await client.api_call(
                "blogEntry.comments", {"blogEntryId": 137534}, convert_case=False
            ),
            file,
        )


async def fetch_blog_entries(client: Client, count: int) -> None:
    with custom_open("testdata/BlogEntry_20.json", "w") as file:
        entries: List[Any] = []
        for x in [137507, 137526, 137534, 137571, 137612, 137622]:
            entries.append(
                await client.api_call(
                    "blogEntry.view", {"blogEntryId": x}, convert_case=False
                )
            )

        json.dump(entries, file)


async def main(count: int):
    os.makedirs(os.path.join(os.path.dirname(__file__), "testdata"), exist_ok=True)
    async with aiohttp.ClientSession() as session:
        client: Client = Client(session)

        for call in [
            fetch_submissions,
            fetch_hacks,
            fetch_standings,
            fetch_comments,
            fetch_contests,
            fetch_users,
            fetch_blog_entries,
            fetch_recent_actions,
            fetch_rating_changes,
        ]:
            await call(client, count)
            await asyncio.sleep(1)


if __name__ == "__main__":
    asyncio.run(main(500))
