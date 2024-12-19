from idlelib.iomenu import errors
from typing import Dict, Any, List

from aiohttp import ClientSession
from urllib.parse import urljoin, quote_plus

from .methods import Methods
from .utils import cc2sc
from . import errors

from hashlib import sha512
import random
import string
import time


class Client(Methods):
    __slots__ = ("params", "session", "api_key", "api_secret")
    params: Dict[str, Any]
    session: ClientSession

    api_key: str | None
    api_secret: str | None
    api_url: str = "https://codeforces.com/api/"

    def __init__(self, session: ClientSession | None = None) -> None:
        self.params = {"lang": "en"}
        self.session = session

        self.api_key = None
        self.api_secret = None

    async def __aenter__(self):
        self.session = self.session or ClientSession()
        await self.session.__aenter__()

        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.__aexit__(exc_type, exc_val, exc_tb)

    def auth(self, api_key: str, api_secret: str) -> None:
        self.api_key = api_key
        self.api_secret = api_secret

    @property
    def authorized(self) -> bool:
        return not (self.api_key is None or self.api_secret is None)

    async def api_call(self, method_name: str, params: Dict[str, Any]) -> Any:
        params.update(self.params)

        if self.authorized:
            params["apiKey"] = self.api_key
            params["time"] = int(time.time())

        raw_params: str = ""
        for k, v in sorted(params.items()):
            if not v:
                continue
            raw_params += ("&" if raw_params else "") + k + "=" + str(v)

        if self.authorized:
            rand: str = "".join(
                [random.choice(string.digits + string.ascii_letters) for x in range(6)]
            )

            base_api_sig: str = (
                rand + "/" + method_name + "?" + raw_params + "#" + self.api_secret
            )

            raw_params += (
                ("&" if raw_params else "")
                + "apiSig="
                + rand
                + sha512(base_api_sig.encode()).hexdigest()
            )

        url: str = urljoin(self.api_url, method_name) + "?" + raw_params
        async with self.session.get(url) as resp:
            raw_data: Dict[str, Any] = await resp.json()
            if raw_data["status"] == "FAILED":
                # TODO: Identify errors
                raise errors.Error(raw_data["comment"])

        if isinstance(raw_data["result"], dict):
            return cc2sc(raw_data["result"])
        return raw_data["result"]
