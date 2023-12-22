from tkinter import *
import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3
from tkinter import simpledialog
from PIL import Image, ImageTk
import os
os.chdir(r'C:\Users\acer\Downloads\FRAMEs')
# setting up the connection
Mydb = sqlite3.connect("sign_in_db.db")
cursor = Mydb.cursor()
cursor.execute(
    "create table if not exists products (name text, size text, price float(2), qty integer)")
Mydb.commit()
class PlaceholderEntry(ttk.Entry):

    def __init__(self, master, placeholder, textcolor='black', placeholdercolor='grey', **kwargs):
        self.text = placeholder
        self.__has_placeholder = False  # placeholder flag
        self.placeholdercolor = placeholdercolor
        self.textcolor = textcolor

        # style for ttk widget
        self.s = ttk.Style()

        # init entry box
        ttk.Entry.__init__(self, master, style='my.TEntry', **kwargs)
        self.s.configure('my.TEntry', forground=self.placeholdercolor)

        # add placeholder if box empty
        self._add()

        # bindings of the widget
        self.bind('<FocusIn>', self._clear)
        self.bind('<FocusOut>', self._add)
        self.bind_all('<Key>', self._normal)
        self.bind_all('<Button-1>', self._cursor)

    def _clear(self, *args):  # method to remove the placeholder
        if self.get() == self.text and self.__has_placeholder:  # remove placeholder when focus gain
            self.delete(0, tk.END)
            self.s.configure('my.TEntry', foreground='black',
                             font=(0, 0, 'normal'))
            self.__has_placeholder = False  # set flag to false

    def _add(self, *args):  # method to add placeholder
        if self.get() == '' and not self.__has_placeholder:  # if no text add placeholder
            self.s.configure('my.TEntry', foreground=self.placeholdercolor,
                             font=(0, 0, 'bold'))
            self.insert(0, self.text)  # insert placeholder
            self.icursor(0)  # move insertion cursor to start of entrybox
            self.__has_placeholder = True  # set flag to true

    def _normal(self, *args):  # method to set the text to normal properties
        self._add()  # if empty add placeholder
        if self.get() == self.text and self.__has_placeholder:  # clear the placeholder if starts typing
            self.bind('<Key>', self._clear)
            self.icursor(-1)  # keep insertion cursor to the end
        else:
            self.s.configure('my.TEntry', foreground=self.textcolor,
                             font=(0, 0, 'normal'))  # set normal font

    def remove(self, first, last):
        if self.get() != self.text:
            self.delete(first, last)
            self._add()
        elif self.acquire() == self.text and not self.__has_placeholder:
            self.delete(first, last)
            self._add()

    def _cursor(self, *args):  # method to not allow user to move cursor when placeholder exists
        if self.get() == self.text and self.__has_placeholder:
            self.icursor(0)


def update_func(rows):
    treeView.delete(*treeView.get_children())
    for i in rows:
        treeView.insert('', 'end', values=i)


def search_func():
    q2 = q.get()
    query = "SELECT name, size, price, qty FROM products WHERE name like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)


def clear_func():
    query = "SELECT name, size, price, qty FROM products"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)
    ent.remove(0, 30)


# exit to home page function
def exit_func():
    window.destroy()
    import home
    #os.system('home.py')
from tkinter.messagebox import askyesno
def exit_func2():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        window.destroy()
def next_page():
    window.destroy()
    os.startfile(r"C:\Users\acer\Downloads\FRAMEs\Buy.py")
window = Tk()  # the form
q = StringVar()  # made for use in search function
window.attributes('-fullscreen', True)
window.title('Search Page')
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry(f'{screenwidth}x{screenheight}+0+0')
img =PhotoImage(file=r"C:\Users\acer\Downloads\pngtree-store-full-of-in-a-dark-room-picture-image_2654942.png")
label1 = Label(image=img)
label1.image = img
label1.pack()
lbl = tk.Label(window,
               text="product info page".title(),
               font=('Futura Bk BT', 30),
               background='#5C3317',
               foreground='white',
               relief=SUNKEN,
               bd=8,
               width=32)
lbl.place(x=screenwidth/2-350, y=50)

