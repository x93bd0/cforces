from datetime import timedelta
from typing import List, Dict, Any

from ..object import Object
from ..user.party import Party
from ..problem.problem_result import ProblemResult


class RanklistRow(Object):
    """Represents a ranklist row."""

    __slots__ = (
        "party",
        "rank",
        "points",
        "penalty",
        "successful_hack_count",
        "unsuccessful_hack_count",
        "problem_results",
        "last_submission_time_seconds",
    )

    party: Party
    rank: int
    points: float
    penalty: int
    successful_hack_count: int
    unsuccessful_hack_count: int
    problem_results: List[ProblemResult]
    last_submission_time_seconds: int

    @property
    def last_submission_time(self) -> timedelta:
        return timedelta(self.last_submission_time_seconds)

    @staticmethod
    def from_dict(raw_data: Dict[str, Any]) -> "RanklistRow":
        problem_results: List[ProblemResult] = []
        for raw_problem_result in raw_data["problem_results"]:
            problem_results.append(ProblemResult.from_dict(raw_problem_result))
        raw_data["problem_results"] = problem_results
        return RanklistRow(**raw_data)
