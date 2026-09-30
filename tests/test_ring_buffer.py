import unittest
from src.ring_buffer_manager import RingBufferManager
from include.types import PacketType


class TestRingBuffer(unittest.TestCase):
    def setUp(self):
        self.manager = RingBufferManager(buffer_size=10)

    def test_enqueue(self):
        for i in range(10):
            self.manager.enqueue_packet(bytes([i]))
        self.assertEqual(self.manager.get_packet_count(), 10)

    def test_dequeue(self):
        for i in range(10):
            self.manager.enqueue_packet(bytes([i]))
        for i in range(10):
            self.assertEqual(self.manager.dequeue_packet(), bytes([i]))
        self.assertEqual(self.manager.get_packet_count(), 0)

if __name__ == '__main__':
    unittest.main()
