from pywinauto import Application


class BasePage:
    def __init__(self, app: Application):
        self.app = app
        self.window_app = app["Calculator"]
        self.window_app.wait("ready", timeout=5)
