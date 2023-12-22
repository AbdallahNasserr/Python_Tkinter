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
from tkinter import *
import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import Image
import tkinter as tk
from tkinter import ttk as ttk
import os
root=Tk()
root.title("reporting")
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.attributes('-fullscreen', TRUE)
img =PhotoImage(file=r"C:\Users\acer\Downloads\new.png")
label1 = Label(image=img)
#label1.pack()
import sqlite3
os.chdir(r'C:\Users\acer\Downloads\FRAMEs')
#print(os.getcwd())
datab=sqlite3.connect("mashroo3.db")
cr=datab.cursor()
cr.execute("create table if not exists purchases (product_name,amount , price ,cost , day)")
#cr.execute("insert into purchases (product_name,amount,price,day)values ('kargo',2,550,'15-12-2022')")
datab.commit()
frame=Frame(root,width=screen_width, height=screen_height) 
def search():
    entry=text.get()
    entry2=text2.get()
    temp=''
    if entry2 == temp :
        cr.execute(f"select * from purchases where day='{entry}'")
    else :
        cr.execute(f"select * from purchases where day>='{entry}' AND day<='{entry2}'")
    r=cr.fetchall()
    lbl_product=tk.Label(root,text=" Product ",font='time 12 bold',fg='blue')
    lbl_amount=tk.Label(root,text=" Amount ",font='time 12 bold',fg='blue')
    lbl_day=tk.Label(root,text=" Day ",font='time 12 bold',fg='blue')
    lbl_price=tk.Label(root,text=" Price ",font='time 12 bold',fg='blue')
    lbl_cost=tk.Label(root,text=" Cost ",font='time 12 bold',fg='blue')
    ##########
    lbl_product.grid(row=0,column=0)
    lbl_amount.grid(row=0,column=1)
    lbl_price.grid(row=0,column=2)
    lbl_cost.grid(row=0,column=3)
    lbl_day.grid(row=0,column=4)
    num=2
    for i in r:
        product=tk.Label(root,text=i[0],font='time 12 bold',fg='blue')
        product.grid(row=num,column=0,padx=10,pady=10)
        
        amount=tk.Label(root,text=i[1],font='time 12 bold',fg='blue')
        amount.grid(row=num,column=1,padx=10,pady=10)
        
        day=tk.Label(root,text=i[2],font='time 12 bold',fg='blue')
        day.grid(row=num,column=2,padx=10,pady=10)
        
        price=tk.Label(root,text=i[3],font='time 12 bold',fg='blue')
        price.grid(row=num,column=3,padx=10,pady=10)
        
        cost=tk.Label(root,text=i[4],font='time 12 bold',fg='blue')
        cost.grid(row=num,column=4,padx=10,pady=10)
        num+=1
    label_total=tk.Label(root,text="Total income ",font='time 12 bold',fg='blue')    
    label_total.place(x=550,y=550) 
    if entry2 == temp :
        cr.execute(f"select sum(cost) from purchases where day='{entry}'")
       
    else :
        cr.execute(f"select sum(cost) from purchases where day>='{entry}' AND day<='{entry2}'")
    #cr.execute("select sum(cost)from purchases where day >='{entry}' AND day <='{entry2}'")
    f=cr.fetchall()
    labl_cost =tk.Label(root,text=f,font='time 12 bold',fg='blue')
    labl_cost.place(x=550,y=600)
labl_txt=tk.Label(root,text="ENTER THE DATE",font=('helvatic',20,'bold'),bg='azure3')
lbl_txt_from=tk.Label(root,text="FROM",font=('helvatic',20),bg='azure3')
lbl_txt_to=tk.Label(root,text="TO",font=('helvatic',20),bg='azure3')
text=tk.Entry(root)
text2=tk.Entry(root)
btn=tk.Button(root,text="SEARCH",command=search,font=("Arial Bold", 15), fg = "green",bg='azure3')
#btn_exit=tk.Button(root,text="EXIT",font=("Arial Bold", 15), fg = "red" ,bg='azure3')

