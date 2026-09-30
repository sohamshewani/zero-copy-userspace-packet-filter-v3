from src.packet_filter_engine import PacketFilterEngine
from include.types import PacketType
from include.errors import BufferOverflowError, InvalidPacketError
from tests.test_integration import run_integration_tests


def main():
    rules = [
        {'protocol': 'TCP', 'allowed': True},
        {'protocol': 'UDP', 'allowed': False}
    ]
    engine = PacketFilterEngine(rules, buffer_size=1024)
    try:
        run_integration_tests(engine)
    except BufferOverflowError as e:
        print(f'Error during integration tests: {e}')
    except InvalidPacketError as e:
        print(f'Invalid packet during tests: {e}')

if __name__ == '__main__':
    main()
