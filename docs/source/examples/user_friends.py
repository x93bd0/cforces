from cforces import Client
import asyncio


YOUR_API_KEY: str = "abcdefghijklmnopqrstuvwxz1234567890abcde"
YOUR_API_SECRET: str = "abcdefghijklmnopqrstuvwxz1234567890abcde"


async def main() -> None:
    client: Client = Client()  # Instantiate a Client object
    client.auth(
        YOUR_API_KEY, YOUR_API_SECRET
    )  # Authenticate the client with an api key & secret pair

    async with client as api:  # Enter an async context (for aiohttp.ClientSession to spawn)
        print(await api.user_friends())  # Call user.friends API method


if __name__ == "__main__":
    asyncio.run(main())
