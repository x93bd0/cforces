from enum import Enum


class ParticipantType(Enum):
    #: Contestants who are participating live in the contest.
    CONTESTANT: str = "CONTESTANT"
    #: Contestants who are participating in practice mode in the contest.
    PRACTICE: str = "PRACTICE"
    #: Contestants who are participating in virtual mode in the contest.
    VIRTUAL: str = "VIRTUAL"
    #: Managers of the contest.
    MANAGER: str = "MANAGER"
    #: Contestants who don't meet the rating requirements for the contest.
    OUT_OF_COMPETITION: str = "OUT_OF_COMPETITION"
