import jwt
import datetime

from django.conf import settings
from ..account_pb2 import UserToken

from account_manager.auth_system.authentication_interfaces import Authentication
from account_manager.auth_system.authentication_exceptions import (
    TokenExpired,
    TokenIsInvalid,
)


class JWTAuth(Authentication):
    SECRET_KEY: str = "i0cwcl!$e54^#0vh6q^)$!+l=_at##a%#0q2&!g$$dau*d2rg8"  # KEY for encoding and decoding tokens
    HASH_FUNCTION: str = "HS256"  # HASH Type

    # Set a TimeDelta to create an expiration time for a token
    # The default time expire is 7 day after creation
    EXPIRE_TIME_AFTER: datetime.datetime = datetime.timedelta(days=7)

    def generate_expire_time() -> datetime.datetime:
        """Generate expiration time for tokens
        based on the EXPIRE_TIME AFTER attribute of the class

        Returns:
           expire_time (datetime.datetime): Expire time as Detetime type
        """

        expire_time = datetime.datetime.utcnow() + JWTAuth.EXPIRE_TIME_AFTER
        return expire_time

    def generate_token(user_id) -> UserToken:
        """Generate JWT token by user id

        Args:
            user_id (int): user id

        Returns:
            token (UserToken): UserToken
        """

        payload = {
            "exp": JWTAuth.generate_expire_time(),  # expire time of token
            "iat": datetime.datetime.utcnow(),  # Generated time of token
            "user_id": str(user_id),
        }

        token = UserToken()
        token.token = jwt.encode(payload, JWTAuth.SECRET_KEY, JWTAuth.HASH_FUNCTION)
        return token

    def decode_token(token: UserToken) -> dict:
        """decoding the JWT token and returning
        the payload inside of the token if the token is correct

        Args:
            token (UserToken): UserToken

        Raises:
            TokenExpired: Toekn is expired
            TokenIsInvalid: The token is invalid

        Returns:
            payload (dict): the payload inside of token
        """

        try:
            payload: dict = jwt.decode(
                token.token, JWTAuth.SECRET_KEY, JWTAuth.HASH_FUNCTION
            )
        except jwt.ExpiredSignatureError:
            raise TokenExpired("The token is expired")
        except Exception as Error:
            raise TokenIsInvalid("The token is invalid try with a new token")

        return payload
