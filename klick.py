import keyboard, mouse, time

Click = False
def clicker():
    global Click
    Click = not Click

keyboard.add_hotkey('W + S', clicker)

while True:
    if Click:
        mouse.click(button='left')
        time.sleep(0.01)