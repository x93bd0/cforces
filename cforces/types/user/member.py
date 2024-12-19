from typing import Dict, Any

from ..object import Object


class Member(Object):
    """Represents a member of a party."""

    __slots__ = ("handle", "name")

    handle: str
    name: str | None

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "Member":
        return Member(**raw_data)
