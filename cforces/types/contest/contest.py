from datetime import timedelta, datetime
from typing import Dict, Any, List

from ..object import Object
from ..problem.submission import Submission
from ...enums import ContestType, ContestPhase


class Contest(Object):
    """Represents a contest on Codeforces."""

    __slots__ = (
        "id",
        "name",
        "type",
        "phase",
        "frozen",
        "duration_seconds",
        "freeze_duration_seconds",
        "start_time_seconds",
        "relative_time_seconds",
        "prepared_by",
        "website_url",
        "description",
        "difficulty",
        "kind",
        "icpc_region",
        "country",
        "city",
        "season",
    )

    id: int
    name: str
    type: ContestType
    phase: ContestPhase
    frozen: bool
    duration_seconds: int | None
    freeze_duration_seconds: int | None
    start_time_seconds: int | None
    relative_time_seconds: int | None
    prepared_by: str
    website_url: str
    description: str
    difficulty: int
    kind: str
    icpc_region: str
    country: str
    city: str
    season: str

    def duration(self) -> timedelta:
        return timedelta(seconds=self.duration_seconds)

    def freeze_duration(self) -> timedelta:
        return timedelta(seconds=self.freeze_duration_seconds)

    def start_time(self) -> datetime:
        return datetime(self.start_time_seconds)

    def relative_time(self) -> timedelta:
        return timedelta(seconds=self.relative_time_seconds)

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "Contest":
        raw_data["contest_type"] = ContestType(raw_data["contest_type"])
        raw_data["contest_phase"] = ContestPhase(raw_data["contest_phase"])
        return Contest(**raw_data)
