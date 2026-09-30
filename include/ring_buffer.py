from types import PacketType


class RingBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, packet: bytes):
        if self.size == self.capacity:
            raise BufferOverflowError()
        self.buffer[self.tail] = packet
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self) -> bytes:
        if self.size == 0:
            raise BufferOverflowError()
        packet = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return packet

    def is_empty(self) -> bool:
        return self.size == 0

    def get_size(self) -> int:
        return self.size
