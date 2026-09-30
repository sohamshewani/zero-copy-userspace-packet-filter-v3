from include.packet_filter import PacketFilter
from include.sliding_window import SlidingWindow
from include.ring_buffer import RingBufferManager
from errors import InvalidPacketError, BufferOverflowError


class PacketFilterEngine:
    def __init__(self, rules: list, buffer_size: int):
        self.filter = PacketFilter(rules)
        self.buffer_manager = RingBufferManager(buffer_size)
        self.sliding_window = SlidingWindow(buffer_size)
        self.packets_handled = 0

    def process_packet(self, packet: bytes) -> PacketType:
        try:
            self.sliding_window.enqueue(self.filter.filter_packet(packet))
            self.buffer_manager.enqueue_packet(packet)
            self.packets_handled += 1
        except InvalidPacketError as e:
            print(f'Invalid packet received: {e}')
        except BufferOverflowError as e:
            print(f'Buffer overflow: {e}')
        return self.filter.filter_packet(packet)