labl_txt.place(x=900,y=200)
lbl_txt_from.place(x=900,y=250)
text.place(x=900,y=300)
lbl_txt_to.place(x=900,y=350)
text2.place(x=900,y=400)
btn.place(x=900,y=450)
#btn_exit.place(x=1100,y=550)
def exit_func2():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
Exit2 = tk.Button(root,
                 text="EXIT",
                 font="Arial 13 bold",
                 width=7,
                 #image=img22,
                 compound="right",
                 background='red',
                 foreground='white',
                 activebackground='#DC143C',
                 relief=SUNKEN,
                 command=exit_func2)
def exit_func():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/home.py')
    #os.system('home.py')
Exit = tk.Button(root,
                 text="Home",
                 font="Arial 15 bold",
                 width=9,
                 #image=img22,
                 compound="right",
                 background='gray',
                 foreground='white',
                 activebackground='green',
                 relief=SUNKEN,
                 command=exit_func)
Exit2.place(x=750, y=800)
Exit.place(x=730, y=700)
cr.execute("select * from purchases where day ='11-12-2022'")
#btn.pack()
#cr.execute("insert into purchases (product_name,amount,price,day)values ('kargo',2,550,'10-12-2022')")
#cr.execute("update purchases set cost=amount*price")
#cr.execute("select * from purchases")
datab.commit()
root.mainloop()
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
db = sqlite3.connect("sign_in_db.db")
cursor = db.cursor()
db.commit()
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
    query = "SELECT pname, pprice,sname,snumber FROM suppliers WHERE pname like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)
def clear_func():
    query = "SELECT pname, pprice,sname,snumber FROM suppliers"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)
    ent.remove(0, 30)
# exit to home page function
def exit_func():
    window.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Suppliers_Frame.py')
    #os.system('home.py')
from tkinter.messagebox import askyesno
def exit_func2():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        window.destroy()
def next_page():
    pass
window = Tk()  # the form
q = StringVar()  # made for use in search function
window.attributes('-fullscreen', True)
window.title('Search Page')
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry(f'{screenwidth}x{screenheight}+0+0')
img =PhotoImage(file=r"C:\Users\acer\Downloads\new.png")
label1 = Label(image=img)
label1.image = img
label1.pack()
lbl = tk.Label(window,
               text="Find Best Supplier".title(),
               font=('Futura Bk BT', 35,'bold'),
               background='#3A3B3C',
               foreground='white',
               relief=SUNKEN,
               bd=8,
               pady=8,
               width=32)
lbl.place(x=screenwidth/2-450, y=50)

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
from tkinter.ttk import *
# style = Style()
# style.configure("Treeview.Heading", font=(None, 50))
treeView.heading(1, text="Product Name")
treeView.heading(2, text="Product Price")
treeView.heading(3, text="Supplier Name")
treeView.heading(4, text="Phone Number")

treeView.column(1, width=300, anchor='center')
treeView.column(2, width=200, anchor='center')
treeView.column(3, width=300, anchor='center')
treeView.column(4, width=300, anchor='center')
# traverse data on the tree view section
cursor.execute("select pname, pprice, sname,snumber FROM suppliers")
rows = cursor.fetchall()
update_func(rows)
style = Style()
style.configure('Treeview',
                font=('Futura Bk BT', 16),
                foreground='white',
                background='#3A3B3C')
style.configure('Treeview.Heading', font=('Futura Bk BT8*9', 14))
lbll=Label(frame2, text="From: ", foreground='white', background='gray', font='Arial 18 bold').pack(side='left')
ent = PlaceholderEntry(frame2,
                       placeholder="Enter Start",
                       placeholdercolor='gray',
                       width=10,
                       textvariable=q,
                       font=('Futura Bk BT', 25))
ent.configure({"background": "black"})
#ent.pack(side='left')
lblll=Label(frame2, text="To: ", foreground='white', background='gray', font='Arial 18 bold').pack(side='left')
entt = PlaceholderEntry(frame2,
                       placeholder="Enter End",
                       placeholdercolor='gray',
                       width=10,
                       textvariable=q,
                       font=('Futura Bk BT', 25))
entt.configure({"background": "black"})
entt.pack(side='left')
helv36 = tkFont.Font(family='Futura Bk BT', size=16, weight='bold')
img1 = PhotoImage(file=r"C:\Users\acer\Downloads\transparency.png")
img1 = img1.subsample(20, 20)
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\order.png")
img2 = img2.subsample(18, 18)

img3 = PhotoImage(file=r"C:\Users\acer\Downloads\loading-arrow.png")
img3 = img3.subsample(20, 20)

