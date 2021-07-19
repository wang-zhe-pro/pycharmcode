#!/usr/bin/python3

import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
import time

from 工资管理.AbouPage import AboutPage
from 工资管理.AdminPage import AdminPage
from 工资管理.EmployPage import EmployPage


class StartPage:
    def __init__(self, gongzi_window):
        gongzi_window.destroy()  # 销毁子界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('工资管理系统')

        self.window.geometry('420x600')  # 这里的乘是小x

        def getTime():
            timeStr = time.strftime('%H:%M:%S')
            Rtime.configure(text=timeStr)
            self.window.after(1000, getTime)

        Rtime = Label(self.window, text='')
        Rtime.pack(pady=25)
        getTime()

        label = Label(self.window, text="员工工资管理系统", width=24, height=1, fg='black', font=("Verdana", 20))
        label.pack(pady=50)  # pady=50 界面的长度
        #row = 0, column = 2, columnspan = 3,

        Button(self.window, text="管理员登陆", font=tkFont.Font(size=16), command=lambda: AdminPage(self.window), width=25,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="员工登陆", font=tkFont.Font(size=16), command=lambda: EmployPage(self.window), width=25,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="用户注册", font=tkFont.Font(size=16), command=lambda: StartPage(self.window), width=25,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text="关于我们", font=tkFont.Font(size=16), command=lambda: AboutPage(self.window), width=25,
               height=2,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        Button(self.window, text='退出系统', height=2, font=tkFont.Font(size=16), width=25, command=self.window.destroy,
               fg='white', bg='gray', activebackground='black', activeforeground='white').pack()
        self.window.mainloop()  # 主消息循环

if __name__ == '__main__':
        # 实例化Application
        window = tk.Tk()
        StartPage(window)