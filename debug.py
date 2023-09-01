from pywinauto import Application
import time


NAVIGATION_BUTTON = "TogglePaneButton"
SETTING_ITEM = "SettingsItem"
STANDARD_ITEM = "Standard"
PLUS_BUTTON = "plusButton"
EQUAL_BUTTON = "equalButton"
RESULT = "CalculatorResults"

# app = Application(backend="uia").start(fr"calc.exe", timeout=10)
app = Application(backend="uia").start(fr"calc.exe", timeout=10)


app.connect(best_match="Calculator", timeout=5)

time.sleep(2)

# numbut = app["Calculator"].child_window(auto_id="num5Button")
app["Calculator"].child_window(auto_id=NAVIGATION_BUTTON).set_focus().click()
app["Calculator"].child_window(auto_id=SETTING_ITEM).set_focus().click_input()
# numbut.draw_outline()




# print(numbut.print_control_identifiers())




time.sleep(5)

app.kill(soft=True)
