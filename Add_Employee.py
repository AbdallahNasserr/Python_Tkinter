from tkinter import messagebox
from tkinter import *
import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
import sys
import os
from tkinter.ttk import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import Image
import tkinter as tk
from tkinter import ttk as ttk
import  sqlite3
os.chdir(r'C:\Users\acer\Downloads\FRAMEs')
#print(os.getcwd())
db = sqlite3.connect("sign_in_db.db")
cr = db.cursor()
cr.execute("create table if not exists sign_in(Username text , Password integer)")
root = Tk()
w= 500
h=300
padx=10
pady=10
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width -  w)/2)
y = int((screen_height - h)/2)
root.geometry(f"{w}x{h}+{x}+{y}")
root.attributes('-fullscreen', True)
style = Style()
style.configure('TButton', font =
               ('calibri', 20, 'bold'),  borderwidth = 8, activebackground='black', background='red')
# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'focus', 'blue')],
                     background = [('active', 'Black')])
# *******************************************************
# *******************************************************
frame = Frame(root, width=screen_width, height=screen_height) 
lbl_img=PhotoImage(file=r"C:\Users\acer\Downloads\Screenshot 2023-12-05 034838.png")
lbl=Label(frame, image= lbl_img)
lbl.place(relheight=1,relwidth=1)
frame.place(relheight=1,relwidth=1)
#root.configure(bg="black")
#root.attributes("-fullscreen", True)# Set fullscreen
#Label1=Label(root,text="fgg").pack()
class PlaceholderEntry(ttk.Entry):
    '''
    Custom modern Placeholder Entry box, takes positional argument master and placeholder along with\n
    textcolor(default being black) and placeholdercolor(default being grey).\n
    Use acquire() for getting output from entry widget\n
    Use shove() for inserting into entry widget\n
    Use remove() for deleting from entry widget\n
    Use length() for getting the length of text in the widget\n
    BUG 1: Possible bugs with binding to this class\n
    BUG 2: Anomalous behaviour with config or configure method
    '''
    def __init__(self, master, placeholder,textcolor='black',placeholdercolor='grey', **kwargs):
        self.text = placeholder
        self.__has_placeholder = False # placeholder flag
        self.placeholdercolor = placeholdercolor
        self.textcolor = textcolor

        # style for ttk widget
        self.s = ttk.Style()

        # init entry box
        ttk.Entry.__init__(self, master, style='my.TEntry', **kwargs)
        self.s.configure('my.TEntry',forground=self.placeholdercolor)

        # add placeholder if box empty
        self._add()

        # bindings of the widget
        self.bind('<FocusIn>', self._clear)
        self.bind('<FocusOut>', self._add)
        self.bind_all('<Key>', self._normal)
        self.bind_all('<Button-1>', self._cursor)

    def _clear(self, *args): # method to remove the placeholder
        if self.get() == self.text and self.__has_placeholder:  # remove placeholder when focus gain
            self.delete(0, tk.END)
            self.s.configure('my.TEntry', foreground='black',
                             font=(0, 0, 'normal'))
            self.__has_placeholder = False #set flag to false

    def _add(self, *args): # method to add placeholder
        if self.get() == '' and not self.__has_placeholder:  # if no text add placeholder
            self.s.configure('my.TEntry', foreground=self.placeholdercolor,
                             font=(0, 0, 'bold'))
            self.insert(0, self.text)  # insert placeholder
            self.icursor(0)  # move insertion cursor to start of entrybox
            self.__has_placeholder = True #set flag to true

    def _normal(self, *args): #method to set the text to normal properties
        self._add()  # if empty add placeholder
        if self.get() == self.text and self.__has_placeholder:  # clear the placeholder if starts typing
            self.bind('<Key>', self._clear)
            self.icursor(-1)  # keep insertion cursor to the end
        else:
            self.s.configure('my.TEntry', foreground=self.textcolor,
                         font=(0, 0, 'normal'))  # set normal font

    def acquire(self):  
        """Custom method to get the text"""
        if self.get() == self.text and self.__has_placeholder:
            return 'None'
        else:
            return self.get()

    def shove(self, index, string):  
        """Custom method to insert text into entry"""
        self._clear()
        self.insert(index, string)

    def remove(self, first, last):  
        """Custom method to remove text from entry"""
        if self.get() != self.text:
            self.delete(first, last)
            self._add()
        elif self.acquire() == self.text and not self.__has_placeholder:
            self.delete(first, last)
            self._add()

    def length(self):
        """Custom method to get the length of text in the entry widget"""
        if self.get() == self.text and self.__has_placeholder:
            return 0
        else:
            return len(self.get())

    def _cursor(self, *args):  # method to not allow user to move cursor when placeholder exists
        if self.get() == self.text and self.__has_placeholder:
            self.icursor(0)
