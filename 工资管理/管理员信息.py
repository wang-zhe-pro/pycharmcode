import pymysql
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from tkinter import *  # 图形界面库
import tkinter.messagebox as messagebox  # 弹窗
import time

#管理员信息表界面
class guanliyuanxinxi:
    def __init__(self, gongzi_window):
        gongzi_window.destroy()  # 销毁主界面

        self.window = Tk()  # 初始框的声明
        self.window.title('管理员信息')

        self.frame_left_top = tk.Frame(width=300, height=300)
        self.frame_right_top = tk.Frame(width=180, height=300)
        self.frame_center = tk.Frame(width=950, height=400)
        self.frame_bottom = tk.Frame(width=350, height=50)

        # 定义下方中心列表区域
        self.columns = ("序号", "账号", "级别", "密码")
        self.tree = ttk.Treeview(self.frame_center, show="headings", height=18, columns=self.columns)
        self.vbar = ttk.Scrollbar(self.frame_center, orient=VERTICAL, command=self.tree.yview)
        # 定义树形结构与滚动条
        self.tree.configure(yscrollcommand=self.vbar.set)

        # 表格的标题
        self.tree.column("序号", width=160, anchor='center')  # 表示列,不显示
        self.tree.column("账号", width=160, anchor='center')
        self.tree.column("级别", width=160, anchor='center')
        self.tree.column("密码", width=160, anchor='center')


        # 调用方法获取表格内容插入
        self.tree.grid(row=0, column=0, sticky=NSEW)
        self.vbar.grid(row=0, column=1, sticky=NS)


        self.id = []
        self.num = []
        self.level = []
        self.passwd = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', user='AloginName', password='root', db='SalaryManage')
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin"  # SQL 查询语句
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                self.id.append(row[0])
                self.num.append(row[1])
                self.level.append(row[2])
                self.passwd.append(row[3])
        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        for i in range(min(len(self.id), len(self.num), len(self.level), len(self.passwd))):  # 写入数据
            self.tree.insert('', i, values=(
                self.id[i], self.num[i], self.level[i], self.passwd[i]))

        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))

        # 定义顶部区域
        # 定义左上方区域
        self.top_title = Label(self.frame_left_top, text="管理员信息:", font=('Verdana', 20))
        self.top_title.grid(row=0, column=0, columnspan=2, sticky=NSEW, padx=50, pady=10)

        self.left_top_frame = tk.Frame(self.frame_left_top)
        self.var_id = StringVar()  # 声明序号
        self.var_num = StringVar()  # 声明账号
        self.var_level = StringVar()  # 声明级别
        self.var_passwd = StringVar()  # 声明密码

        # 序号
        self.right_top_id_label = Label(self.frame_left_top, text="序号：", font=('Verdana', 15))
        self.right_top_id_entry = Entry(self.frame_left_top, textvariable=self.var_id,
                                               font=('Verdana', 15))
        self.right_top_id_label.grid(row=1, column=0)  # 位置设置
        self.right_top_id_entry.grid(row=1, column=1)
        # 管理员账号
        self.right_top_num_label = Label(self.frame_left_top, text="账号：", font=('Verdana', 15))
        self.right_top_num_entry = Entry(self.frame_left_top, textvariable=self.var_num,
                                                 font=('Verdana', 15))
        self.right_top_num_label.grid(row=2, column=0)  # 位置设置
        self.right_top_num_entry.grid(row=2, column=1)
        # 管理员级别
        self.right_top_level_label = Label(self.frame_left_top, text="级别：", font=('Verdana', 15))
        self.right_top_level_entry = Entry(self.frame_left_top, textvariable=self.var_level,
                                                font=('Verdana', 15))
        self.right_top_level_label.grid(row=3, column=0)  # 位置设置
        self.right_top_level_entry.grid(row=3, column=1)
        # 管理员密码
        self.right_top_passwd_label = Label(self.frame_left_top, text="密码：", font=('Verdana', 15))
        self.right_top_passwd_entry = Entry(self.frame_left_top, textvariable=self.var_passwd,
                                                font=('Verdana', 15))
        self.right_top_passwd_label.grid(row=4, column=0)  # 位置设置
        self.right_top_passwd_entry.grid(row=4, column=1)



        # 定义右上方区域
        self.right_top_title = Label(self.frame_right_top, text="操作：", font=('Verdana', 20))

        self.tree.bind('<Button-1>', self.click)  # 左键获取位置
        self.right_top_button1 = ttk.Button(self.frame_right_top, text='新建管理员', width=20, command=self.new_row)
        self.right_top_button2 = ttk.Button(self.frame_right_top, text='更新选中管理员信息', width=20,
                                            command=self.updata_row)
        self.right_top_button3 = ttk.Button(self.frame_right_top, text='删除选中员工管理员信息', width=20,
                                            command=self.del_row)
        self.right_top_button4 = ttk.Button(self.frame_right_top, text='查询', width=20,
                                            command=self.select_row)
        self.right_top_button5 = ttk.Button(self.frame_right_top, text='清空', width=20,
                                            command=self.clear)

        # 位置设置
        self.right_top_title.grid(row=0, column=0, pady=10)
        self.right_top_button1.grid(row=1, column=0, padx=20, pady=10)
        self.right_top_button2.grid(row=2, column=0, padx=20, pady=10)
        self.right_top_button3.grid(row=3, column=0, padx=20, pady=10)
        self.right_top_button4.grid(row=4, column=0, padx=20, pady=10)
        # 整体区域定位
        self.frame_left_top.grid(row=0, column=0, padx=2, pady=5)
        self.frame_right_top.grid(row=0, column=1, padx=30, pady=40)
        self.frame_center.grid(row=1, column=0, columnspan=2, padx=4, pady=5)
        self.frame_bottom.grid(row=2, column=0, columnspan=2)

        self.frame_left_top.grid_propagate(0)
        self.frame_right_top.grid_propagate(0)
        self.frame_center.grid_propagate(0)
        self.frame_bottom.grid_propagate(0)

        self.frame_left_top.tkraise()  # 开始显示主菜单
        self.frame_right_top.tkraise()  # 开始显示主菜单
        self.frame_center.tkraise()  # 开始显示主菜单
        self.frame_bottom.tkraise()  # 开始显示主菜单

        self.window.protocol("WM_DELETE_WINDOW", self.back)  # 捕捉右上角关闭点击
        self.window.mainloop()  # 进入消息循环

    def back(self):
        InfoManage(self.window)  # 显示主窗口 销毁本窗口

    def click(self, event):
        self.col = self.tree.identify_column(event.x)  # 列
        self.row = self.tree.identify_row(event.y)  # 行

        print(self.col)
        print(self.row)
        self.row_info = self.tree.item(self.row, "values")
        self.var_id.set(self.row_info[0])
        self.var_num.set(self.row_info[1])
        self.var_level.set(self.row_info[2])
        self.var_passwd.set(self.row_info[3])

        self.right_top_id_entry_entry = Entry(self.frame_left_top, state='disabled',
                                              textvariable=self.var_id,
                                              font=('Verdana', 15))
        print('')

    def tree_sort_column(self, tv, col, reverse):  # Treeview、列名、排列方式
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)  # 排序方式
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            tv.move(k, '', index)
        tv.heading(col, command=lambda: self.tree_sort_column(tv, col, not reverse))  # 重写标题，使之成为再点倒序的标题

        # 新建管理员信息
    def new_row(self):
        print('123')
        print(self.var_id.get() + self.var_num.get())
        print(self.id + self.num)
        cnt = 0
        print(cnt)
        if self.var_id.get() != '':
            # 打开数据库连接
            db = pymysql.connect(host='localhost', user='AloginName', password='root', db='SalaryManage',
                                     autocommit=True)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "select count(1) from admin where AloginName = '%s'" % \
                    (self.var_id.get())  # SQL 插入语句
            try:
                print(sql)
                cursor.execute(sql)  # 执行sql语句
                cnt = cursor.fetchall()[0][0]
                print(cnt)
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '数据库连接失败哦！')
            db.close()  # 关闭数据库连接

        if cnt != 0:
            messagebox.showinfo('警告！', '该序号记录已存在！')
        else:
            if self.var_id.get() != '' and self.var_num.get() != '' and self.var_level.get() != '' and self.var_passwd.get() != '':
                # 打开数据库连接
                db = pymysql.connect(host='localhost', user='AloginName', password='root', db='SalaryManage',autocommit=True)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "INSERT INTO admin (Aid,AloginName,AloginLevel,AloginPwd) \
                                VALUES ('%s','%s','%s','%s')" % \
                       (self.var_id.get(), self.var_num.get(), self.var_level.get(), self.var_passwd.get())  # SQL 插入语句
                try:
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                except:
                    db.rollback()  # 发生错误时回滚
                    # messagebox.showinfo('警告！', '添加失败！')
                db.close()  # 关闭数据库连接

                self.id.append(self.var_id.get())
                self.num.append(self.var_num.get())
                self.level.append(self.var_level.get())
                self.passwd.append(self.var_password.get())

                self.tree.insert('', len(self.id) - 1, values=(
                    self.id[len(self.id) - 1], self.num[len(self.id) - 1],
                    self.level[len(self.id) - 1], self.password[len(self.id) - 1],))
                self.tree.update()
                messagebox.showinfo('提示！', '插入成功！')

            else:
                messagebox.showinfo('警告！', '请填写管理员信息')

