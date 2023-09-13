# from tkinter import *
# import random
# import time


# def bros():
#    x = random.choice(['yu.png'])

#    return x


# def img(event):
#    global b1, b2
#    for i in range(18):
#        b1 = PhotoImage(file=(bros()))
#        b2 = PhotoImage(file=(bros()))
#        lab1['image'] = b1
#        lab2['image'] = b2
#        root.update()
#        time.sleep(0.12)


# root = Tk()
# root.geometry('1000x500')
# root.title('My healthy body')
# root.resizable(height=False, width=False)
# root.iconphoto(True, PhotoImage(file=('yu.png')))
# font = PhotoImage(file=('Screenshot_3.png'))
# Label(root, image=font).pack()
# lab1 = Label(root)
# lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
# lab2 = Label(root)

import tkinter as tk
from tkinter import ttk
import sqlite3


class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='city.png')  # ncg6n
        btn_open_dialog = tk.Button(toolbar, text='To see more', command=self.open_dialog,
                                    bg='#d7d8e0', bd=0, compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        self.update_img = tk.PhotoImage(file='runner.png')
        btn_edit_dialog = tk.Button(toolbar, text='Edit', bg='#d7d8e0', bd=0, image=self.update_img,
                                    compound=tk.TOP, command=self.open_update_dialog)
        btn_edit_dialog.pack(side=tk.LEFT)

        self.tree = ttk.Treeview(self, columns=(
            'ID', 'description', 'costs', 'total'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('description', width=365, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        self.tree.column('total', width=100, anchor=tk.CENTER)

        self.tree.heading('ID', text='ID')
        self.tree.heading('description', text='description')
        self.tree.heading('costs', text='costs')
        self.tree.heading('total', text='total')

        self.tree.pack()

    def records(self, description, costs, total):
        self.db.insert_data(description, costs, total)
        self.view_records()

    def update_record(self, description, costs, total):
        self.db.c.execute('''Update finance description=?, costs=?, total=? Where Id=?'''
                          (description, costs, total, self.tree.set(self.tree.selection()[0], '$1')))
        self.db.conn.commit()
        self.view_records()

    def view_records(self):
        self.db.c.execute('''Select * from finance''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row)
         for row in self.db.c.fetchall()]

    def open_dialog(self):
        Child()

    def open_update_dialog(self):
        Update()


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Регистрация пользователя')
        self.geometry('500x270+400+300')
        self.resizable(False, False)

        label_description = tk.Label(self, text='Имя')
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text='Пол')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Ваш рост')
        label_sum.place(x=50, y=110)
        label_description = tk.Label(self, text='Ваш вес')
        label_description.place(x=50, y=140)

        self.entry_description = ttk.Entry(self)
        self.entry_description.place(x=200, y=50)

        self.entry_money = ttk.Entry(self)
        self.entry_money.place(x=200, y=110)

#        self.combobox = ttk.Combobox(
#            self, values=[u'сбросить лишний вес', u'набрать мышечную массу'])
#        self.combobox.current(0)
#        self.combobox.place(x=200, y=50)

        self.combobox = ttk.Combobox(
            self, values=[u'Мужской', u'Женский', u'Другой)))'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        self.combobox = ttk.Combobox(
            self, values=[u'160-164', u'165-169', u'170-174', u'175-179', u'180-184', u'185-189', u'190-194', u'195-199'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=110)

        self.combobox = ttk.Combobox(
            self, values=[u'55-60', u'60-65', u'65-70', u'70-75', u'75-80', u'80-85', u'85-90', u'90-95', u'95-100'])
        self.combobox.current(0)
        self.combobox.place(x=200, y=140)

        btn_cancel = ttk.Button(self, text='Close', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        self.btn_ok = ttk.Button(self, text='add')
        self.btn_ok.place(x=220, y=170)
        self.btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_description.get(),
                                                                       self.entry_money.get(),
                                                                       self.combobox.get()))

        self.grab_set()
        self.focus_set()


class Update(Child):
    def __init__(self):
        super().__init__()
        self.init_edit()
        self.view = app

    def init_edit(self):
        self.title('Update data')
        btn_edit = ttk.Button(self, text='Update data')
        btn_edit.place(x=205, y=175)
        btn_edit.bind('<Button-1>', lambda event: self.view.update_record(self.entry_description.get(),
                                                                          self.combobox.get(),
                                                                          self.entry_money.get()))
        self.btn_ok.destroy()


class DB:
    def __init__(self):
        self.conn = sqlite3.connect('progress')
        self.c = self.conn.cursor()
        self.c.execute(
            'Create  table if not exists finance (id integer primary key, description text, costs text, total real)')
        self.conn.commit()

    def insert_data(self, description, costs, total):
        self.c.execute(
            '''INSERT INTO finance(description, costs, total)VALUES(?,?,?)''', (description, costs, total))
        self.conn.commit()


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("My healthy body")
    root.geometry("1300x800+800+500")
    root.resizable(False, False)
    root.mainloop()
