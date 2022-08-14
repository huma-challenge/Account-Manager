from django.contrib.auth import get_user_model

from django_grpc_framework import generics

from account_manager.account.serializers import UserProtoSerializer


# Get active user model
User = get_user_model()


class UserService(generics.ModelService):
    queryset = User.objects.all()
    serializer_class = UserProtoSerializer

    def List(self, request, context):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        # This RPC is a Stream RPC so we shold pass data as yield insted of returne
        for message in serializer.message:
            yield message

    def Retrieve(self, request, context):
        print(request)
        return super().Retrieve(request, context)
