from enum import Enum


class TopicLevelErrorPolicy(Enum):
    Finalize = "finalize"
    Ignore = "Ignore"
    Raise = "Raise"
