#
# Autogenerated by Thrift Compiler (0.10.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:tornado
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
import sys

from thrift.transport import TTransport


class DependencyLink(object):
    """
    Attributes:
     - parent
     - child
     - callCount
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRING, 'parent', 'UTF8', None, ),  # 1
        (2, TType.STRING, 'child', 'UTF8', None, ),  # 2
        None,  # 3
        (4, TType.I64, 'callCount', None, None, ),  # 4
    )

    def __init__(self, parent=None, child=None, callCount=None,):
        self.parent = parent
        self.child = child
        self.callCount = callCount

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.parent = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.child = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.I64:
                    self.callCount = iprot.readI64()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('DependencyLink')
        if self.parent is not None:
            oprot.writeFieldBegin('parent', TType.STRING, 1)
            oprot.writeString(self.parent.encode('utf-8') if sys.version_info[0] == 2 else self.parent)
            oprot.writeFieldEnd()
        if self.child is not None:
            oprot.writeFieldBegin('child', TType.STRING, 2)
            oprot.writeString(self.child.encode('utf-8') if sys.version_info[0] == 2 else self.child)
            oprot.writeFieldEnd()
        if self.callCount is not None:
            oprot.writeFieldBegin('callCount', TType.I64, 4)
            oprot.writeI64(self.callCount)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.parent is None:
            raise TProtocolException(message='Required field parent is unset!')
        if self.child is None:
            raise TProtocolException(message='Required field child is unset!')
        if self.callCount is None:
            raise TProtocolException(message='Required field callCount is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Dependencies(object):
    """
    Attributes:
     - links
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'links', (TType.STRUCT, (DependencyLink, DependencyLink.thrift_spec), False), None, ),  # 1
    )

    def __init__(self, links=None,):
        self.links = links

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, (self.__class__, self.thrift_spec))
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.LIST:
                    self.links = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = DependencyLink()
                        _elem5.read(iprot)
                        self.links.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, (self.__class__, self.thrift_spec)))
            return
        oprot.writeStructBegin('Dependencies')
        if self.links is not None:
            oprot.writeFieldBegin('links', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.links))
            for iter6 in self.links:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        if self.links is None:
            raise TProtocolException(message='Required field links is unset!')
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
