from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import askyesno
from PIL import Image
import os
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
               ('calibri', 40, 'bold'),  borderwidth = 10, activebackground='black', background='red')
# Changes will be reflected
# by the movement of mouse.
style.map('TButton', foreground = [('active', '!disabled', 'focus', 'blue')],
                     background = [('active', 'Black')])


# *******************************************************
# *******************************************************
frame2 = Frame(root, width=screen_width, height=screen_height)
root.resizable(False, False) 
lbl_img=PhotoImage(file=r"C:\Users\acer\Downloads\pngtree-store-full-of-in-a-dark-room-picture-image_2654942.png")
lbl=Label(frame2, image= lbl_img)
lbl.place(relheight=1,relwidth=1)
frame2.place(relheight=1,relwidth=1)
#root.configure(bg="black")
#root.attributes("-fullscreen", True)# Set fullscreen
#Label1=Label(root,text="fgg").pack()
user_lbl= Label(frame2, text  = "Enter Username: ", width=18, foreground='#F4F6F7', background="#951D11", font="Arial 22 bold")
pass_lbl= Label(frame2, text  = "Enter Password: ", width=18, foreground='#F4F6F7', background="#951D11", font="Arial 22 bold")
user_entry= Entry(frame2, width=22, font='Arial 20 bold', background="#C0392B", foreground="#C0392B")
pass_entry= Entry(frame2, show='*', width=22, font='Arial 20 bold', background="#C0392B", foreground="#C0392B")
img = PhotoImage(file=r"C:\Users\acer\Downloads\add-user_609195.png")
img = img.subsample(9,9)
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\search-profile.png")
img2 = img2.subsample(9,9)
img3 = PhotoImage(file=r"C:\Users\acer\Downloads\garbage.png")
img3 = img3.subsample(9,9)
img4 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
def add():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Add_Supplier.py')
btn_add=Button(frame2,  text="ADD ".title(), compound='right', image=img, width=20, command=add)

def open_search():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Search_Supplier_Frame.py')
def open_delete():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Delete_Supplier.py')
btn_search=Button(frame2,  text="SEARCH".title(), compound='right', image=img2, width=20, command=open_search)
btn_delete=Button(frame2,  text="DELETE".title(), compound='right', image=img3, width=20, command=open_delete)
#print(f"{screen_height} {screen_width}")
def exit():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
def open_home():
    root.destroy()
    import home
#user_lbl.place(x=400, y=400)
#pass_lbl.place(x=400, y=450)
#user_entry.place(x=700, y=400)
#pass_entry.place(x=700, y=450)
btn_add.place(x=500, y=300)
btn_search.place(x=500, y=430)
btn_delete.place(x=500, y=550)
from tkinter import *
img4 = img4.subsample(20,20)
img5 = PhotoImage(file=r"C:\Users\acer\Downloads\home (1).png")
img5 = img5.subsample(20,20)
btn_home=Button(frame2,  text="HOME", compound='right', image=img5, width=120, command=open_home, font='Arial 15 bold', bd=4, background='brown',activebackground='gray',  fg='white', padx=8)
btn_exit=Button(frame2,  text="EXIT", compound='right', image=img4, width=90, command=exit, font='Arial 15 bold', bd=4, background='#EB5406',activebackground='Black',  fg='white', padx=8)
lbl=Label(frame2,text="Suppliers Home",width=35, bg='#5C3317',  bd=5, relief='sunken',highlightbackground="red", font="Arial 40 bold",justify='center', fg='white',anchor='center').place(x=250,y=70)
btn_exit.place(x=15, y=15)
btn_home.place(x=730, y=750)
root.mainloop()