img4 = PhotoImage(file=r"C:\Users\acer\Downloads\undo.png")
img4 = img4.subsample(20, 20)

img22 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img22 = img2.subsample(13,13)
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
style.configure('TButton',
                font=('Futura Bk BT', 15, 'bold'),
                borderwidth=10, activebackground='blue',
                background='blue', foreground='black')
style.map('TButton',
          foreground=[('active', '!disabled', 'focus', 'blue')],
          background=[('active', 'blue')])
buy = Button(window,
                text="Buy",
                #font="Arial 20 bold",
                width=15,
                image=img2,
                compound="right",
                # background='#384448',
                # foreground='white',
                # activebackground='green',
                # relief=SUNKEN,
                # bd=5,
                command=next_page)
Exit = Button(window,
                 text="Return",
                #  font=helv36,
                width=15,
                 image=img4,
                 compound="right",
                #  background='#EB5406',
                #  foreground='white',
                #  activebackground='#DC143C',
                #  relief=SUNKEN,
                #  bd=5,
                 command=exit_func)
sales = Button(window,
                text="Sales",
                #font="Arial 20 bold",
                width=15,
                image=img2,
                compound="right",
                # background='#384448',
                # foreground='white',
                # activebackground='green',
                # relief=SUNKEN,
                # bd=5,
                command=next_page)
buy.place(x=500, y=750)
sales.place(x=292, y=750)
Exit.place(x=850, y=750)
window.mainloop()
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
from tkinter import messagebox
os.chdir(r'C:\Users\acer\Downloads\FRAMEs')
import sqlite3
db = sqlite3.connect('sign_in_db.db')
cr = db.cursor()
cr.execute('create table if not exists suppliers(sname text, snumber integer,pname text, pprice integer)')
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
lbl_img=PhotoImage(file=r"C:\Users\acer\Downloads\industrie-uk-store-covent-garden-7.png")
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
# #########################################################################################################
supp_name = Label(frame, text  = "Enter Supplier Name: ", width=22, foreground='#F4F6F7', background='#5C3317',  font="Arial 25 bold",borderwidth=1)
supp_num= Label(frame, text  = "Enter Supplier Number: ", width=22, foreground='#F4F6F7', background='#5C3317', font="Arial 25 bold")
prod_name= Label(frame, text  = "Enter Product Name: ", width=22, foreground='#F4F6F7', background='#5C3317',  font="Arial 25 bold",borderwidth=1)
prod_prc= Label(frame, text  = "Enter Product Price: ", width=22, foreground='#F4F6F7', background='#5C3317', font="Arial 25 bold")
supp_name_entry= PlaceholderEntry(frame,placeholder='Enter Supplier Name:',  width=25, font='Arial 20 italic')
supp_num_entry= PlaceholderEntry(frame,placeholder='Enter Supplier Number:',  width=25, font='Arial 20 italic')
prod_name_entry= PlaceholderEntry(frame,placeholder='Enter Product Name:',  width=25, font='Arial 20 italic')
prod_prc_entry= PlaceholderEntry(frame,placeholder='Enter Product Price:',  width=25, font='Arial 20 italic')
img = PhotoImage(file=r"C:\Users\acer\Downloads\user (1).png")
img = img.subsample(9,9)
def login_fun():
    if(len(supp_name_entry.get())>0 and len(supp_num_entry.get())>0 and len(prod_name_entry.get())>0 and len(prod_prc_entry.get())>0):
        cr.execute(f'insert into suppliers(sname, snumber, pname, pprice) values("{supp_name_entry.get()}",{int(supp_num_entry.get())} , "{prod_name_entry.get()}",{int(prod_prc_entry.get())} )')
        db.commit()
        messagebox.showinfo('Added', 'Added Succefully')
        prod_name_entry.delete(0,END)
        prod_prc_entry.delete(0,END)
btn_add=Button(frame,  text="ADD  ", compound='right', image=img, command=login_fun, width=15)
#print(f"{screen_height} {screen_width}")
def exit():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
from tkinter import *
lbl=Label(frame,text="Add New Supplier",width=35  ,bg='#5C3317',
               bd=5,
               relief='sunken',
               highlightbackground="red",
               font="Arial 40 bold",
               justify='center',
               fg='white',
               anchor='center').place(x=200,y=70)
