
from waterfall.util.bitstring import Bitstring
from waterfall.exception import CapacityIsNotEnough


class LSBAlgorithm(object):
    def __init__(self, bit):
        assert 1 < bit <= 8
        self.bit = bit

    def embed(self, secret_space, watermark):
        assert secret_space.ndim == 1
        bitstring = Bitstring(watermark)
        try:
            for i in range(0, len(bitstring), self.bit):
                secret_space[i//self.bit] &= ((1 << (self.bit + 1)) - 1) ^ 255
                secret_space[i//self.bit] |= bitstring[i:i+self.bit]
            return secret_space
        except IndexError:
            raise CapacityIsNotEnough()

    def extract(self, secret_space):
        assert secret_space.ndim == 1
        bitstring = Bitstring([0] * (len(secret_space) * self.bit // 8))
        mask = (1 << self.bit) - 1
        for i in range(len(secret_space)):
            bitstring[i*self.bit:(i+1)*self.bit] = secret_space[i] & mask
        return bitstring.bytes
