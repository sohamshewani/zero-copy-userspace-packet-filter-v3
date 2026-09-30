from include.ring_buffer import RingBuffer


class RingBufferManager:
    def __init__(self, buffer_size: int):
        self.buffer = RingBuffer(buffer_size)

    def enqueue_packet(self, packet: bytes):
        self.buffer.enqueue(packet)

    def dequeue_packet(self) -> bytes:
        return self.buffer.dequeue()

    def is_empty(self) -> bool:
        return self.buffer.is_empty()

    def get_packet_count(self) -> int:
        return self.buffer.get_size()
