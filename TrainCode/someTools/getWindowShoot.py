import time

import cv2
import pyautogui
import numpy as np
import win32api, win32con, win32gui, win32ui
from pathlib import Path
import yaml

# CONFIG_PATH = Path(__file__).parent.parent.joinpath("config.yaml")
# assert CONFIG_PATH.is_file()
#
#
# with open(CONFIG_PATH, encoding='utf-8') as f:
#     result = yaml.safe_load(f)
#     DEFAULT_MONITOR_WIDTH = result.get("windows").get("monitor_width")
#     DEFAULT_MONITOR_HEIGHT = result.get("windows").get("monitor_height")
#     WINDOW_NAME = result.get("game").get("window_name")


# def cap(region=None):
#     img = pyautogui.screenshot(region=region) if region else pyautogui.screenshot()
#     return cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)


def cap(region=None):
    if region is not None:
        left, top, w, h = region
        # w = x2 - left + 1
        # h = y2 - top + 1
    # else:
    #     w = DEFAULT_MONITOR_WIDTH  # set this
    #     h = DEFAULT_MONITOR_HEIGHT  # set this
    #     left = 0
    #     top = 0

    # hwnd = win32gui.FindWindow(None, WINDOW_NAME)
    hwnd = win32gui.GetDesktopWindow()
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()

    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)

    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (w, h), dcObj, (left, top), win32con.SRCCOPY)
    # dataBitMap.SaveBitmapFile(cDC, bmpfilenamename)
    signedIntsArray = dataBitMap.GetBitmapBits(True)
    img = np.frombuffer(signedIntsArray, dtype="uint8")
    img.shape = (h, w, 4)
    # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2BGR)
    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())

    return img
