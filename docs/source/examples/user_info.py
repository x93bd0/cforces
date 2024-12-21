from cforces import Client
import asyncio


async def main() -> None:
    client: Client = Client()  # Instantiate a Client object
    async with client as api:  # Enter an async context (for aiohttp.ClientSession to spawn)
        print(await api.user_info(["x93bd0"]))  # Call user.info API method


if __name__ == "__main__":
    asyncio.run(main())
