# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Model

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Vertices(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Vertices()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVertices(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Vertices
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Vertices
    def Buffer(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            a = self._tab.Vector(o)
            return self._tab.Get(flatbuffers.number_types.Uint8Flags, a + flatbuffers.number_types.UOffsetTFlags.py_type(j * 1))
        return 0

    # Vertices
    def BufferAsNumpy(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.GetVectorAsNumpy(flatbuffers.number_types.Uint8Flags, o)
        return 0

    # Vertices
    def BufferLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # Vertices
    def BufferIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        return o == 0

def VerticesStart(builder):
    builder.StartObject(1)

def Start(builder):
    VerticesStart(builder)

def VerticesAddBuffer(builder, buffer):
    builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(buffer), 0)

def AddBuffer(builder, buffer):
    VerticesAddBuffer(builder, buffer)

def VerticesStartBufferVector(builder, numElems):
    return builder.StartVector(1, numElems, 1)

def StartBufferVector(builder, numElems):
    return VerticesStartBufferVector(builder, numElems)

def VerticesEnd(builder):
    return builder.EndObject()

def End(builder):
    return VerticesEnd(builder)

try:
    from typing import List
except:
    pass

class VerticesT(object):

    # VerticesT
    def __init__(self):
        self.buffer = None  # type: List[int]

    @classmethod
    def InitFromBuf(cls, buf, pos):
        vertices = Vertices()
        vertices.Init(buf, pos)
        return cls.InitFromObj(vertices)

    @classmethod
    def InitFromPackedBuf(cls, buf, pos=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, pos)
        return cls.InitFromBuf(buf, pos+n)

    @classmethod
    def InitFromObj(cls, vertices):
        x = VerticesT()
        x._UnPack(vertices)
        return x

    # VerticesT
    def _UnPack(self, vertices):
        if vertices is None:
            return
        if not vertices.BufferIsNone():
            if np is None:
                self.buffer = []
                for i in range(vertices.BufferLength()):
                    self.buffer.append(vertices.Buffer(i))
            else:
                self.buffer = vertices.BufferAsNumpy()

    # VerticesT
    def Pack(self, builder):
        if self.buffer is not None:
            if np is not None and type(self.buffer) is np.ndarray:
                buffer = builder.CreateNumpyVector(self.buffer)
            else:
                VerticesStartBufferVector(builder, len(self.buffer))
                for i in reversed(range(len(self.buffer))):
                    builder.PrependUint8(self.buffer[i])
                buffer = builder.EndVector()
        VerticesStart(builder)
        if self.buffer is not None:
            VerticesAddBuffer(builder, buffer)
        vertices = VerticesEnd(builder)
        return vertices
