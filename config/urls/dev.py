import imp
from config.urls.base import *

from account_manager.api.views import UserService
from protobufs.account_manager import account_pb2_grpc

# Active all servicers on the server [channel]
def grpc_handlers(server):

    # Active UserService as a servicer for UserManager service
    account_pb2_grpc.add_UserManagerServicer_to_server(
        UserService.as_servicer(), server
    )
