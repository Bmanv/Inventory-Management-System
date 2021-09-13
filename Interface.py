from tkinter import *
import tkinter
from PIL import Image, ImageTk
from datetime import date
import time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1350x700+0+0')
        self.root.title('Inventory Management System | Developed by Bman')
        root.config(bg='white')

        #======Title==========
        self.icon_title=Image.open("images/title2.jpg")
        self.icon_title=self.icon_title.resize((70,68))
        self.icon_title=ImageTk.PhotoImage(self.icon_title)
        title=Label(self.root, text='Inventroy Management System', image=self.icon_title,compound=LEFT,
                    font=('times new roman',40,'bold'),bg='#010c48'
                    ,fg='white', anchor='w',padx=20).place(x=0,y=0, relwidth=1, height=70)

        #=========Logout Button===========
        log_out=Button(self.root, text='Logout', font=('times new roman', 15, 'bold'),cursor='hand2',
                       bg='#009688').place(x=1150,y=10,height=50,width=150)
        #========clock====
        
        self.lbl_clock=Label(root,
                             text=f'Welcome To Inventor Management System\t\tDate: {date.today()}\t\tTime: {time.strftime("%H:%M:%S")}',
                             bg='grey',font=('times new roman', 15))
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        #================ Left Menu=============
        self.MenuLogo=Image.open('images/menulogo.png')
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        
        LeftMenu=Frame(self.root, bd=2, relief=RIDGE, bg='white')
        LeftMenu.place(x=0,y=102, width=200,height=565)

        lbl_menuLogo=Label(LeftMenu, image=self.MenuLogo).pack(side=TOP,fill=X)
        #menu label
        lbl_menu=Label(LeftMenu, text='Menu', font=('times new roman',20), bg='#009688').pack(side=TOP,fill=X)
        #menu button 1
        self.icon_side=Image.open('images/icon_side.png')
        self.icon_side=self.icon_side.resize((20,20))
        self.icon_side=ImageTk.PhotoImage(self.icon_side)
        
        btn_employee=Button(LeftMenu,text='Employee',image=self.icon_side, compound=LEFT,padx=5,anchor='w',
                            font=('times new roman',20,'bold'),bg='white',cursor='hand2', bd=3).pack(side=TOP,fill=X)
        btn_supplier=Button(LeftMenu,text='Supplier',image=self.icon_side, compound=LEFT,padx=5,anchor='w',
                            font=('times new roman',20,'bold'),bg='white',cursor='hand2', bd=3).pack(side=TOP,fill=X)
        btn_category=Button(LeftMenu,text='Category',image=self.icon_side, compound=LEFT,padx=5,anchor='w',
                            font=('times new roman',20,'bold'),bg='white',cursor='hand2', bd=3).pack(side=TOP,fill=X)
        btn_product=Button(LeftMenu,text='Products',image=self.icon_side, compound=LEFT,padx=5,anchor='w',
                            font=('times new roman',20,'bold'),bg='white',cursor='hand2', bd=3).pack(side=TOP,fill=X)
        btn_sales=Button(LeftMenu,text='Sales',image=self.icon_side, compound=LEFT,padx=5,anchor='w',
                            font=('times new roman',20,'bold'),bg='white',cursor='hand2', bd=3).pack(side=TOP,fill=X)
        btn_exit=Button(LeftMenu,text='Exit',image=self.icon_side, compound=LEFT,padx=5,anchor='w',
                            font=('times new roman',20,'bold'),bg='white',cursor='hand2', bd=3).pack(side=TOP,fill=X)

        #=============content=============
        self.lbl_employee=Label(self.root,text='Total Employee\n[ 0 ]',
                                bg='#1F618D',fg='white',bd=5,font=('goudy old style',20,'bold'),
                                relief=RIDGE).place(x=300,y=120,height=150,width=300)
        self.lbl_supplier=Label(self.root,text='Total Suppliers\n[ 0 ]',
                                bg='#EC7063',fg='white',bd=5,font=('goudy old style',20,'bold'),
                                relief=RIDGE).place(x=650,y=120,height=150,width=300)
        self.lbl_category=Label(self.root,text='Total Categories\n[ 0 ]',
                                bg='#009688',fg='white',bd=5,font=('goudy old style',20,'bold'),
                                relief=RIDGE).place(x=1000,y=120,height=150,width=300)
        self.lbl_product=Label(self.root,text='Total Products\n[ 0 ]',
                                bg='grey',fg='white',bd=5,font=('goudy old style',20,'bold'),
                                relief=RIDGE).place(x=300,y=300,height=150,width=300)
        self.lbl_sales=Label(self.root,text='Total Sales\n[ 0 ]',
                                bg='#D4AC0D',fg='white',bd=5,font=('goudy old style',20,'bold'),
                                relief=RIDGE).place(x=650,y=300,height=150,width=300)
        #=========labele footer=======
        lbl_footer=Label(self.root,text='IMS-Inventory Management System | Developed By Bman\nFor any technical issues, contact 031xxxx6754',
                         font=('times new roman',15),bg='grey').pack(side=BOTTOM,fill=X)
        

root=Tk()
IMS_obj=IMS(root)

root.mainloop()
