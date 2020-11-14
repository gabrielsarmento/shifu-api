from tornado.web import RequestHandler


class BaseHandler(RequestHandler):  # noqa
    """
    Base handler gonna to be used instead of RequestHandler.
    """

    def write_error(self, status_code, **kwargs):
        error = kwargs.get('exc_info')[1]
        self.set_status(error.status_code)
        self.write({
            'message': error.message,
            'metadata': error.metadata
        })
