import win32con, win32ui, win32gui,win32api, win32process
import psutil
import os

class Ergodic():
    def __init__(self):
        self.hwnd_title = dict()
    def get_all_hwnd(self, hwnd, mouse):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            self.hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)+';'+win32gui.GetClassName(hwnd)})

    def get_all_hwnd1(self, hwnd, mouse):
        # if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            self.windows.update({hwnd: win32gui.GetWindowText(hwnd) + ';' + win32gui.GetClassName(hwnd)})


    def get_child_window(self,hwnd):
        self.windows = dict()
        win32gui.EnumChildWindows(hwnd, self.get_all_hwnd1,self.windows)
        print(self.windows)
        return self.windows

    def __call__(self, *args, **kwargs):

        win32gui.EnumWindows(self.get_all_hwnd, 0)

        for h, t in self.hwnd_title.items():
            if t != "":
                print('hwnd:',h,'class type:', t)
        return self.hwnd_title
def get_child_windows(parent):
    '''
    获得parent的所有子窗口句柄
     返回子窗口句柄列表
     '''
    if not parent:
        return
    hwndChildList = []
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd), hwndChildList)
    return hwndChildList
if __name__ == '__main__':
    # win = win32gui.FindWindow('TaskManagerWindow','任务管理器')
    # print(win)
    ergo =Ergodic()
    ergo()
    # ergo.get_child_window(198252)
    # print(get_child_windows(198252))
    # size =win32gui.GetClientRect(1050534)
    # print(size)
