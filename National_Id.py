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
from tkinter import messagebox
from PIL import Image
import tkinter as tk
from tkinter import ttk as ttk
os.chdir(r'C:\Users\acer\Downloads\FRAMEs')
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
lbl_img=PhotoImage(file=r"C:\Users\acer\Downloads\lago-1257-home-office-36e8-with-air-desk-1593015859.png")
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
user_lbl= Label(frame, text  = "Enter Your National_ID: ", width=25, foreground='#F4F6F7', background='#3A3B3C', font="Arial 25 bold", relief=SUNKEN)
pass_lbl= Label(frame, text  = "Enter Manager Password: ", width=23, foreground='#F4F6F7', background='#3A3B3C', font="Arial 22 bold")
user_entry= PlaceholderEntry(frame,show='*',placeholder='National_ID',placeholdercolor="#C0C0C0",width=25,  font='Arial 25 bold')
pass_entry= PlaceholderEntry(frame,placeholder='Enter Password', show='*', width=22, font='Arial 20 bold')
img = PhotoImage(file=r"C:\Users\acer\Downloads\padlock.png")
img = img.subsample(13,13)
imgg = PhotoImage(file=r"C:\Users\acer\Downloads\undo.png")
imgg = imgg.subsample(13,13)
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(13,13)
def login_fun():
    if user_entry.get()=='30307211401535':
        messagebox.showinfo('Password', "Hi Sir,\nYour Password is: 00000000\nPlease don't forget it again!".title())
    else: messagebox.showerror("Error", "You Aren't Manager!!")
def mang():
    root.destroy()
    os.startfile("C:/Users/acer/Downloads/FRAMEs/Manager.py")
btn_login=Button(frame,  text="Show Password  ", width=18, compound='right', image=img, command=login_fun)
btn_login2=Button(frame,  text="Return ", width=18, compound='right', image=imgg, command=mang)
#print(f"{screen_height} {screen_width}")
def exit():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
lbl=Label(frame,text="password generator".title(),width=35, background='#3A3B3C', font="Arial 40 bold",justify='center', foreground='white',padding=(10, 5), anchor='center').place(x=280,y=70)
user_lbl.place(x=280, y=400)
#pass_lbl.place(x=300, y=450)
user_entry.place(x=780, y=400)
#pass_entry.place(x=700, y=450)
btn_login.place(x=600, y=550)
btn_login2.place(x=600, y=650)
from tkinter import *
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(20,20)
btn_exit=Button(frame,  text="EXIT", compound='right', image=img2, width=90, command=exit, font='Arial 15 bold', bd=4, background='#EB5406',activebackground='Black',  fg='white', padx=8)
btn_exit.place(x=15, y=15)
root.mainloop()