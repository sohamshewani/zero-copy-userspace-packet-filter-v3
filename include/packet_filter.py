from types import PacketType
from errors import InvalidPacketError


class PacketFilter:
    def __init__(self, rules: list):
        self.rules = rules

    def filter_packet(self, packet: bytes) -> PacketType:
        for rule in self.rules:
            if rule.matches(packet):
                return rule.allowed_packet_type
        raise InvalidPacketError()
