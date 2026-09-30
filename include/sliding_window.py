from types import PacketType
from errors import BufferOverflowError, InvalidPacketError


class SlidingWindow:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.slots = [False] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0
        self.packet_types = {PacketType.TCP: 0, PacketType.UDP: 0, PacketType.ICMP: 0, PacketType.OTHER: 0}

    def enqueue(self, packet_type: PacketType):
        if self.size == self.capacity:
            raise BufferOverflowError()
        self.slots[self.tail] = True
        self.packet_types[packet_type] += 1
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self) -> PacketType:
        if self.size == 0:
            raise BufferOverflowError()
        packet_type = PacketType.OTHER
        for i in range(self.capacity):
            index = (self.head + i) % self.capacity
            if self.slots[index]:
                packet_type = PacketType(self.packet_types.keys()[i])
                self.slots[index] = False
                self.packet_types[packet_type] -= 1
                break
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return packet_type
