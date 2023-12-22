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