from enum import Enum


# TODO: Implement __getitem__ (TestSet[n] -> TESTS_n)


class TestSet(Enum):
    #: Samples testset data shown in problem statement.
    SAMPLES: str = "SAMPLES"
    #: Light tests used before tests on certain contest types.
    PRETESTS = "PRETESTS"
    #: Problem system tests.
    TESTS = "TESTS"
    #: Undocumented (TODO)
    CHALLENGES: str = "CHALLENGES"

    #: Testset #1
    TESTS1: str = "TESTS1"
    #: Testset #2
    TESTS2: str = "TESTS2"
    #: Testset #3
    TESTS3: str = "TESTS3"
    #: Testset #4
    TESTS4: str = "TESTS4"
    #: Testset #5
    TESTS5: str = "TESTS5"
    #: Testset #6
    TESTS6: str = "TESTS6"
    #: Testset #7
    TESTS7: str = "TESTS7"
    #: Testset #8
    TESTS8: str = "TESTS8"
    #: Testset #9
    TESTS9: str = "TESTS9"
    #: Testset #10
    TESTS10: str = "TESTS10"
