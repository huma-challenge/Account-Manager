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

    @authentication_by(JWTAuth)
    def Destroy(self, request, context):
        user = self.user
        user.delete()
        return empty_pb2.Empty()

    def Login(self, request: UserLoginRequest, context):
        try:
            user = user_model.objects.get(username=request.username)

            # Raising an Error"DoesNotExist" When Password not matched
            if not user.check_password(request.password):
                raise user_model.DoesNotExist

        except user_model.DoesNotExist:
            raise AuthenticationFailed(
                "Can't find any user with this username and password"
            )
        except Exception as Error:
            raise AuthenticationFailed(Error)

        token = JWTAuth.generate_token(user.id)
        user = UserProtoSerializer(user)

        response = UserLoginResponse()
        response.token.CopyFrom(token)
        response.user.CopyFrom(user.message)

        return response

