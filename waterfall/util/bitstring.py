class Bitstring(object):
    def __init__(self, bytes):
        self._bytes = bytearray(bytes)

    def __getitem__(self, key):
        if isinstance(key, slice):
            ret = 0
            for offset, index in enumerate(range(*key.indices(len(self)))):
                ret += self[index] << offset
            return ret
        elif isinstance(key, int):
            if key < -len(self) or key >= len(self):
                raise IndexError("The index (%d) is out of range." % key)
            if key < 0:
                return self[len(self)+key]
            else:
                return (self._bytes[key // 8] >> (key % 8)) & 1
        else:
            raise TypeError("Invalid argument type")

    def __setitem__(self, key, value):
        if isinstance(key, slice):
            iteration = range(*key.indices(len(self)))
            assert (2 << len(iteration)) // 2 > value >= 0
            for offset, index in enumerate(iteration):
                self[index] = (value >> offset) & 1
        elif isinstance(key, int):
            assert value in [0, 1]
            if key < -len(self) or key >= len(self):
                raise IndexError("The index (%d) is out of range." % key)
            if key < 0:
                self[len(self)+key] = value
            else:
                self._bytes[key // 8] &= (1 << (key % 8)) ^ 255
                self._bytes[key // 8] |= value << (key % 8)
        else:
            raise TypeError("Invalid argument type")

    def __len__(self):
        return len(self._bytes) * 8

    @property
    def bytes(self):
        return bytes(self._bytes)

    @property
    def list(self):
        return list(self._bytes)