frame1 = Frame(window)
frame1.place(x=screenwidth/2-520, y=screenheight-450)

frame2 = tk.Frame(window, bg='#5C3317')
frame2.place(x=screenwidth/2-350, y=300)


treeView = Treeview(frame1,
                    columns=[1, 2, 3, 4],
                    show="headings",
                    height="15",
                    selectmode='browse')
treeView.pack(side=LEFT)

yscrollbar = ttk.Scrollbar(frame1, orient="vertical", command=treeView.yview)
yscrollbar.pack(side=RIGHT, fill="y")
treeView.configure(yscrollcommand=yscrollbar.set)


treeView.heading(1, text="Name")
treeView.heading(2, text="Size")
treeView.heading(3, text="Price")
treeView.heading(4, text="QTY")

treeView.column(1, width=400, anchor='center')
treeView.column(2, width=200, anchor='center')
treeView.column(3, width=200, anchor='center')
treeView.column(4, width=200, anchor='center')


# traverse data on the tree view section
cursor.execute(
    "select name, size, price, qty FROM products")
rows = cursor.fetchall()
update_func(rows)

style = Style()
style.configure('Treeview',
                font=('Futura Bk BT', 16),
                foreground='white',
                background='#5C3317')
style.configure('Treeview.Heading', font=('Futura Bk BT', 14))


ent = PlaceholderEntry(frame2,
                       placeholder="Enter the product name",
                       placeholdercolor='gray',
                       width=30,
                       textvariable=q,
                       font=('Futura Bk BT', 25))
ent.configure({"background": "black"})
ent.pack(side=tk.LEFT, padx=1)

helv36 = tkFont.Font(family='Futura Bk BT', size=16, weight='bold')

img1 = PhotoImage(file=r"C:\Users\acer\Downloads\transparency.png")
img1 = img1.subsample(20, 20)

img2 = PhotoImage(file=r"C:\Users\acer\Downloads\order.png")
img2 = img2.subsample(18, 18)

img3 = PhotoImage(file=r"C:\Users\acer\Downloads\loading-arrow.png")
img3 = img3.subsample(20, 20)

img4 = PhotoImage(file=r"C:\Users\acer\Downloads\undo.png")
img4 = img4.subsample(20, 20)
Exit = tk.Button(window,
                 text="Return",
                 font=helv36,
                 width=100,
                 image=img4,
                 compound="right",
                 background='#C0C0C0',
                 foreground='black',
                 activebackground='#DC143C',
                 relief=SUNKEN,
                 bd=5,
                 command=exit_func)
Exit.place(x=50, y=20)
img22 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img22 = img2.subsample(13,13)
Exit2 = tk.Button(window,
                 text="EXIT",
                 font=helv36,
                 width=50,
                 image=img22,
                 compound="right",
                 background='red',
                 foreground='white',
                 activebackground='#DC143C',
                 #relief=SUNKEN,
                 command=exit_func2)
Exit2.place(x=750, y=800)

searchButton = tk.Button(frame2,
                         text="Search",
                         font=helv36,
                         width=100,
                         padx=8,
                         background='white',
                         foreground='black',
                        activebackground='black',
                        activeforeground='#EE9A4D',
                         image=img1,
                         compound="right",
                         relief=SUNKEN,
                         bd=5,
                         command=search_func)
searchButton.pack(side=tk.LEFT, padx=5, pady=2)

clearButton = tk.Button(frame2,
                        text='Refresh',
                        font=helv36,
                        width=100,
                        image=img3,
                        compound="right",
                        background='white',
                        foreground='black',
                        activebackground='black',
                        activeforeground='#EE9A4D',
                        relief=SUNKEN,
                        bd=5,
                        command=clear_func)
clearButton.pack(side=tk.LEFT, padx=1)

buy = tk.Button(window,
                text="Buy",
                font="Arial 20 bold",
                width=120,
                image=img2,
                compound="right",
                background='#C0C0C0',
                foreground='black',
                activebackground='green',
                relief=SUNKEN,
                bd=5,
                command=next_page)
buy.place(x=1380, y=20)

window.mainloop()