from tkinter.ttk import *
supp_name.place(x=350, y=250)
supp_num.place(x=350, y=350)
prod_name.place(x=350, y=450)
prod_prc.place(x=350, y=550)
supp_name_entry.place(x=800, y=250)
supp_num_entry.place(x=800, y=350)
prod_name_entry.place(x=800, y=450)
prod_prc_entry.place(x=800, y=550)
btn_add.place(x=650, y=650)
img5 = PhotoImage(file=r"C:\Users\acer\Downloads\undo.png")
img5=img5.subsample(20,20)
def open_home():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Suppliers_Frame.py')
btn_home=Button(frame,  text="Return", compound='right', image=img5, command=open_home).place(x=690,y=750)
from tkinter import *
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(20,20)
btn_exit=Button(frame,  text="EXIT", compound='right', image=img2, width=90, command=exit, font='Arial 15 bold', bd=4, background='#EB5406',activebackground='Black',  fg='white', padx=8)
btn_exit.place(x=15, y=15)
root.mainloop()
from tkinter import *
import tkinter as tk
from tkinter import font as tkFont
from tkinter import ttk
from tkinter.ttk import *
from tkinter import *
from tkinter.ttk import *
from tkinter import ttk
from tkinter.messagebox import askyesno
from PIL import Image
import tkinter as tk
from tkinter import ttk as ttk
import os
root=Tk()
root.title("reporting")
imgg= PhotoImage(file=r"C:\Users\acer\Downloads\1697103025587.png")
labell=Label(image=imgg)
labell.pack()
screen_width=root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.attributes("-fullscreen", True)
import sqlite3
db=sqlite3.connect("mashrooo3.db")
#database
def purchase():
    
    cr=db.cursor()
    productvar=prod_ent.get()
    amountvar=int(amount_ent.get())
    pricevar=int(price_ent.get())
    dayvar=day_ent.get()
    cr.execute(f"insert into purchases (product_name,amount,price,day) values ('{productvar}',{amountvar},{pricevar},'{dayvar}')")
    cr.execute("update purchases set cost =amount*price")
    cost=amountvar*pricevar
    lbl_cost=tk.Label(root,text=cost,font=('helvatic',13,'bold'))
    lbl_cost.place(x=170,y=400)
    cr.execute(f"update product set amount = amount-{amountvar} where product_name='{productvar}'")
    db.commit()
    db.close()

def increment():
     cr=db.cursor()
     cr.execute("create table if not exists product (product_name text ,amount integer, price integer,supplier text)") 
     productvar=prod_entry.get()
     amountvar=int(amount_entry.get())
     pricevar=int(price_entry.get())
     supvar=sup_entry.get()
     try:
         cr.execute(f"insert into product (product_name,amount,price ,supplier )values ('{productvar}',{amountvar},{pricevar},'{supvar}')")
     
     except:
         cr.execute(f"update product set amount =amount + '{amountvar}' where product_name='{productvar}'")
         
     messagebox.showinfo ('info','added successfuly')
     
     #messagebox.showerror('error','cant add product previosly entered')
     
     db.commit()
     db.close()
    
    
    
    
    
    
    
    
    
    
    

# purchases 
lbl_makpur=tk.Label(root,text="MAKE PURCHASES",font=('helvatic',20,'bold'),bg='azure3')
product=tk.Label(root,text="Product name",font=('helvatic',15,'bold'),bg='azure3')
amount=tk.Label(root,text="Amount",font=('helvatic',15,'bold'),bg='azure3')
price=tk.Label(root,text="Price",font=('helvatic',15,'bold'),bg='azure3')
day=tk.Label(root,text="Date",font=('helvatic',15,'bold'),bg='azure3')
btn_mkpur=tk.Button(root,text="Make purchase",font=('helvatic',10,'bold'),bg='azure3',command=purchase)
prod_ent=tk.Entry(root,font=('helvatic',10,'bold'))
amount_ent=tk.Entry(root,font=('helvatic',10,'bold'))
price_ent=tk.Entry(root,font=('helvatic',10,'bold'))
day_ent=tk.Entry(root,font=('helvatic',10,'bold'))

