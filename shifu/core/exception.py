class BaseApiException(Exception):
    status_code = 500
    message = 'Ops! Something is going wrong, ' \
              'please try again or contact our support team. :)'

    def __init__(self, metadata=None):
        self.metadata = metadata
