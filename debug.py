from pywinauto import Application
import time

# app = Application(backend="uia").start(fr"calc.exe", timeout=10)
app = Application(backend="win32").start(fr"calc.exe", timeout=10)


app.connect(best_match="Calculator", timeout=5)

time.sleep(2)

# numbut = app["Calculator"].child_window(auto_id="num5Button")
numbut = app.top_window().child_window(Name="Calculator")

numbut.draw_outline()


time.sleep(5)

app.kill(soft=True)
