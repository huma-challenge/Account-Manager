from abc import ABC, abstractclassmethod, abstractmethod, abstractstaticmethod


class Authentication(ABC):
    @abstractstaticmethod
    def generate_token(user_id):
        ...

    @abstractstaticmethod
    def decode_token(token):
        ...
