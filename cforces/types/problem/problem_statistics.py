from typing import Dict, Any

from ..object import Object


class ProblemStatistics(Object):
    """Represents a statistic data about a problem."""

    __slots__ = ("contest_id", "index", "solved_count")

    contest_id: int | None
    index: str
    solved_count: int

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "ProblemStatistics":
        return ProblemStatistics(**raw_data)
