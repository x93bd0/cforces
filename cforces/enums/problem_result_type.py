from enum import Enum


class ProblemResultType(Enum):
    #: Results that may be subject to changes (by hacks, or the system tests).
    PRELIMINARY: str = "PRELIMINARY"
    #: Results that cannot change.
    FINAL: str = "FINAL"
