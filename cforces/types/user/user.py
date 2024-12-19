from typing import Dict

from ..object import Object
from datetime import datetime


class User(Object):
    """Represents a Codeforces user."""

    __slots__ = (
        "handle",
        "email",
        "vk_id",
        "open_id",
        "first_name",
        "last_name",
        "country",
        "city",
        "organization",
        "contribution",
        "rank",
        "rating",
        "max_rank",
        "max_rating",
        "last_online_time_seconds",
        "registration_time_seconds",
        "friend_of_count",
        "avatar",
        "title_photo",
    )

    handle: str
    email: str | None
    vk_id: str | None
    open_id: str | None
    first_name: str | None
    last_name: str | None
    country: str | None
    city: str | None
    organization: str | None
    contribution: int
    rank: str
    rating: int
    max_rank: str
    max_rating: int
    last_online_time_seconds: int
    registration_time_seconds: int
    friend_of_count: int
    avatar: str
    title_photo: str

    @property
    def last_online_time(self) -> datetime:
        return datetime.fromtimestamp(self.last_online_time_seconds)

    @property
    def registration_time(self) -> datetime:
        return datetime.fromtimestamp(self.registration_time_seconds)

    @staticmethod
    def from_dict(raw_data: Dict[str, int | str]) -> "User":
        return User(**raw_data)
