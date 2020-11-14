from marshmallow import ValidationError

from shifu.core.api import BaseHandler
from shifu.exceptions.users import UserPayloadValidationException
from shifu.handlers.serializers import UserSchema
from shifu.helpers.user import encrypt_password


class UserHandler(BaseHandler):  # noqa
    def post(self):
        try:
            user = UserSchema().loads(self.request.body)
            user = encrypt_password(user)
        except ValidationError as e:
            raise UserPayloadValidationException(metadata=e.messages)

        self.set_status(201)
        self.write(user)
