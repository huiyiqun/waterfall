class Bitstring(object):
    def __init__(self, bytes):
        self.bytes = bytes

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
                return (self.bytes[key // 8] >> (key % 8)) & 1
        else:
            raise TypeError("Invalid argument type")

    def __len__(self):
        return len(self.bytes) * 8
