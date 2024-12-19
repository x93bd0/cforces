from typing import Any, Dict

from . import Problem
from ..object import Object
from ..user.party import Party
from ...enums.verdict import Verdict


class Hack(Object):
    """Represents a hack, made during Codeforces Round."""

    __slots__ = (
        "id",
        "creation_time_seconds",
        "hacker",
        "defender",
        "verdict",
        "problem",
        "test",
        "judge_protocol",
    )

    id: int
    contest_id: int
    hacker: Party
    defender: Party
    verdict: Verdict
    problem: Problem
    test: str | None
    judge_protocol: Dict[str, Any] | None  # TODO: Create a type for this

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "Hack":
        raw_data["hacker"] = Party.from_dict(raw_data["hacker"])
        raw_data["defender"] = Party.from_dict(raw_data["defender"])
        raw_data["verdict"] = Verdict(raw_data["verdict"])
        raw_data["problem"] = Problem(raw_data["problem"])
        return Hack(**raw_data)
