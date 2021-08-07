from enum import Enum, auto


class ResourceType(Enum):
    EC2 = auto()
    S3 = auto()
    SNS = auto()
    SQS = auto()
