from django.contrib.auth import get_user_model

from django_grpc_framework import generics

from account_manager.account.serializers import UserProtoSerializer

from account_manager.auth_system.authentication import JWTAuth
from account_manager.auth_system.decorators import authentication_by


# Get active user model
user_model = get_user_model()


class UserService(generics.ModelService):
    queryset = user_model.objects.all()
    serializer_class = UserProtoSerializer

    @authentication_by(JWTAuth)
    def List(self, request, context):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # This RPC is a Stream RPC so we shold pass data as yield insted of return
        for message in serializer.message:
            yield message

    @authentication_by(JWTAuth)
    def Retrieve(self, request, context):
        instance = self.user
        serializer = self.get_serializer(instance)
        return serializer.message

    @authentication_by(JWTAuth)
    def Update(self, request, context):
        instance = self.user
        serializer = self.get_serializer(instance, message=request.user, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.message

