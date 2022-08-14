class TokenIsInvalid(Exception):
    """Token Is Invalid"""

    ...


class TokenExpired(Exception):
    "Token is Expired"


class AuthenticationFailed(Exception):
    "Authentication Failed"
