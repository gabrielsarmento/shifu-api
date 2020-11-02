from marshmallow import ValidationError
from tornado.web import RequestHandler

from shifu.handlers.serializers import UserSchema
from shifu.helpers.user import encrypt_password


class UserHandler(RequestHandler):  # noqa
    def post(self):
        try:
            user = UserSchema().loads(self.request.body)
            user = encrypt_password(user)
            self.set_status(201)
            self.write(user)
        except ValidationError as e:
            self.set_status(400)
            self.write({'error': e.messages})
