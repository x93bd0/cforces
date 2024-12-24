from aiohttp import ClientSession
from cforces import Client
import asyncio


YOUR_API_KEY: str = "abcdefghijklmnopqrstuvwxz1234567890abcde"
YOUR_API_SECRET: str = "abcdefghijklmnopqrstuvwxz1234567890abcde"


async def main() -> None:
    async with ClientSession() as session:  # Enter an async context (for aiohttp.ClientSession to spawn)
        client: Client = Client(
            session
        )  # Instantiate a Client object and pass the aiohttp session to it.

        client.auth(
            YOUR_API_KEY, YOUR_API_SECRET
        )  # Authenticate the client with an api key & secret pair

        print(await client.user_friends())  # Call user.friends API method


if __name__ == "__main__":
    asyncio.run(main())
