class TokenIsInvalid(Exception):
    """Token Is Invalid"""

    ...


class TokenExpired(Exception):
    "Token is Expired"
    ...


class OperatoinFailed(Exception):
    "The Operation Failed"


class AuthenticationFailed(Exception):
    "Authentication Failed"
    ...
