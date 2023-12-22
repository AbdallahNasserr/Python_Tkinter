from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import askyesno
from PIL import Image, ImageTk
from tkinter import font as tkFont
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import os
os.chdir(r'C:\Users\acer\Downloads\FRAMEs')
# Now you can import the module
def exit():
    answer = askyesno(title='Exit Confirmation',
                      message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
def open_search():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Search_Frame.py')
def open_inventory():
    root.destroy()
    os.system(r"C:\Users\acer\Downloads\FRAMEs\Buy.py")

def open_supplier():
    root.destroy()
    os.startfile("C:/Users/acer/Downloads/FRAMEs/Suppliers_Frame.py")
    
    #/******************************************************************************************************************/


def open_report():
    root.destroy()
    os.system(r"C:\Users\acer\Downloads\FRAMEs\SDOC-7F8FEBE0876144864B10C51C653D7200-12-07-SI.py")


root = Tk()
w = 500
h = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = int((screen_width - w)/2)
y = int((screen_height - h)/2)
root.geometry(f"{w}x{h}+{x}+{y}")
root.attributes('-fullscreen', True)
style = Style()
# Changes will be reflected
# by the movement of mouse.
style.configure('TButton',
                font=('Futura Bk BT', 40, 'bold'),
                borderwidth=10, activebackground='blue',
                background='blue', foreground='black')
style.map('TButton',
          foreground=[('active', '!disabled', 'focus', 'blue')],
          background=[('active', 'blue')])

# style.configure('TButton', background='red', foreground='blue',
#                 width=20, borderwidth=1, focusthickness=3, focuscolor='none')
# style.map('TButton', background=[('active', 'red')])


frame = Frame(root, width=screen_width, height=screen_height)
root.resizable(False, False)

lbl_img = Image.open(r"C:\Users\acer\Downloads\3_3_.png")
resize_image = lbl_img.resize((screen_width, screen_height))
img = ImageTk.PhotoImage(resize_image)
lbl = Label(frame, image=img)
lbl.place(relheight=1, relwidth=1)
frame.place(relheight=1, relwidth=1)
img1 = PhotoImage(file=r"C:\Users\acer\Downloads\transparency.png")
img1 = img1.subsample(7,7)

img22 = PhotoImage(file=r"C:\Users\acer\Downloads\warehouse.png")
img22 = img22.subsample(7,7)

img3 = PhotoImage(file=r"C:\Users\acer\Downloads\inventory.png")
img3 = img3.subsample(7, 7)

img4 = PhotoImage(file=r"C:\Users\acer\Downloads\report (1).png")
img4 = img4.subsample(7,7)

img5 = PhotoImage(file=r"C:\Users\acer\Downloads\remove-button.png")
img5 = img5.subsample(7,7)

btn_search = Button(frame,
                    text="Search  ",
                    compound='right',
                    image=img1,
                    width=20,
                    command=open_search,
                    )

btn_buy = Button(frame,
                 text="Inventory  ",
                 compound='right',
                 image=img22,
                 width=20, command=open_inventory)

btn_supplier = Button(frame,
                      text="Supplier  ",
                      compound='right',
                      image=img3,
                      width=20,
                      command=open_supplier)

btn_report = Button(frame,
                    text="Report  ",
                    compound='right',
                    image=img4,
                    width=20,
                    command=open_report)
btn_exit = tk.Button(frame,
                     text="EXIT",
                     compound='right',
                     image=img5,
                     width=90,
                     font='Arial 18 bold',
                     bd=4,
                     background='#EB5406',
                     activebackground='#2F0909',
                     fg='white',
                     padx=8,
                     command=exit)
lbl = tk.Label(frame,
               text="HOME PAGE",
               width=35,
               bg='#384448',
               bd=5,
               relief='sunken',
               highlightbackground="red",
               font="Arial 40 bold",
               justify='center',
               fg='white',
               anchor='center').place(x=250, y=30)
from tkinter import *
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(20,20)
btn_exit=Button(frame,  text="EXIT", compound='right', image=img2, width=90, command=exit, font='Arial 15 bold', bd=4, background='#EB5406',activebackground='Black',  fg='white', padx=8)
btn_search.place(x=500, y=200)
btn_buy.place(x=500, y=335)
btn_supplier.place(x=500, y=465)
btn_report.place(x=500, y=600)
btn_exit.place(x=15, y=15)
root.mainloop()