lbl_makpur.place(x=170,y=100)
product.place(x=150,y=200)
amount.place(x=150,y=250)
price.place(x=150,y=300)
day.place(x=150,y=350)
prod_ent.place(x=300,y=200)
amount_ent.place(x=300,y=250)
price_ent.place(x=300,y=300)
day_ent.place(x=300,y=350)
btn_mkpur.place(x=330,y=400)

# inventory

lbl_increment=tk.Label(root,text="INCREMENT INVENTORY",font=('helvatic',20,'bold'),bg='azure3')
product_inven=tk.Label(root,text="Product name",font=('helvatic',15,'bold'),bg='azure3')
amount_inven=tk.Label(root,text="Amount",font=('helvatic',15,'bold'),bg='azure3')
price_inven=tk.Label(root,text="Price",font=('helvatic',15,'bold'),bg='azure3')
suplier=tk.Label(root,text="Supplier",font=('helvatic',15,'bold'),bg='azure3')
btn_increment=tk.Button(root,text="Buy",font=('helvatic',13,'bold'),bg='azure3',command=increment)


prod_entry=tk.Entry(root,font=('helvatic',10,'bold'))
amount_entry=tk.Entry(root,font=('helvatic',10,'bold'))
price_entry=tk.Entry(root,font=('helvatic',10,'bold'))
sup_entry=tk.Entry(root,font=('helvatic',10,'bold'))

lbl_increment.place(x=800,y=100)
product_inven.place(x=800,y=200)
amount_inven.place(x=800,y=250)
price_inven.place(x=800,y=300)
suplier.place(x=800,y=350)
prod_entry.place(x=950,y=200)
amount_entry.place(x=950,y=250)
price_entry.place(x=950,y=300)
sup_entry.place(x=950,y=350)
btn_increment.place(x=1010,y=380)
img22 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
#img22 = img22.subsample(13,13)
def exit_func2():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
Exit2 = tk.Button(root,
                 text="EXIT",
                 font="Arial 13 bold",
                 width=7,
                 #image=img22,
                 compound="right",
                 background='red',
                 foreground='white',
                 activebackground='#DC143C',
                 relief=SUNKEN,
                 command=exit_func2)
def exit_func():
    root.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/home.py')
    #os.system('home.py')
Exit = tk.Button(root,
                 text="Home",
                 font="Arial 15 bold",
                 width=9,
                 #image=img22,
                 compound="right",
                 background='gray',
                 foreground='white',
                 activebackground='green',
                 relief=SUNKEN,
                 command=exit_func)
Exit2.place(x=750, y=800)
Exit.place(x=730, y=700)
root.mainloop()

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
db = sqlite3.connect("sign_in_db.db")
cursor = db.cursor()
db.commit()
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
    query = "SELECT pname, pprice,sname,snumber FROM suppliers WHERE pname like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)
def clear_func():
    query = "SELECT pname, pprice,sname,snumber FROM suppliers"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)
    ent.remove(0, 30)
# exit to home page function
def exit_func():
    window.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Suppliers_Frame.py')
    #os.system('home.py')
from tkinter.messagebox import askyesno
def exit_func2():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        window.destroy()
def next_page():
    pass
window = Tk()  # the form
q = StringVar()  # made for use in search function
window.attributes('-fullscreen', True)
window.title('Search Page')
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry(f'{screenwidth}x{screenheight}+0+0')
img =PhotoImage(file=r"C:\Users\acer\Downloads\new.png")
label1 = Label(image=img)
label1.image = img
label1.pack()
lbl = tk.Label(window,
               text="Find Best Supplier".title(),
               font=('Futura Bk BT', 35,'bold'),
               background='#3A3B3C',
               foreground='white',
               relief=SUNKEN,
               bd=8,
               pady=8,
               width=32)
lbl.place(x=screenwidth/2-450, y=50)

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
from tkinter.ttk import *
# style = Style()
# style.configure("Treeview.Heading", font=(None, 50))
treeView.heading(1, text="Product Name")
treeView.heading(2, text="Product Price")
treeView.heading(3, text="Supplier Name")
treeView.heading(4, text="Phone Number")

treeView.column(1, width=300, anchor='center')
treeView.column(2, width=200, anchor='center')
treeView.column(3, width=300, anchor='center')
treeView.column(4, width=300, anchor='center')
# traverse data on the tree view section
cursor.execute("select pname, pprice, sname,snumber FROM suppliers")
rows = cursor.fetchall()
update_func(rows)
style = Style()
style.configure('Treeview',
                font=('Futura Bk BT', 16),
                foreground='white',
                background='#3A3B3C')
