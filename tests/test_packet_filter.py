import unittest
from src.packet_filter_engine import PacketFilterEngine
from include.types import PacketType


class TestPacketFilter(unittest.TestCase):
    def setUp(self):
        self.engine = PacketFilterEngine(rules=[{'protocol': 'TCP', 'allowed': True}], buffer_size=10)

    def test_valid_packet(self):
        packet = b'valid packet'
        self.assertEqual(self.engine.process_packet(packet), PacketType.TCP)

    def test_invalid_packet(self):
        packet = b'invalid packet'
        with self.assertRaises(InvalidPacketError):
            self.engine.process_packet(packet)

if __name__ == '__main__':
    unittest.main()
