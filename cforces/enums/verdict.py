from enum import Enum


class Verdict(Enum):
    #: Undocumented (TODO)
    FAILED: str = "FAILED"
    #: Undocumented (TODO)
    OK: str = "OK"
    #: Undocumented (TODO)
    PARTIAL: str = "PARTIAL"
    #: Undocumented (TODO)
    COMPILATION_ERROR: str = "COMPILATION_ERROR"
    #: Undocumented (TODO)
    RUNTIME_ERROR: str = "RUNTIME_ERROR"
    #: Undocumented (TODO)
    WRONG_ANSWER: str = "WRONG_ANSWER"
    #: Undocumented (TODO)
    PRESENTATION_ERROR: str = "PRESENTATION_ERROR"
    #: Undocumented (TODO)
    TIME_LIMIT_EXCEEDED: str = "TIME_LIMIT_EXCEEDED"
    #: Undocumented (TODO)
    SECURITY_VIOLATED: str = "SECURITY_VIOLATED"
    #: Undocumented (TODO)
    CRASHED: str = "CRASHED"
    #: Undocumented (TODO)
    INPUT_PREPARATION_CRASHED: str = "INPUT_PREPARATION_CRASHED"
    #: Undocumented (TODO)
    CHALLENGED: str = "CHALLENGED"
    #: Undocumented (TODO)
    SKIPPED: str = "SKIPPED"
    #: Undocumented (TODO)
    TESTING: str = "TESTING"
    #: Undocumented (TODO)
    REJECTED: str = "REJECTED"
