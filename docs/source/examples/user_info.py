from aiohttp import ClientSession
from cforces import Client
import asyncio


async def main() -> None:
    async with ClientSession() as session:  # Enter an async context (for aiohttp.ClientSession to spawn)
        client: Client = Client(
            session
        )  # Instantiate a Client object and pass the aiohttp session to it.
        print(await client.user_info(["x93bd0"]))  # Call user.info API method


if __name__ == "__main__":
    asyncio.run(main())
