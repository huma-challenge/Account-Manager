from .authentication_exceptions import OperatoinFailed, TokenIsInvalid
from account_manager.auth_system.models import BlackListToken

from django.contrib.auth import get_user_model

user_model = get_user_model()


def get_user_by_id(id):
    try:
        return user_model.objects.get(id=id)
    except user_model.DoesNotExist:
        return None


def add_token_to_blacklist(token):
    return BlackListToken.objects.create(token=token.token)


def remove_token_from_blacklist(token):
    raise NotImplemented
