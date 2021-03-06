# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import data_pb2 as data__pb2


class SnakeStub(object):
    """Generate files
    python -m grpc_tools.protoc -I./. --python_out=. --grpc_python_out=. ./data.proto

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.send_high_score = channel.unary_unary(
                '/DATA2410_Portfolio2.Snake/send_high_score',
                request_serializer=data__pb2.High_score.SerializeToString,
                response_deserializer=data__pb2.Confirmed.FromString,
                )
        self.send_fruit = channel.unary_unary(
                '/DATA2410_Portfolio2.Snake/send_fruit',
                request_serializer=data__pb2.Position.SerializeToString,
                response_deserializer=data__pb2.Confirmed.FromString,
                )
        self.send_player = channel.unary_unary(
                '/DATA2410_Portfolio2.Snake/send_player',
                request_serializer=data__pb2.Player.SerializeToString,
                response_deserializer=data__pb2.Player.FromString,
                )
        self.get_leaderboard = channel.unary_unary(
                '/DATA2410_Portfolio2.Snake/get_leaderboard',
                request_serializer=data__pb2.No_parameter.SerializeToString,
                response_deserializer=data__pb2.Leaderboard.FromString,
                )
        self.get_size = channel.unary_unary(
                '/DATA2410_Portfolio2.Snake/get_size',
                request_serializer=data__pb2.No_parameter.SerializeToString,
                response_deserializer=data__pb2.Position.FromString,
                )
        self.get_information = channel.unary_stream(
                '/DATA2410_Portfolio2.Snake/get_information',
                request_serializer=data__pb2.Player.SerializeToString,
                response_deserializer=data__pb2.Information.FromString,
                )


class SnakeServicer(object):
    """Generate files
    python -m grpc_tools.protoc -I./. --python_out=. --grpc_python_out=. ./data.proto

    """

    def send_high_score(self, request, context):
        """Send to server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_fruit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def send_player(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_leaderboard(self, request, context):
        """Get from server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_size(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_information(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SnakeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'send_high_score': grpc.unary_unary_rpc_method_handler(
                    servicer.send_high_score,
                    request_deserializer=data__pb2.High_score.FromString,
                    response_serializer=data__pb2.Confirmed.SerializeToString,
            ),
            'send_fruit': grpc.unary_unary_rpc_method_handler(
                    servicer.send_fruit,
                    request_deserializer=data__pb2.Position.FromString,
                    response_serializer=data__pb2.Confirmed.SerializeToString,
            ),
            'send_player': grpc.unary_unary_rpc_method_handler(
                    servicer.send_player,
                    request_deserializer=data__pb2.Player.FromString,
                    response_serializer=data__pb2.Player.SerializeToString,
            ),
            'get_leaderboard': grpc.unary_unary_rpc_method_handler(
                    servicer.get_leaderboard,
                    request_deserializer=data__pb2.No_parameter.FromString,
                    response_serializer=data__pb2.Leaderboard.SerializeToString,
            ),
            'get_size': grpc.unary_unary_rpc_method_handler(
                    servicer.get_size,
                    request_deserializer=data__pb2.No_parameter.FromString,
                    response_serializer=data__pb2.Position.SerializeToString,
            ),
            'get_information': grpc.unary_stream_rpc_method_handler(
                    servicer.get_information,
                    request_deserializer=data__pb2.Player.FromString,
                    response_serializer=data__pb2.Information.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DATA2410_Portfolio2.Snake', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Snake(object):
    """Generate files
    python -m grpc_tools.protoc -I./. --python_out=. --grpc_python_out=. ./data.proto

    """

    @staticmethod
    def send_high_score(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DATA2410_Portfolio2.Snake/send_high_score',
            data__pb2.High_score.SerializeToString,
            data__pb2.Confirmed.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def send_fruit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DATA2410_Portfolio2.Snake/send_fruit',
            data__pb2.Position.SerializeToString,
            data__pb2.Confirmed.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def send_player(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DATA2410_Portfolio2.Snake/send_player',
            data__pb2.Player.SerializeToString,
            data__pb2.Player.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_leaderboard(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DATA2410_Portfolio2.Snake/get_leaderboard',
            data__pb2.No_parameter.SerializeToString,
            data__pb2.Leaderboard.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_size(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DATA2410_Portfolio2.Snake/get_size',
            data__pb2.No_parameter.SerializeToString,
            data__pb2.Position.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_information(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/DATA2410_Portfolio2.Snake/get_information',
            data__pb2.Player.SerializeToString,
            data__pb2.Information.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
