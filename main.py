
import tkinter as tk
import threading
import time
import ctypes
import inspect
import tkinter.messagebox as messagebox
from ui import Ui_Windows
from tool import Tool



class ProcessFunc():
    def autoJiejiePrcocess(self):
        while 1:
            print("running jiejie")
            time.sleep(1.0)
    def autoYuhunPrcocess(self):
        while 1:
            print("running Yuhun")
            time.sleep(1.0)

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)



class Application():
    def __init__(self, ui):
        self.root = ui
        self.MainWindow = Ui_Windows(self.root)
        self.Proc = ProcessFunc()
        self.btnEvent()
        self.runflag = 0
        self.busyflag = {"Jiejie":0, "Yuhun":0}
        self.Tl = Tool()

    def btnEvent(self):
        btnJiejie = tk.Button(self.root, text='结界', font=('#000000', 12), fg=('#444444'),
                              bd=0.5, command=lambda: self.autoJiejie())
        btnJiejie.place(relx=0.02, rely=0.02, relheight=0.15, relwidth=0.30)



        btnYuHun = tk.Button(self.root, text='御魂', font=('#000000', 12), fg=('#444444'),
                              bd=0.5, command=lambda: self.autoYuhun())
        btnYuHun.place(relx=0.32, rely=0.02, relheight=0.15, relwidth=0.30)

    def autoJiejie(self):
        if(self.runflag == 0):
            self.busyflag["Jiejie"] = 1
            self.runflag = 1
            self.autoJiejiePrcocess = threading.Thread(target=self.Proc.autoJiejiePrcocess)
            self.autoJiejiePrcocess.setDaemon(True)
            self.autoJiejiePrcocess.start()
        elif self.busyflag["Jiejie"] == 1:
            self.runflag = 0
            self.Proc.stop_thread(self.autoJiejiePrcocess)
            print("stop jiejie")
            self.busyflag["Jiejie"] = 0
        else:
            messagebox.showwarning(title='warning!', message = "Busy!")

    def autoYuhun(self):
        if(self.runflag == 0):
            self.busyflag["Yuhun"] = 1
            self.runflag = 1
            self.autoYuhunPrcocess = threading.Thread(target=self.Proc.autoYuhunPrcocess)
            self.autoYuhunPrcocess.setDaemon(True)
            self.autoYuhunPrcocess.start()
        elif self.busyflag["Yuhun"] == 1:
            self.runflag = 0
            self.Proc.stop_thread(self.autoYuhunPrcocess)
            print("stop Yuhun")
            self.busyflag["Yuhun"] = 0
        else:
            messagebox.showwarning(title='warning!', message = "Busy!")










if __name__ == '__main__':
    ui = tk.Tk()
    app = Application(ui)
    ui.mainloop()







