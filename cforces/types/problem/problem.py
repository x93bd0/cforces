from typing import List, Dict, Any

from ..object import Object
from ...enums import ProblemType


class Problem(Object):
    """Represents a problem."""

    __slots__ = (
        "contest_id",
        "problemset_name",
        "index",
        "name",
        "type",
        "points",
        "rating",
        "tags",
    )

    contest_id: int | None
    problemset_name: str | None
    index: str
    name: str
    type: ProblemType
    points: float | None
    rating: int | None
    tags: List[str]

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "Problem":
        raw_data["type"] = ProblemType(raw_data["type"])
        return Problem(**raw_data)
