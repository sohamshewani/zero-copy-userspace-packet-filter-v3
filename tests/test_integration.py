import unittest
from src.packet_filter_engine import PacketFilterEngine
from include.types import PacketType


class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.engine = PacketFilterEngine(rules=[{'protocol': 'TCP', 'allowed': True}], buffer_size=10)

    def test_integration(self):
        packets = [b'valid packet', b'invalid packet'] * 10
        for packet in packets:
            self.engine.process_packet(packet)
        self.assertEqual(self.engine.sliding_window.get_size(), 10)
        self.assertEqual(self.engine.buffer_manager.get_packet_count(), 10)

if __name__ == '__main__':
    unittest.main()
