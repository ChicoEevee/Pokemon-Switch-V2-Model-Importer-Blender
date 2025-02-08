# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Morphs(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Morphs()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMorphs(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Morphs
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Morphs
    def MorphBuffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from Titan.Model.MorphBuffer import MorphBuffer
            obj = MorphBuffer()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Morphs
    def MorphBufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Morphs
    def MorphBufferIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def MorphsStart(builder):
    builder.StartObject(1)

def Start(builder):
    MorphsStart(builder)

def MorphsAddMorphBuffer(builder, morphBuffer):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(morphBuffer), 0)

def AddMorphBuffer(builder, morphBuffer):
    MorphsAddMorphBuffer(builder, morphBuffer)

def MorphsStartMorphBufferVector(builder, numElems):
    return builder.StartVector(4, numElems, 4)

def StartMorphBufferVector(builder, numElems):
    return MorphsStartMorphBufferVector(builder, numElems)

def MorphsEnd(builder):
    return builder.EndObject()

def End(builder):
    return MorphsEnd(builder)

import Titan.Model.MorphBuffer
try:
    from typing import List
except:
    pass

class MorphsT(object):

    # MorphsT
    def __init__(self):
        self.morphBuffer = None  # type: List[Titan.Model.MorphBuffer.MorphBufferT]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        morphs = Morphs()
        morphs.Init(buf, pos)
        return cls.InitFromObj(morphs)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, morphs):
        x = MorphsT()
        x._UnPack(morphs)
        return x

    # MorphsT
    def _UnPack(self, morphs):
        if morphs is None:
            return
        if not morphs.MorphBufferIsNone():
            self.morphBuffer = []
            for i in range(morphs.MorphBufferLength()):
                if morphs.MorphBuffer(i) is None:
                    self.morphBuffer.append(None)
                else:
                    morphBuffer_ = Titan.Model.MorphBuffer.MorphBufferT.InitFromObj(morphs.MorphBuffer(i))
                    self.morphBuffer.append(morphBuffer_)

    # MorphsT
    def Pack(self, builder):
        if self.morphBuffer is not None:
            morphBufferlist = []
            for i in range(len(self.morphBuffer)):
                morphBufferlist.append(self.morphBuffer[i].Pack(builder))
            MorphsStartMorphBufferVector(builder, len(self.morphBuffer))
            for i in reversed(range(len(self.morphBuffer))):
                builder.PrependUOffsetTRelative(morphBufferlist[i])
            morphBuffer = builder.EndVector()
        MorphsStart(builder)
        if self.morphBuffer is not None:
            MorphsAddMorphBuffer(builder, morphBuffer)
        morphs = MorphsEnd(builder)
        return morphs
