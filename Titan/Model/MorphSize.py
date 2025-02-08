# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MorphSize(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MorphSize()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMorphSize(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MorphSize
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MorphSize
    def Size(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

def MorphSizeStart(builder):
    builder.StartObject(1)

def Start(builder):
    MorphSizeStart(builder)

def MorphSizeAddSize(builder, size):
    builder.PrependUint32Slot(0, size, 0)

def AddSize(builder, size):
    MorphSizeAddSize(builder, size)

def MorphSizeEnd(builder):
    return builder.EndObject()

def End(builder):
    return MorphSizeEnd(builder)


class MorphSizeT(object):

    # MorphSizeT
    def __init__(self):
        self.size = 0  # type: int

    @classmethod
    def InitFromBuf(cls, buf, pos):
        morphSize = MorphSize()
        morphSize.Init(buf, pos)
        return cls.InitFromObj(morphSize)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, morphSize):
        x = MorphSizeT()
        x._UnPack(morphSize)
        return x

    # MorphSizeT
    def _UnPack(self, morphSize):
        if morphSize is None:
            return
        self.size = morphSize.Size()

    # MorphSizeT
    def Pack(self, builder):
        MorphSizeStart(builder)
        MorphSizeAddSize(builder, self.size)
        morphSize = MorphSizeEnd(builder)
        return morphSize
