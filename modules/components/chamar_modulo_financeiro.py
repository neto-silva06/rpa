from pywinauto import Desktop
import pyautogui
def ir_para_modulo_financeiro():
        box = pyautogui.locateOnScreen(
        'modules/components/botao.png',
        confidence=0.8
        )

        if box:
                centro = pyautogui.center(box)
                pyautogui.click(centro)


        