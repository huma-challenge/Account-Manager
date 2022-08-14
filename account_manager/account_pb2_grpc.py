# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from account_manager import account_pb2 as account__manager_dot_account__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


class UserManagerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.List = channel.unary_stream(
                '/account.UserManager/List',
                request_serializer=account__manager_dot_account__pb2.UserListRequest.SerializeToString,
                response_deserializer=account__manager_dot_account__pb2.User.FromString,
                )
        self.Create = channel.unary_unary(
                '/account.UserManager/Create',
                request_serializer=account__manager_dot_account__pb2.User.SerializeToString,
                response_deserializer=account__manager_dot_account__pb2.User.FromString,
                )
        self.Retrieve = channel.unary_unary(
                '/account.UserManager/Retrieve',
                request_serializer=account__manager_dot_account__pb2.UserRetrieveRequest.SerializeToString,
                response_deserializer=account__manager_dot_account__pb2.User.FromString,
                )
        self.Update = channel.unary_unary(
                '/account.UserManager/Update',
                request_serializer=account__manager_dot_account__pb2.User.SerializeToString,
                response_deserializer=account__manager_dot_account__pb2.User.FromString,
                )
        self.Destroy = channel.unary_unary(
                '/account.UserManager/Destroy',
                request_serializer=account__manager_dot_account__pb2.User.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Login = channel.unary_unary(
                '/account.UserManager/Login',
                request_serializer=account__manager_dot_account__pb2.UserLoginRequest.SerializeToString,
                response_deserializer=account__manager_dot_account__pb2.UserToken.FromString,
                )


class UserManagerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def List(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Retrieve(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Login(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_UserManagerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'List': grpc.unary_stream_rpc_method_handler(
                    servicer.List,
                    request_deserializer=account__manager_dot_account__pb2.UserListRequest.FromString,
                    response_serializer=account__manager_dot_account__pb2.User.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=account__manager_dot_account__pb2.User.FromString,
                    response_serializer=account__manager_dot_account__pb2.User.SerializeToString,
            ),
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=account__manager_dot_account__pb2.UserRetrieveRequest.FromString,
                    response_serializer=account__manager_dot_account__pb2.User.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=account__manager_dot_account__pb2.User.FromString,
                    response_serializer=account__manager_dot_account__pb2.User.SerializeToString,
            ),
            'Destroy': grpc.unary_unary_rpc_method_handler(
                    servicer.Destroy,
                    request_deserializer=account__manager_dot_account__pb2.User.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Login': grpc.unary_unary_rpc_method_handler(
                    servicer.Login,
                    request_deserializer=account__manager_dot_account__pb2.UserLoginRequest.FromString,
                    response_serializer=account__manager_dot_account__pb2.UserToken.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'account.UserManager', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class UserManager(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/account.UserManager/List',
            account__manager_dot_account__pb2.UserListRequest.SerializeToString,
            account__manager_dot_account__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.UserManager/Create',
            account__manager_dot_account__pb2.User.SerializeToString,
            account__manager_dot_account__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.UserManager/Retrieve',
            account__manager_dot_account__pb2.UserRetrieveRequest.SerializeToString,
            account__manager_dot_account__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.UserManager/Update',
            account__manager_dot_account__pb2.User.SerializeToString,
            account__manager_dot_account__pb2.User.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Destroy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.UserManager/Destroy',
            account__manager_dot_account__pb2.User.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Login(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/account.UserManager/Login',
            account__manager_dot_account__pb2.UserLoginRequest.SerializeToString,
            account__manager_dot_account__pb2.UserToken.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
