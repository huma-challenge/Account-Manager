from .querys import get_user_by_id, is_token_blacklist
from .authentication_exceptions import TokenIsInvalid
from account_manager.auth_system.authentication_interfaces import Authentication
from account_manager.auth_system.tools import request_have_token


def authentication_by(auth_method: Authentication):
    """authentication request by a Authentication object
    and add a user attribute to self

    Args:
        auth_method (Authentication): Authentication Method like JWTAuth
    """

    def decorator(view):
        def warpper(self, request, context, *args, **kwargs):

            if not request_have_token:
                raise TokenIsInvalid("the Request not contain User Token")
            if is_token_blacklist(request.token.token):
                raise TokenIsInvalid("The token is invalid try with a new token")

            result = auth_method.decode_token(request.token)
            user = get_user_by_id(result.get("user_id", 0))

            # if can't find user by user id
            if not user:
                raise TokenIsInvalid("This Token is Invalid try with a new token")

            self.user = user

            return view(self, request, context, *args, **kwargs)

        return warpper

    return decorator
