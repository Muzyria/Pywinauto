from pywinauto import Application


class BasePage:
    NAVIGATION_BUTTON = "TogglePaneButton"
    SETTING_ITEM = "SettingsItem"
    STANDARD_ITEM = "Standard"
    PLUS_BUTTON = "plusButton"
    EQUAL_BUTTON = "equalButton"
    RESULT = "CalculatorResults"

    def __init__(self, app: Application):
        self.app = app
        self.window_app = app["Calculator"]
        self.window_app.wait("ready", timeout=5)

    def open_menu(self):
        self.window_app.child_window(auto_id=self.NAVIGATION_BUTTON).set_focus().click()

    def click_number(self, number: int):
        self.window_app.child_window(auto_id=f"num{number}Button").set_focus().click()

    def click_plus(self):
        self.window_app.child_window(auto_id=self.PLUS_BUTTON).click_input()

    def click_equal(self):
        self.window_app.child_window(auto_id=self.EQUAL_BUTTON).click_input()

    def get_result(self) -> int:
        result = self.window_app.child_window(auto_id=self.RESULT).texts()
        return int(result[0].split(" ")[2])

    def set_numbers(self, number: int):
        self.window_app.child_window(auto_id=self.RESULT).type_keys(number)

    def open_page(self, page_name: str):
        pages = {"standard": self.STANDARD_ITEM,
                 "settings": self.SETTING_ITEM}
        self.window_app.child_window(auto_id=pages[page_name]).set_focus().click_input()
        if page_name == "standard":
            from pages.standard_page import StandardPage
            return StandardPage(self.app)
        elif page_name == "settings":
            from pages.setting_page import SettingPage
            return SettingPage(self.app)

