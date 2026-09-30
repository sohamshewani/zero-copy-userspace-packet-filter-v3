class ZeroCopyFilterError(Exception):
    pass


class BufferOverflowError(ZeroCopyFilterError):
    pass


class InvalidPacketError(ZeroCopyFilterError):
    pass
