from tkinter import *
import tkinter
from PIL import Image, ImageTk
from datetime import date
import time
from tkinter import messagebox
from os import listdir as dir  

from employees import employeeClass
from suppliers import supplierClass
from categories import categoryClass

from create_db import DatabaseConnection
db=DatabaseConnection()

class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x520+220+130')
        self.root.title('Inventory Management System | Developed by Bman')
        root.config(bg='white')
        self.root.focus_force()


        #============variables
        self.bill_list=[]
        self.var_invoicetxt=StringVar()
        #=====================Title
        title=Label(self.root, text='View Customer Bills ', bd=3,font=('goudy old style',30,'bold'), bg='#0f4d7d',
                    fg='white',relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)

        #=========== Content
        font_style={'font':('times new roman',15)}
        #---------labels
        lbl_invoice=Label(root, text='Invoice no.', **font_style,bg='white').place(x=50,y=100)

        #---------entries
        txt_invoice=Entry(root,**font_style,textvariable=self.var_invoicetxt, bg='lightyellow').place(x=160, y=100,width=180,height=28)

        #--------button seaech
        btn_search=Button(root,text='search',command=self.search, font=('times new roman',15,'bold'),bg='#2196f3',
                          fg='white',cursor='hand2').place(x=360,y=100, width=120,height=28)
        btn_clear=Button(root,text='clear', command=self.clear, font=('times new roman',15,'bold'),bg='lightgray',
                          cursor='hand2').place(x=490,y=100, width=120,height=28)

                        
        #===================bill frame
        sale_frame=Frame(root,bd=3,relief=RIDGE)
        sale_frame.place(x=50,y=140,width=200,height=330)
        
        scrolly=Scrollbar(sale_frame,orient=VERTICAL)
        self.sales_list=Listbox(sale_frame,font=('goudy old stle',15), bg='white',yscrollcommand=scrolly.set)
        scrolly.pack(side=RIGHT, fill=Y)
        scrolly.config(command=self.sales_list.yview())
        self.sales_list.pack(fill=BOTH, expand=1)
        self.sales_list.bind('<ButtonRelease-1>',self.get_data)

         #===================bill frame
        bill_frame=Frame(root,bd=3,relief=RIDGE)
        bill_frame.place(x=280,y=140,width=410,height=330)
        
        #=====================Title
        bill_title=Label(bill_frame, text=' Customer Bill Area', bd=3,font=('goudy old style',20), bg='orange',
                        ).pack(side=TOP,fill=X,padx=3,pady=3)

        scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,font=('goudy old stle',15), bg='lightyellow',yscrollcommand=scrolly2.set)
        scrolly2.pack(side=RIGHT, fill=Y)
        scrolly2.config(command=self.sales_list.yview())
        self.bill_area.pack(fill=BOTH, expand=1)
        

        self.billpic=Image.open('images/bill.jpg')
        self.billpic=self.billpic.resize((390,300),Image.ANTIALIAS)
        self.billpic=ImageTk.PhotoImage(self.billpic)

        lbl_bill_image=Label(self.root, image=self.billpic, bd=0)
        lbl_bill_image.place(x=700,y=140)
        
        self.show()
    def show(self):
        del self.bill_list[:]
        self.sales_list.delete(0,END)
        for i in dir('bills'):
            if i.split('.')[-1]=='txt':
                self.sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        
        index_=self.sales_list.curselection()
        file_name=self.sales_list.get(index_)
        fp=open(f'./bills/{file_name}','r')
        self.bill_area.delete('1.0',END)
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close

    def search(self):
        if self.var_invoicetxt.get()=='':
            messagebox.showerror('Error','Invoice no. is required',parent=self.root)
        else:
            if self.var_invoicetxt.get() in self.bill_list:
                fp=open(f'./bills/{self.var_invoicetxt.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close
            else:
                messagebox.showerror('Error','Invalid Invoice No.',parent=self.root)


    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)
        self.var_invoicetxt.set('')
        

if __name__=='__main__':
    root=Tk()
    sales=salesClass(root)
    root.mainloop()
