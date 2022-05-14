import pyautogui
from time import sleep

iter = 0
while (iter < 3):
    iter = iter + 1
    # First Page
    pyautogui.middleClick(1800, 1250)
    pyautogui.middleClick(1600, 1250)
    pyautogui.middleClick(1400, 1250)
    pyautogui.middleClick(1200, 1250)
    pyautogui.middleClick(1000, 1250)
    pyautogui.middleClick(800, 1250)

    pyautogui.middleClick(1800, 1050)
    pyautogui.middleClick(1600, 1050)
    pyautogui.middleClick(1400, 1050)
    pyautogui.middleClick(1200, 1050)
    pyautogui.middleClick(1000, 1050)
    pyautogui.middleClick(800, 1050)

    pyautogui.middleClick(1800, 800)
    pyautogui.middleClick(1600, 800)
    pyautogui.middleClick(1400, 800)
    pyautogui.middleClick(1200, 800)
    pyautogui.middleClick(1000, 800)
    pyautogui.middleClick(800, 800)

    pyautogui.middleClick(1800, 600)
    pyautogui.middleClick(1600, 600)
    pyautogui.middleClick(1400, 600)
    pyautogui.middleClick(1200, 600)
    pyautogui.middleClick(1000, 600)
    pyautogui.middleClick(800, 600)

    pyautogui.middleClick(1800, 400)
    pyautogui.middleClick(1600, 400)
    pyautogui.middleClick(1400, 400)
    pyautogui.middleClick(1200, 400)
    pyautogui.middleClick(1000, 400)
    pyautogui.middleClick(800, 400)

    sleep(40)
    count = 0
    while (count < 30):
        count = count + 1
        pyautogui.hotkey('ctrlleft', 'tab')
        sleep(2)
        pyautogui.hotkey('ctrlleft', 'f')
        pyautogui.typewrite('edit')
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('enter')

    sleep(4)
    count = 0
    while (count < 30):
        count = count + 1
        sleep(1)
        pyautogui.hotkey('ctrlleft', 'f')
        pyautogui.typewrite('save changes')
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('enter')
        sleep(2)
        pyautogui.hotkey('ctrlleft', 'w')

    sleep(2)
    pyautogui.press('pageup')
    sleep(1)
