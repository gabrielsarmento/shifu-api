from shifu.core.exception import BaseApiException


class UserPayloadValidationException(BaseApiException):
    message = 'User payload validation error.'
    status_code = 400