style.configure('Treeview.Heading', font=('Futura Bk BT8*9', 14))
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

img22 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img22 = img2.subsample(13,13)
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
style.configure('TButton',
                font=('Futura Bk BT', 15, 'bold'),
                borderwidth=10, activebackground='blue',
                background='blue', foreground='black')
style.map('TButton',
          foreground=[('active', '!disabled', 'focus', 'blue')],
          background=[('active', 'blue')])
buy = Button(window,
                text="Buy",
                #font="Arial 20 bold",
                width=15,
                image=img2,
                compound="right",
                # background='#384448',
                # foreground='white',
                # activebackground='green',
                # relief=SUNKEN,
                # bd=5,
                command=next_page)
Exit = Button(window,
                 text="Return",
                #  font=helv36,
                width=15,
                 image=img4,
                 compound="right",
                #  background='#EB5406',
                #  foreground='white',
                #  activebackground='#DC143C',
                #  relief=SUNKEN,
                #  bd=5,
                 command=exit_func)
buy.place(x=500, y=750)
Exit.place(x=850, y=750)
window.mainloop()
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
db = sqlite3.connect("sign_in_db.db")
cursor = db.cursor()
db.commit()


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
        self.s.configure('my.TEntry',forground=self.placeholdercolor)

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
    query = "select sname, snumber,pname,pprice FROM suppliers WHERE sname like '%"+q2+"%'"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)


def clear_func():
    query = "select sname, snumber,pname,pprice FROM suppliers"
    cursor.execute(query)
    rows = cursor.fetchall()
    update_func(rows)
    ent.remove(0, 30)
# exit to home page function
def exit_func():
    window.destroy()
    os.startfile('C:/Users/acer/Downloads/FRAMEs/Suppliers_Frame.py')
    #os.system('home.py')
from tkinter.messagebox import askyesno
def exit_func2():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        window.destroy()
def next_page():
    answer = askyesno(title='Exit Confirmation',
                    message=f"Are you sure that you want to Delete {ent.get()}?".title())
    if answer:
        #print(ent.get())
        cursor.execute(f"Delete from suppliers where sname like '%{ent.get()}%'")
        db.commit()
        messagebox.showinfo('Deleted', 'Deleted Succefully')
window = Tk()  # the form
q = StringVar()  # made for use in search function
window.attributes('-fullscreen', True)
window.title('Search Page')
screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
window.geometry(f'{screenwidth}x{screenheight}+0+0')
img =PhotoImage(file=r"C:\Users\acer\Downloads\new.png")
label1 = Label(image=img)
label1.pack()
lbl = tk.Label(window,
               text="Delete Supplier".title(),
               font=('Futura Bk BT', 35,'bold'),
               background='#8B0000',
               foreground='white',
               relief=SUNKEN,
               bd=8,
               pady=8,
               width=32)
lbl.place(x=screenwidth/2-450, y=50)

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


treeView.heading(3, text="Product Name")
treeView.heading(4, text="Product Price")
treeView.heading(1, text="Supplier Name")
treeView.heading(2, text="Phone Number")

treeView.column(3, width=300, anchor='center')
treeView.column(4, width=200, anchor='center')
treeView.column(1, width=300, anchor='center')
treeView.column(2, width=300, anchor='center')


# traverse data on the tree view section
cursor.execute("select sname, snumber, pname,pprice FROM suppliers")
rows = cursor.fetchall()
update_func(rows)
style = Style()
style.configure('Treeview',
                font=('Futura Bk BT', 16),
                foreground='white',
                background='#2B1B17')
style.configure('Treeview.Heading', font=('Futura Bk BT8*9', 14))

ent = PlaceholderEntry(frame2,
                       placeholder="Enter Supplier Name",
                       placeholdercolor='gray',
                       width=30,
                       textvariable=q,
                       font=('Futura Bk BT', 25))
ent.configure({"background": "black"})
ent.pack(side=tk.LEFT, padx=1)

helv36 = tkFont.Font(family='Futura Bk BT', size=16, weight='bold')

img1 = PhotoImage(file=r"C:\Users\acer\Downloads\transparency.png")
img1 = img1.subsample(20, 20)

