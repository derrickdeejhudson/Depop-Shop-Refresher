import pyautogui
from time import sleep

pyautogui.click(1900, 300)

iter = 0
while (iter < 7):
    iter = iter + 1
    # First Page
    pyautogui.middleClick(500, 350)
    pyautogui.middleClick(700, 350)
    pyautogui.middleClick(900, 350)
    pyautogui.middleClick(1100, 350)
    pyautogui.middleClick(1300, 350)
    pyautogui.middleClick(1500, 350)

    pyautogui.middleClick(500, 600)
    pyautogui.middleClick(700, 600)
    pyautogui.middleClick(900, 600)
    pyautogui.middleClick(1100, 600)
    pyautogui.middleClick(1300, 600)
    pyautogui.middleClick(1500, 600)

    pyautogui.middleClick(500, 850)
    pyautogui.middleClick(700, 850)
    pyautogui.middleClick(900, 850)
    pyautogui.middleClick(1100, 850)
    pyautogui.middleClick(1300, 850)
    pyautogui.middleClick(1500, 850)

    sleep(5)
    count = 0
    while (count < 18):
        count = count + 1
        pyautogui.hotkey('ctrlleft', 'tab')
        sleep(1)
        pyautogui.hotkey('ctrlleft', 'f')
        pyautogui.typewrite('edit')
        pyautogui.press('enter')
        pyautogui.press('esc')
        pyautogui.press('enter')

    sleep(4)
    count = 0
    while (count < 18):
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
    pyautogui.press('f5')
    sleep(1)
    pyautogui.click(453, 488)
    pyautogui.middleClick(1900, 300)
    pyautogui.moveTo(1900, 900)
    sleep(2)
    pyautogui.click(1900, 300)
