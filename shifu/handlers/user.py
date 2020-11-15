from shifu.core.api import BaseHandler
from shifu.helpers.user import encrypt_password, serialize_user_payload


class UserHandler(BaseHandler):  # noqa
    def post(self):
        user = serialize_user_payload(self.request.body)
        user = encrypt_password(user)

        self.set_status(201)
        self.write(user)
