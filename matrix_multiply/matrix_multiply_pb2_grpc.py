# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import matrix_multiply_pb2 as matrix__multiply__pb2


class MatrixOperationStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Multiply = channel.unary_unary(
                '/matrix.MatrixOperation/Multiply',
                request_serializer=matrix__multiply__pb2.MatrixRequest.SerializeToString,
                response_deserializer=matrix__multiply__pb2.MatrixResponse.FromString,
                )


class MatrixOperationServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Multiply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MatrixOperationServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Multiply': grpc.unary_unary_rpc_method_handler(
                    servicer.Multiply,
                    request_deserializer=matrix__multiply__pb2.MatrixRequest.FromString,
                    response_serializer=matrix__multiply__pb2.MatrixResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'matrix.MatrixOperation', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MatrixOperation(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Multiply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/matrix.MatrixOperation/Multiply',
            matrix__multiply__pb2.MatrixRequest.SerializeToString,
            matrix__multiply__pb2.MatrixResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