#更新选中管理员信息
    def updata_row(self):
        res = messagebox.askyesnocancel('警告！', '是否更新所填数据？')
        if res == True:
            if self.var_id.get() == self.row[1]:  #
                # 打开数据库连接
                db = pymysql.connect(host='localhost', user='AloginName', password='root', db='SalaryManage',
                                 autocommit=True)
                cursor = db.cursor()  # 使用cursor()方法获取操作游标
                sql = "Update admin SET AloginName = '%s', AloginLevel = '%s',AloginPwd = '%s' \
				 WHERE Aid = '%d' " #% (
                    #self.var_name.get(), self.var_way.get(), self.var_count.get(),self.var_reason.get(), self.var_id.get())" # SQL 插入语句
                try:
                    print(sql)
                    cursor.execute(sql)  # 执行sql语句
                    db.commit()  # 提交到数据库执行
                    messagebox.showinfo('提示！', '更新成功！')
                except:
                    db.rollback()  # 发生错误时回滚
                    messagebox.showinfo('警告！', '更新失败，数据库连接失败！')
                db.close()  # 关闭数据库连接

                id_index = self.id.index(self.row_info[0])
                self.num[id_index] = self.num.get()
                self.level[id_index] = self.var_level.get()
                self.passwd[id_index] = self.var_passwd.get()


                self.tree.item(self.tree.selection()[0], values=(
                    self.var_id.get(), self.var_num.get(), self.var_passwd.get(),))
                # 修改对于行信息
            else:
                messagebox.showinfo('警告！', '不能修改管理员记录！')

