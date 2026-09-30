import unittest
from src.packet_filter_engine import PacketFilterEngine
from include.types import PacketType


class TestSlidingWindow(unittest.TestCase):
    def setUp(self):
        self.engine = PacketFilterEngine(rules=[{'protocol': 'TCP', 'allowed': True}], buffer_size=10)

    def test_enqueue(self):
        for i in range(10):
            self.engine.process_packet(bytes([i]))
        self.assertEqual(self.engine.sliding_window.get_size(), 10)

    def test_dequeue(self):
        for i in range(10):
            self.engine.process_packet(bytes([i]))
        for i in range(10):
            self.assertEqual(self.engine.sliding_window.dequeue_packet(), PacketType.TCP)
        self.assertEqual(self.engine.sliding_window.get_size(), 0)

if __name__ == '__main__':
    unittest.main()
