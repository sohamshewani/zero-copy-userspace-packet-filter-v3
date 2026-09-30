from enum import Enum

class PacketType(Enum):
    TCP = 1
    UDP = 2
    ICMP = 3
    OTHER = 4
