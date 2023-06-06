from enum import Enum
from struct import unpack_from, calcsize


class Types(Enum):
    float = "f"
    double = "d"
    uint8 = "B"
    uint16 = "H"
    uint32 = "I"
    uint64 = "Q"
    int8 = "b"
    int16 = "h"
    int32 = "i"
    int64 = "q"
    char = "c"


class BinaryReader():
    def __init__(self, offset, buffer):
        self.offset = offset
        self.buffer = buffer
        self.pattern = '<'

    def read(self, _pattern):
        pattern = self.pattern + _pattern.value
        result = unpack_from(pattern, self.buffer, self.offset)
        self.offset += calcsize(pattern)
        return result[0]

    def readWithSize(self, _pattern, size):
        res = []
        for i in range(0, size):
            pattern = self.pattern + _pattern.value
            result = unpack_from(pattern, self.buffer, self.offset)
            self.offset += calcsize(pattern)
            res.append(result[0])
        return res

    def copy(self, offset):
        return BinaryReader(offset, self.buffer)


def readE(reader):
    e1 = reader.read(Types.float)
    e2 = reader.read(Types.uint64)
    e3 = reader.read(Types.uint32)
    e4 = reader.read(Types.int32)
    return dict(E1=e1, E2=e2, E3=e3, E4=e4)


def readC(reader):
    c1 = reader.read(Types.double)
    c2 = reader.read(Types.float)
    return dict(C1=c1, C2=c2)


def readD(reader):
    d1 = reader.read(Types.double)
    d2 = reader.read(Types.int8)
    d3 = reader.read(Types.int32)
    d4 = reader.read(Types.double)
    return dict(D1=d1, D2=d2, D3=d3, D4=d4)


def readB(reader, buffer):
    b1 = reader.read(Types.int64)
    size2 = reader.read(Types.uint16)
    adress2 = reader.read(Types.uint16)
    b2 = []
    cReader = BinaryReader(offset=adress2, buffer=buffer)
    for _ in range(0, size2):
        b2.append(
            readC(BinaryReader(offset=cReader.read(Types.uint16),
                               buffer=buffer)))
    b3 = reader.readWithSize(Types.uint8, 8)
    b4 = readD(reader)
    size5 = reader.read(Types.uint32)
    adress5 = reader.read(Types.uint16)
    b5 = reader.copy(offset=adress5).readWithSize(Types.uint8, size5)
    return dict(B1=b1, B2=b2, B3=b3, B4=b4, B5=b5)


def main(buffer):
    reader = BinaryReader(offset=3, buffer=buffer)
    a1 = reader.read(Types.int32)
    a2 = reader.readWithSize(Types.uint8, 5)
    a3 = reader.read(Types.uint32)
    a4 = readB(reader, buffer)
    return dict(A1=a1, A2=a2, A3=a3, A4=a4)