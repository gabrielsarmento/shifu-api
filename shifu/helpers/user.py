from bcrypt import gensalt, hashpw
from marshmallow import ValidationError

from shifu.exceptions.users import UserPayloadValidationException
from shifu.handlers.serializers import UserSchema


def encrypt_password(user: dict) -> dict:
    password = user.pop('password')
    hash_password = hashpw(password.encode(), gensalt()).decode()
    user['password'] = hash_password
    return user


def serialize_user_payload(user_json: str) -> dict:
    try:
        user = UserSchema().loads(user_json)
        return user
    except ValidationError as e:
        raise UserPayloadValidationException(metadata=e.messages)
