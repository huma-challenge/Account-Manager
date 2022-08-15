from django.contrib.auth import get_user_model

from django_grpc_framework import proto_serializers
from protobufs.account_manager import account_pb2

# Get active user model
User = get_user_model()


class UserProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = User
        proto_class = account_pb2.User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
        ]
