import pyautogui
from datetime import datetime


def screenshot_erro(nome):

    data = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    caminho = f"C:\RPA\logs\{nome}_{data}.png"

    pyautogui.screenshot(caminho)