img2 = PhotoImage(file=r"C:\Users\acer\Downloads\garbage.png")
img2 = img2.subsample(15, 15)

img3 = PhotoImage(file=r"C:\Users\acer\Downloads\loading-arrow.png")
img3 = img3.subsample(20, 20)

img4 = PhotoImage(file=r"C:\Users\acer\Downloads\undo.png")
img4 = img4.subsample(15,15)

img22 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img22 = img2.subsample(13,13)

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
Exit2 = tk.Button(window,
                 text="EXIT",
                 font=helv36,
                 width=50,
                 image=img22,
                 compound="right",
                 background='red',
                 foreground='white',
                 activebackground='#DC143C',
                 relief=RIDGE,
                 command=exit_func2)
Exit2.place(x=50, y=50)
style.configure('TButton',
                font=('Futura Bk BT', 15, 'bold'),
                borderwidth=10, activebackground='blue',
                background='blue', foreground='black')
style.map('TButton',
          foreground=[('active', '!disabled', 'focus', 'blue')],
          background=[('active', 'blue')])
Exit = Button(window,
                 text="Return",
                #  font=helv36,
                width=15,
                 image=img4,
                 compound="right",
                #  background='#EB5406',
                #  foreground='white',
                #  activebackground='#DC143C',
                #  relief=SUNKEN,
                #  bd=5,
                 command=exit_func)
style2=Style()
style2.configure('TButton',
                font=('Futura Bk BT', 15, 'bold'),
                borderwidth=10, activebackground='red',
                background='red', foreground='red')
style2.map('TButton',
          foreground=[('active', '!disabled', 'focus', 'black')],
          background=[('active', 'black')])
buy = ttk.Button(window,
                text="Delete",
                #font="Arial 20 bold",
                width=15,
                image=img2,
                compound="right",
                # background='#384448',
                # foreground='white',
                # activebackground='green',
                # relief=SUNKEN,
                # bd=5,
                command=next_page)
buy.place(x=500, y=750)
Exit.place(x=850, y=750)
window.mainloop()
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
    pass
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
    os.system('C:\coding\home.py')

def open_supplier():
    root.destroy()
    os.startfile("C:/Users/acer/Downloads/FRAMEs/Suppliers_Frame.py")
    
    #/******************************************************************************************************************/


def open_report():
    root.destroy()
    os.system('C:\coding\home.py')


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

img22 = PhotoImage(file=r"C:\Users\acer\Downloads\cash.png")
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
                 text="Buy  ",
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
user_lbl= Label(frame, text  = "Enter Manager Name: ", width=23, foreground='#F4F6F7', background='#3A3B3C', font="Arial 22 bold", relief=SUNKEN)
pass_lbl= Label(frame, text  = "Enter Manager Password: ", width=23, foreground='#F4F6F7', background='#3A3B3C', font="Arial 22 bold")
user_entry= PlaceholderEntry(frame,placeholder='Enter Username', placeholdercolor="#C0C0C0",width=22,  font='Arial 20 bold')
pass_entry= PlaceholderEntry(frame,placeholder='Enter Password', show='*', width=22, font='Arial 20 bold')
img = PhotoImage(file=r"C:\Users\acer\Downloads\key.png")
img = img.subsample(13,13)
imgg = PhotoImage(file=r"C:\Users\acer\Downloads\question.png")
imgg = imgg.subsample(13,13)
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(13,13)
def login_fun():
    if user_entry.get()=='Abdallah' and pass_entry.get()=='00000000':
        root.destroy()
        os.startfile("C:/Users/acer/Downloads/FRAMEs/Add_Employee.py")
    else: messagebox.showerror("Error", "You Aren't Manager!!")
def mang():
    root.destroy()
    os.startfile("C:/Users/acer/Downloads/FRAMEs/National_Id.py")
