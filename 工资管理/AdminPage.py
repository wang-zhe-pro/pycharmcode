#!/usr/bin/python3

import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
import time
class AdminPage:
    def __init__(self, gongzi_window):
        gongzi_window.destroy()  # 销毁主界面

        self.window = tk.Tk()  # 初始框的声明
        self.window.title('管理员登陆页面')
        self.window.geometry('420x600')  # 这里的乘是小x

        label = Label(self.window, text="管理员登陆", width=24, height=1, fg='black', font=("Verdana", 20))
        label.grid(row=0, column=2, columnspan=3, pady=50)  # pady=50 界面的长度
        label2 = Label(self.window, text='管理员账号：', font=tkFont.Font(size=18))
        label2.grid(row=1, column=0, columnspan=3, padx=15, pady=20)
        self.AName = tk.Entry(self.window, width=15, font=tkFont.Font(size=18), bg='Ivory')
        self.AName.grid(row=1, column=4, columnspan=3, padx=15, pady=20)

        label3 = Label(self.window, text='管理员密码：', font=tkFont.Font(size=18))
        label3.grid(row=2, column=0, columnspan=3, padx=15, pady=20)
        self.APwd = tk.Entry(self.window, width=15, font=tkFont.Font(size=18), bg='Ivory', show='*')
        self.APwd.grid(row=2, column=4, columnspan=3, padx=15, pady=20)

        btn1 = Button(self.window, text="登陆", width=20, font=tkFont.Font(size=15), command=self.login)
        btn1.grid(row=3, column=2, columnspan=3, padx=25, pady=20)

        btn2 = Button(self.window, text="返回首页", width=20, font=tkFont.Font(size=15), command=self.back)
        btn2.grid(row=4, column=2, columnspan=3, padx=25, pady=20)

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def login(self):
        name = str(self.AName.get())
        pas = str(self.APwd.get())
        print(name)
        print(pas)
        db = pymysql.connect(host='localhost', user='AloginName', password='root', db='SalaryManage', autocommit=True)
        # # 使用cursor()方法获取操作游标
        cursor = db.cursor()

        sql = "select * from admin"

        # 执行SQL语句
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            print(row[1], row[3])
        # global flag
        f = 0
        for row in results:
            if name == row[1]:
                f = 1
                if pas == row[3]:
                    InfoManage(self.window)  # 进入管理员操作界面
                else:
                    messagebox.showinfo("警告", "密码错误!")
                    self.APwd.delete(0, END)
        if f == 0:
            messagebox.showinfo("警告", "用户名错误或不存在!")
            self.AName.delete(0, END)
            self.APwd.delete(0, END)

        db.close()

    def back(self):
        StartPage(self.window)  # 回到主窗口
