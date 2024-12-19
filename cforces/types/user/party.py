from datetime import datetime
from typing import List, Dict, Any

from ..object import Object
from ..user.member import Member
from ...enums import ParticipantType


class Party(Object):
    """Represents a party, participating in a contest."""

    __slots__ = (
        "contest_id",
        "members",
        "participant_type",
        "team_id",
        "team_name",
        "ghost",
        "room",
        "start_time_seconds",
    )

    contest_id: int | None
    members: List[Member]
    participant_type: ParticipantType
    team_id: int | None
    team_name: str | None
    ghost: bool
    room: int | None
    start_time_seconds: int | None

    @property
    def start_time(self) -> datetime:
        return datetime.fromtimestamp(self.start_time_seconds)

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "Party":
        members: List[Member] = []
        for raw_member in raw_data["members"]:
            members.append(Member.from_dict(raw_member))

        raw_data["participant_type"] = ParticipantType(raw_data["participant_type"])
        return Party(**raw_data)
