

import win32.win32gui as win32gui
import pythonwin.win32ui as win32ui
import win32.lib.win32con as win32con
import win32.win32api as win32api
import win32com.client as client

class Tool():
    def __init__(self):
        self.shell = client.Dispatch("WScript.Shell")
    def SetAsForegroundWindow(self, name):
        # 获取后台窗口的句柄，注意后台窗口不能最小化
        hWnd = win32gui.FindWindow(None, name)  # 参数1为类名，参数2为标题

        # 通过pywin32模块下的SetForegroundWindow函数调用时，会出现error: (0, 'SetForegroundWindow', 'No error message is available')
        # 报错，后经网上查询确认，为pywin32模块下的一个小bug，在该函数调用前，需要先发送一个其他键给屏幕，如ALT键 。
        self.shell.SendKeys('%')
        print(hWnd)
        win32gui.SetForegroundWindow(hWnd)



if __name__ == '__main__':
    Tl = Tool()
    Tl.SetAsForegroundWindow("阴阳师-网易游戏")




