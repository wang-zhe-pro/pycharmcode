import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
import time
# About页面
from 工资管理.StartPage import StartPage


class AboutPage:
    def __init__(self, gongzi_window):
        gongzi_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('关于我们')
        self.window.geometry('420x600')  # 这里的乘是小x

        label = tk.Label(self.window, text='员工工资管理系统', width=24, height=1, font=('Verdana', 20))
        label.grid(row=0, column=2, columnspan=3, pady=20)  # pady=20 界面的长度

        label2 = Label(self.window, text='作者：菜鸟集中营', font=('Verdana', 18))
        label2.grid(row=1, column=2, columnspan=3, pady=30)  # pady=30 界面的长度

        btn1 = Button(self.window, text="返回首页", width=8, font=tkFont.Font(size=12), command=self.back)
        btn1.grid(row=2, column=2, columnspan=3, pady=30)
        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口