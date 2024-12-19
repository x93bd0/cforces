from enum import Enum


class Rank(Enum):
    #: User with a rating between or equal to: 0 and 1199
    NEWBIE: str = 'newbie'
    #: User with a rating between or equal to: 1200 and 1399
    PUPIL: str = 'pupil'
    #: User with a rating between or equal to: 1400 and 1599
    SPECIALIST: str = 'specialist'
    #: User with a rating between or equal to: 1600 and 1899
    EXPERT: str = 'expert'
    #: User with a rating between or equal to: 1900 and 2099
    CANDIDATE_MASTER: str = 'candidate master'
    #: User with a rating between or equal to: 2100 and 2299
    MASTER: str = 'master'
    #: User with a rating between or equal to: 2300 and 2399
    INTERNATIONAL_MASTER: str = 'international master'
    #: User with a rating between or equal to: 2400 and 2599
    GRANDMASTER: str = 'grandmaster'
    #: User with a rating between or equal to: 2600 and 2999
    INTERNATIONAL_GRANDMASTER: str = 'international grandmaster'
    #: User with a rating between or equal to: 3000 and 3999
    LEGENDARY_GRANDMASTER: str = 'legendary grandmaster'
    #: User with a rating greater or equal to: 4000
    TOURIST: str = 'tourist'
