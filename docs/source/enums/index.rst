Enumerations
============

The Codeforces API has several enumerations for describing internal states,
which are implemented at the :mod:`cforces.enums` module for making coding easier.

The following enumerations are built-in:

.. list-table:: List of enumerations
    :header-rows: 1

    * - Name
      - Description
    * - :class:`~cforces.enums.ContestPhase`
      - The phase in which the contest is. (Used at
        :attr:`~cforces.types.contest.Contest.phase` attribute of
        :class:`~cforces.types.contest.Contest` class)
    * - :class:`~cforces.enums.ContestType`
      - The type of the contest. (Used at
        :attr:`~cforces.types.contest.Contest.type` attribute of
        :class:`~cforces.types.contest.Contest` class)
    * - :class:`~cforces.enums.ParticipantType`
      - The type of participant in the contest (Used at
        :attr:`~cforces.types.user.Party.participant_type` attribute of
        :class:`~cforces.types.user.Party` class)
    * - :class:`~cforces.enums.ProblemResultType`
      - Describes the type of result a party can get from a problem.
        (Used at :attr:`~cforces.types.contest.RanklistRow.results` attribute of
        :class:`~cforces.types.contest.RanklistRow` class)
    * - :class:`~cforces.enums.ProblemType`
      - Undocumented (TODO)
    * - :class:`~cforces.enums.Rank`
      - A non-API enumeration that describes available ranks.
    * - :class:`~cforces.enums.TestSet`
      - Undocumented (TODO)
    * - :class:`~cforces.enums.Verdict`
      - Undocumented (TODO)

.. toctree::
    :hidden:

    ContestPhase <contest_phase>
    ContestType <contest_type>
    ParticipantType <participant_type>
    ProblemResultType <problem_result_type>
    ProblemType <problem_type>
    Rank <rank>
    TestSet <testset>
    Verdict <verdict>
