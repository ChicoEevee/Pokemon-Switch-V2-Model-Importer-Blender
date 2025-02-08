# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TRMBF(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TRMBF()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTRMBF(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TRMBF
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TRMBF
    def Unused(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Uint32Flags, o + self._tab.Pos)
        return 0

    # TRMBF
    def Buffers(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Titan.Model.Buffer import Buffer
            obj = Buffer()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TRMBF
    def BuffersLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TRMBF
    def BuffersIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        return o == 0

def TRMBFStart(builder):
    builder.StartObject(2)

def Start(builder):
    TRMBFStart(builder)

def TRMBFAddUnused(builder, unused):
    builder.PrependUint32Slot(0, unused, 0)

def AddUnused(builder, unused):
    TRMBFAddUnused(builder, unused)

def TRMBFAddBuffers(builder, buffers):
    builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(buffers), 0)

def AddBuffers(builder, buffers):
    TRMBFAddBuffers(builder, buffers)

def TRMBFStartBuffersVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartBuffersVector(builder, numElems):
    return TRMBFStartBuffersVector(builder, numElems)

def TRMBFEnd(builder):
    return builder.EndObject()

def End(builder):
    return TRMBFEnd(builder)

import Titan.Model.Buffer
try:
    from typing import List
except:
    pass

class TRMBFT(object):

    # TRMBFT
    def __init__(self):
        self.unused = 0  # type: int
        self.buffers = None  # type: List[Titan.Model.Buffer.BufferT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        trmbf = TRMBF()
        trmbf.Init(buf, pos)
        return cls.InitFromObj(trmbf)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, trmbf):
        x = TRMBFT()
        x._UnPack(trmbf)
        return x

    # TRMBFT
    def _UnPack(self, trmbf):
        if trmbf is None:
            return
        self.unused = trmbf.Unused()
        if not trmbf.BuffersIsNone():
            self.buffers = []
            for i in range(trmbf.BuffersLength()):
                if trmbf.Buffers(i) is None:
                    self.buffers.append(None)
                else:
                    buffer_ = Titan.Model.Buffer.BufferT.InitFromObj(trmbf.Buffers(i))
                    self.buffers.append(buffer_)

    # TRMBFT
    def Pack(self, builder):
        if self.buffers is not None:
            bufferslist = []
            for i in range(len(self.buffers)):
                bufferslist.append(self.buffers[i].Pack(builder))
            TRMBFStartBuffersVector(builder, len(self.buffers))
            for i in reversed(range(len(self.buffers))):
                builder.PrependUOffsetTRelative(bufferslist[i])
            buffers = builder.EndVector()
        TRMBFStart(builder)
        TRMBFAddUnused(builder, self.unused)
        if self.buffers is not None:
            TRMBFAddBuffers(builder, buffers)
        trmbf = TRMBFEnd(builder)
        return trmbf
