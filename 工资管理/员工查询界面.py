import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
import time

from 工资管理.StartPage import StartPage


class InfoEmploy:
    def __init__(self, gongzi_window):
        gongzi_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('员工查询界面')
        self.window.geometry('420x600')  # 这里的乘是小x


        label = tk.Label(self.window, text='员工选择', width=15, height=1, font=('Verdana', 20))
        label.grid(row=1, column=2, columnspan=3,padx = 80, pady=30)  # pady=20 界面的长度

        btn1 = Button(self.window, text="工资查询", width=15, height=1, relief='raised', font=('Verdana', 20), command=lambda: jiangchengxize(self.window),
                      fg='white', bg='gray', activebackground='black',
                      activeforeground='white')
        btn1.grid(row=4, column=2, columnspan=1,padx = 80,pady=30)

        btn2 = Button(self.window, text="个人信息查看", width=15, height=1,relief='raised',  font=('Verdana', 20), command=lambda: yuangongxinxi(self.window),
                      fg='white', bg='gray', activebackground='black',
                      activeforeground='white')
        btn2.grid(row=2, column=2, columnspan=1,padx = 80, pady=30)


        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        StartPage(self.window)  # 显示主窗口 销毁本窗口