# ##########################################
supp_name = Label(frame, text  = "Enter Employee Username: ", width=25, foreground='#F4F6F7', background='#616D7E',  font="Arial 25 bold",borderwidth=1)
supp_num= Label(frame, text  = "Enter Employee Password: ", width=25, foreground='#F4F6F7', background='#616D7E', font="Arial 25 bold")
prod_name= Label(frame, text  = "Enter Product Name: ", width=22, foreground='#F4F6F7', background='#5C3317',  font="Arial 25 bold",borderwidth=1)
prod_prc= Label(frame, text  = "Enter Product Price: ", width=22, foreground='#F4F6F7', background='#5C3317', font="Arial 25 bold")
supp_name_entry= PlaceholderEntry(frame,placeholder='Username',  width=28, font='Arial 22 italic')
supp_num_entry= PlaceholderEntry(frame,placeholder='Password',  width=28, font='Arial 22 italic')
prod_name_entry= PlaceholderEntry(frame,placeholder='Enter Product Name:',  width=25, font='Arial 20 italic')
prod_prc_entry= PlaceholderEntry(frame,placeholder='Enter Product Price:',  width=25, font='Arial 20 italic')
img = PhotoImage(file=r"C:\Users\acer\Downloads\user (1).png")
img = img.subsample(9,9)
def is_string(s):
    return isinstance(s, str)
    #import home
def login_fun():
    cr = db.cursor()
    if(is_string(supp_name_entry.get())) and len(supp_num_entry.get())>=8:
        cr.execute(f"insert into sign_in(Username , Password ) values('{supp_name_entry.get()}',{int(supp_num_entry.get())})")
        db.commit()
        messagebox.showinfo('Added',"Added Succefully!")
    else: 
        messagebox.showwarning('Not Valid',"Name should be only characters and password length more than seven")
btn_add=Button(frame,  text="ADD  ", compound='right', image=img, command=login_fun, width=15)
#print(f"{screen_height} {screen_width}")
def exit():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
from tkinter import *
lbl=Label(frame,text="Add Employee",width=35  ,bg='#616D7E',
               bd=5,
               relief='sunken',
               highlightbackground="red",
               font="Arial 40 bold",
               justify='center',
               fg='white',
               anchor='center').place(x=200,y=70)
from tkinter.ttk import *
supp_name.place(x=250, y=350)
supp_num.place(x=250, y=500)
#prod_name.place(x=350, y=450)
#prod_prc.place(x=350, y=550)
supp_name_entry.place(x=730, y=355)
supp_num_entry.place(x=730, y=500)
#prod_name_entry.place(x=800, y=450)
#prod_prc_entry.place(x=800, y=550)
btn_add.place(x=650, y=650)
img5 = PhotoImage(file=r"C:\Users\acer\Downloads\undo.png")
img5=img5.subsample(20,20)
def open_home():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Manager.py')
btn_home=Button(frame,  text="Return", compound='right', image=img5, command=open_home).place(x=690,y=750)
from tkinter import *
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(20,20)
btn_exit=Button(frame,  text="EXIT", compound='right', image=img2, width=90, command=exit, font='Arial 15 bold', bd=4, background='#EB5406',activebackground='Black',  fg='white', padx=8)
btn_exit.place(x=15, y=15)
db.commit()
root.mainloop()