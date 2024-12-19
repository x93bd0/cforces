from enum import Enum


class ContestPhase(Enum):
    #: The contest has not yet started.
    BEFORE: str = "BEFORE"
    #: The contest has started.
    CODING: str = "CODING"
    #: The contest has ended, but system tests are pending.
    PENDING_SYSTEM_TEST: str = "PENDING_SYSTEM_TEST"
    #: The contest has ended, and system tests are running.
    SYSTEM_TEST: str = "SYSTEM_TEST"
    #: The contest has ended, and it is not subject to any changes.
    FINISHED: str = "FINISHED"
