from protobufs.account_manager.account_pb2 import UserToken


def request_have(request, attr_name: str):
    """check a request have a specific attribute

    Args:
        request (Any): A Request obj
        attr_name (str): attribute name

    Returns:
        bool : status check
    """

    try:
        getattr(request, str(attr_name))
        return True
    except AttributeError:
        return False


def request_have_token(request):
    """Check Request have UserToken

    Args:
        request (Any): Reqeust obj

    Returns:
        bool : status of check
    """
    return isinstance(request_have(request, "token"), UserToken)