# 删除选中/单个员工奖惩信息
    def del_row(self):
        res = messagebox.askyesnocancel('警告！', '是否删除所选数据？')
        if res == True:
            print(self.row_info[0])  # 鼠标选中的序号
            print(self.tree.selection()[0])  # 行号
            print(self.tree.get_children())  # 所有行
            # 打开数据库连接
            db = pymysql.connect(host='localhost', user='AloginName', password='root', db='SalaryManage',
                                 autocommit=True)
            cursor = db.cursor()  # 使用cursor()方法获取操作游标
            sql = "DELETE FROM admin WHERE Aid = '%s' " % (self.row_info[0])  # SQL 插入语句
            try:
                cursor.execute(sql)  # 执行sql语句
                db.commit()  # 提交到数据库执行
                messagebox.showinfo('提示！', '删除成功！')
            except:
                db.rollback()  # 发生错误时回滚
                messagebox.showinfo('警告！', '删除失败，数据库连接失败！')
            db.close()  # 关闭数据库连接

            id_index = self.id.index(self.row_info[0])
            print(id_index)
            del self.id[id_index]
            del self.num[_index]
            del self.level[way_index]
            del self.passwd[count_index]


            print(self.id)
            self.tree.delete(self.tree.selection()[0])  # 删除所选行
            print(self.tree.get_children())

#查询
    def select_row(self):
        self.id = []
        self.num = []
        self.level = []
        self.passwd = []
        # 打开数据库连接
        db = pymysql.connect(host='localhost', user='AloginName', password='root', db='SalaryManage',
                                 autocommit=True)
        cursor = db.cursor()  # 使用cursor()方法获取操作游标
        sql = "SELECT * FROM admin "  # SQL 查询语句

        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表

            results = cursor.fetchall()
            print(results)

            for row in results:
                self.id.append(row[0])
                self.num.append(row[1])
                self.level.append(row[2])
                self.passwd.append(row[3])

        except:
            print("Error: unable to fetch data")
            messagebox.showinfo('警告！', '数据库连接失败！')
        db.close()  # 关闭数据库连接

        print("test***********************")
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

        for i in range(min(len(self.id), len(self.num), len(self.level), len(self.passwd))):  # 写入数据
            self.tree.insert('', i, values=(
                self.id[i], self.num[i], self.level[i], self.passwd[i]))
        for col in self.columns:  # 绑定函数，使表头可排序
            self.tree.heading(col, text=col,
                              command=lambda _col=col: self.tree_sort_column(self.tree, _col, False))
    #清空
    def clear(self):
        self.var_id.set('')
        self.var_num.set('')
        self.var_level.set('')
        self.var_passwd.set('')

