<a id="readme-top"></a>
[![Built With][BuiltWithPy-Badge]][BuiltWithPy-Link]
[![Stargazers][Stars-Badge]][Stars-Link]
[![License][License-Badge]][License-Link]
[![Telegram Channel][Telegram-Badge]][Telegram-Link]

<br />
<div align="center">
  <a href="https://github.com/x93bd0/cforces">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Codeforces_logo.svg/512px-Codeforces_logo.svg.png" alt="Logo" width="512" height="60">
  </a>

  <h3 align="center">Python Codeforces API</h3>
  <p align="center">
    A Codeforces API wrapper for Python.
    <br />
    <a href="https://github.com/x93bd0/cforces/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/x93bd0/cforces/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>

## About The Project
`cforces` is a complete implementation of the [Codeforces-API][CodeforcesAPI-Link], featuring classes for every type of the API, each with detailed documentation for a better understanding.

It's heavily inspired on [Pyrogram][Pyrogram-Link] structure and documentation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Installation
### From PyPi (stable)
```sh
pip install cforces
```

### From Github (latest)
```
pip install git+https://github.com/x93bd0/cforces/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Basic Usage
As an example, in the following code snippet we are obtaining the handles of the friends of the authenticated user and printing their user objects:

```python
from cforces import Client, types
from typing import List
import asyncio


async def main() -> None:
    client: Client = Client()  # Instantiate a Client object.
    client.auth(
        YOUR_API_KEY, YOUR_API_SECRET
    )  # Authenticate yourself with your api_key + api_secret.

    async with client as api:
        friends_handles: List[str] = (
            await api.user_friends()
        )  # Fetch authenticated user's friends.
        friends_users: List[User] = await api.user_info(
            friends_handles
        )  # Fetch a user object for each of those.

        for user in friends_users:
            print(user)  # Print it.


if __name__ == "__main__":
    asyncio.run(main())
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## TODO List

- [ ] Finish the documentation.
- [ ] Implement helper methods for making the interaction easier.
- [ ] Find every possible error and implement it. (partial impl)
- [ ] Add tests.
- [ ] Fix bug: When a ';' is returned in the error comments, it is treated as a whole new error.
- [ ] Better cc2sc

## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

[CodeforcesAPI-Link]: https://codeforces.com/apiHelp
[Pyrogram-Link]: https://github.com/pyrogram/pyrogram/

[BuiltWithPy-Badge]: https://img.shields.io/badge/Built_With-Python-blue?style=for-the-badge&logo=python&logoColor=white
[BuiltWithPy-Link]: https://python.org/

[Stars-Badge]: https://img.shields.io/github/stars/x93bd0/cforces?style=for-the-badge
[Stars-Link]: https://github.com/x93bd0/cforces/stargazers

[License-Badge]: https://img.shields.io/github/license/x93bd0/cforces?style=for-the-badge
[License-Link]: https://github.com/x93bd0/cforces/blob/master/LICENSE.txt

[Telegram-Badge]: https://img.shields.io/badge/Telegram_Channel-grey?style=for-the-badge&logo=telegram&logoColor=white
[Telegram-Link]: https://t.me/x93dev
