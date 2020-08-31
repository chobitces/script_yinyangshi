import tkinter as tk

class Ui_Windows():
    def __init__(self, ui):
        self.root = ui
        self.setupUi()

    def setupUi(self):
        self.root.title("阴阳师脚本")
        width = 400
        height = 400


        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.root.resizable(width=True, height=True)





if __name__ == '__main__':
    ui = tk.Tk()
    app = Ui_Windows(ui)
    ui.mainloop()