btn_login=Button(frame,  text="Iam The Manager  ", width=18, compound='right', image=img, command=login_fun)
btn_login2=Button(frame,  text="Forgot Password? ", width=18, compound='right', image=imgg, command=mang)
#print(f"{screen_height} {screen_width}")
def exit():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
lbl=Label(frame,text="Manager Authentication",width=35, background='#3A3B3C', font="Arial 40 bold",justify='center', foreground='white',padding=(10, 5), anchor='center').place(x=280,y=70)
user_lbl.place(x=300, y=400)
pass_lbl.place(x=300, y=450)
user_entry.place(x=700, y=400)
pass_entry.place(x=700, y=450)
btn_login.place(x=600, y=550)
btn_login2.place(x=600, y=650)
from tkinter import *
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(20,20)
img5 = PhotoImage(file=r"C:\Users\acer\Downloads\undo.png")
img5 = img5.subsample(20,20)
def mang():
    root.destroy()
    os.startfile("C:/Users/acer/Downloads/FRAMEs/Login_Frame.py")
btn_home=tk.Button(frame,  text="Return", compound='right', image=img5, width=125, command=mang, font='Arial 15 bold', bd=4, background='gray',activebackground='gray',  fg='white', padx=8, relief=SOLID)
btn_exit=Button(frame,  text="EXIT", compound='right', image=img2, width=90, command=exit, font='Arial 15 bold', bd=4, background='#EB5406',activebackground='Black',  fg='white', padx=8)
btn_exit.place(x=15, y=15)
btn_home.place(x=670, y=750)

root.mainloop()

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
from tkinter import messagebox
from tkinter.messagebox import showerror
import sqlite3
os.chdir(r'C:\Users\acer\Downloads\FRAMEs')
db = sqlite3.connect("sign_in_db.db")
cr = db.cursor()
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
lbl_img=PhotoImage(file=r"C:\Users\acer\Downloads\new.png")
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
user_lbl= Label(frame, text  = "Enter Username: ", width=18, foreground='#F4F6F7', background="#951D11", font="Arial 22 bold")
pass_lbl= Label(frame, text  = "Enter Password: ", width=18, foreground='#F4F6F7', background="#951D11", font="Arial 22 bold")
user_entry= PlaceholderEntry(frame,placeholder='Enter Username', placeholdercolor="#C0C0C0",width=22,  font='Arial 20 bold')
pass_entry= PlaceholderEntry(frame,placeholder='Enter Password', show='*', width=22, font='Arial 20 bold')
img = PhotoImage(file=r"C:\Users\acer\Downloads\key.png")
img = img.subsample(13,13)
imgg = PhotoImage(file=r"C:\Users\acer\Downloads\manager.png")
imgg = imgg.subsample(13,13)
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(13,13)
def login_fun():
    database= cr.execute('select * from sign_in').fetchall()
    flag=0
    for i in database:
        #print(i[0]==user_entry.get(), end=' ')
        #print(i[1]==pass_entry.get(), end=' ')
        if(i[0]==user_entry.get() and i[1]==int(pass_entry.get())):
            flag=1
    if(flag):
        root.destroy()
        os.startfile(r'C:\Users\acer\Downloads\FRAMEs\home.py')
    else:
        messagebox.showerror('Not Valid!', "Invalid credentials. Staff access only.")

def mang():
    root.destroy()
    os.startfile("C:/Users/acer/Downloads/FRAMEs/Manager.py")
btn_login=Button(frame,  text="Log in!  ", width=18, compound='right', image=img, command=login_fun)
btn_login2=Button(frame,  text="Are You Manager?", width=18, compound='right', image=imgg, command=mang)
#print(f"{screen_height} {screen_width}")
def exit():
    answer = askyesno(title='Exit Confirmation',
                    message='Are you sure that you want to quit?'.title())
    if answer:
        root.destroy()
lbl=Label(frame,text="Welcome To clothing Store System",width=35, background='#5C3317', font="Arial 40 bold",justify='center', foreground='white',padding=(10, 5), anchor='center').place(x=280,y=70)
user_lbl.place(x=400, y=400)
pass_lbl.place(x=400, y=450)
user_entry.place(x=700, y=400)
pass_entry.place(x=700, y=450)
btn_login.place(x=600, y=550)
btn_login2.place(x=600, y=650)
from tkinter import *
img2 = PhotoImage(file=r"C:\Users\acer\Downloads\button.png")
img2 = img2.subsample(20,20)
btn_exit=Button(frame,  text="EXIT", compound='right', image=img2, width=90, command=exit, font='Arial 15 bold', bd=4, background='#EB5406',activebackground='Black',  fg='white', padx=8)
btn_exit.place(x=15, y=15)
db.commit()
root.mainloop()