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
import logging
from .ttypes import *
from thrift.Thrift import TProcessor
from thrift.transport import TTransport
from tornado import gen
from tornado import concurrent


class Iface(object):
    def emitZipkinBatch(self, spans):
        """
        Parameters:
         - spans
        """
        pass

    def emitBatch(self, batch):
        """
        Parameters:
         - batch
        """
        pass


class Client(Iface):
    def __init__(self, transport, iprot_factory, oprot_factory=None):
        self._transport = transport
        self._iprot_factory = iprot_factory
        self._oprot_factory = (oprot_factory if oprot_factory is not None
                               else iprot_factory)
        self._seqid = 0
        self._reqs = {}
        self._transport.io_loop.spawn_callback(self._start_receiving)

    @gen.engine
    def _start_receiving(self):
        while True:
            try:
                frame = yield self._transport.readFrame()
            except TTransport.TTransportException as e:
                for future in self._reqs.values():
                    future.set_exception(e)
                self._reqs = {}
                return
            tr = TTransport.TMemoryBuffer(frame)
            iprot = self._iprot_factory.getProtocol(tr)
            (fname, mtype, rseqid) = iprot.readMessageBegin()
            method = getattr(self, 'recv_' + fname)
            future = self._reqs.pop(rseqid, None)
            if not future:
                # future has already been discarded
                continue
            try:
                result = method(iprot, mtype, rseqid)
            except Exception as e:
                future.set_exception(e)
            else:
                future.set_result(result)

    def emitZipkinBatch(self, spans):
        """
        Parameters:
         - spans
        """
        self._seqid += 1
        self.send_emitZipkinBatch(spans)

    def send_emitZipkinBatch(self, spans):
        oprot = self._oprot_factory.getProtocol(self._transport)
        oprot.writeMessageBegin('emitZipkinBatch', TMessageType.ONEWAY, self._seqid)
        args = emitZipkinBatch_args()
        args.spans = spans
        args.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()

    def emitBatch(self, batch):
        """
        Parameters:
         - batch
        """
        self._seqid += 1
        self.send_emitBatch(batch)

    def send_emitBatch(self, batch):
        oprot = self._oprot_factory.getProtocol(self._transport)
        oprot.writeMessageBegin('emitBatch', TMessageType.ONEWAY, self._seqid)
        args = emitBatch_args()
        args.batch = batch
        args.write(oprot)
        oprot.writeMessageEnd()
        oprot.trans.flush()


class Processor(Iface, TProcessor):
    def __init__(self, handler):
        self._handler = handler
        self._processMap = {}
        self._processMap["emitZipkinBatch"] = Processor.process_emitZipkinBatch
        self._processMap["emitBatch"] = Processor.process_emitBatch

    def process(self, iprot, oprot):
        (name, type, seqid) = iprot.readMessageBegin()
        if name not in self._processMap:
            iprot.skip(TType.STRUCT)
            iprot.readMessageEnd()
            x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
            oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
            x.write(oprot)
            oprot.writeMessageEnd()
            oprot.trans.flush()
            return
        else:
            return self._processMap[name](self, seqid, iprot, oprot)

    @gen.coroutine
    def process_emitZipkinBatch(self, seqid, iprot, oprot):
        args = emitZipkinBatch_args()
        args.read(iprot)
        iprot.readMessageEnd()
        yield gen.maybe_future(self._handler.emitZipkinBatch(args.spans))

    @gen.coroutine
    def process_emitBatch(self, seqid, iprot, oprot):
        args = emitBatch_args()
        args.read(iprot)
        iprot.readMessageEnd()
        yield gen.maybe_future(self._handler.emitBatch(args.batch))

# HELPER FUNCTIONS AND STRUCTURES


class emitZipkinBatch_args(object):
    """
    Attributes:
     - spans
    """

    thrift_spec = (
        None,  # 0
        (1, TType.LIST, 'spans', (TType.STRUCT, (zipkincore.ttypes.Span, zipkincore.ttypes.Span.thrift_spec), False), None, ),  # 1
    )

    def __init__(self, spans=None,):
        self.spans = spans

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
                    self.spans = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = zipkincore.ttypes.Span()
                        _elem5.read(iprot)
                        self.spans.append(_elem5)
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
        oprot.writeStructBegin('emitZipkinBatch_args')
        if self.spans is not None:
            oprot.writeFieldBegin('spans', TType.LIST, 1)
            oprot.writeListBegin(TType.STRUCT, len(self.spans))
            for iter6 in self.spans:
                iter6.write(oprot)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class emitBatch_args(object):
    """
    Attributes:
     - batch
    """

    thrift_spec = (
        None,  # 0
        (1, TType.STRUCT, 'batch', (jaeger.ttypes.Batch, jaeger.ttypes.Batch.thrift_spec), None, ),  # 1
    )

    def __init__(self, batch=None,):
        self.batch = batch

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
                if ftype == TType.STRUCT:
                    self.batch = jaeger.ttypes.Batch()
                    self.batch.read(iprot)
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
        oprot.writeStructBegin('emitBatch_args')
        if self.batch is not None:
            oprot.writeFieldBegin('batch', TType.STRUCT, 1)
            self.batch.write(oprot)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
