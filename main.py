from tornado.web import Application
from tornado.ioloop import IOLoop


urls = [

]


def create_app() -> Application:
    api = Application(
        handlers=urls,
        debug=True
    )
    return api


if __name__ == '__main__':
    app = create_app()
    app.listen(8888)
    IOLoop.current().start()
