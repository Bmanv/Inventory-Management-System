from tkinter import *
import tkinter
from PIL import Image, ImageTk
from datetime import date
from tkinter import ttk,messagebox

from create_db import DatabaseConnection

db=DatabaseConnection()
db.create_db_category()


class categoryClass:
    def add_category(self):
        try:
            if self.var_name.get()=='':
                messagebox.showerror('Error','Employee ID is required',parent=root)
            else:
                add_emp=db.add_category(self.var_name.get())
                messagebox.showinfo('Success','Category Added Successfully',parent=self.root)
                db.show_category(self.SupplierTable,END,self.root,messagebox)
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')
            
    def update_category(self):
        update_emp=db.update_category(self.var_name.get(),self.var_cate_id.get(),messagebox,self.root)
        db.show_category(self.SupplierTable,END,self.root,messagebox)

    def delete_category(self):
        if self.var_name.get()=='':
            messagebox.showerror('Error','Employee ID is Required',parent= self.root)
        else:
            delete_emp=db.delete_category(messagebox,self.root,self.var_name.get())
            db.show_category(self.SupplierTable,END,self.root,messagebox)
            self.clear_data()
        

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        self.var_cate_id.set(row[0])
        self.var_name.set(row[1])


    def clear_data(self):
        self.var_name.set('')                   
        db.show_category(self.SupplierTable,END,self.root,messagebox)

    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x520+220+130')
        self.root.title('Inventory Management System | Developed by Bman')
        root.config(bg='white')
        self.root.focus_force()

        #====variables
        self.var_cate_id=StringVar()
        self.var_name=StringVar()

        #=====title=====
        title=Label(self.root, text='Manage Product Category', bd=3,font=('goudy old style',40,'bold'), bg='#0f4d7d',
                    fg='white',relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10)
        #==========content=================
        lbl_name=Label(self.root, text='Enter Category Name',
                       font=('goudy old style',20,'bold'),bg='white').place(x=10,y=110)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15),
                         bg='lightyellow').place(x=10,y=165,width=300,height=30)
        
        #=====================buttons
        btn_add=Button(self.root,command=self.add_category, text='Save', font=('goudy old style',15),fg='white',bg='#2196f3',
                       cursor='hand2').place(x=10,y=210,width=110,height=28)
        btn_update=Button(self.root,command=self.update_category, text='Update',font=('goudy old style',15),fg='white',bg='#4caf50',
                       cursor='hand2').place(x=130,y=210,width=110,height=28)
        btn_delete=Button(self.root,command=self.delete_category,text='Delete',font=('goudy old style',15),fg='white',bg='#f44336',
                       cursor='hand2').place(x=250,y=210,width=110,height=28)
        btn_clear=Button(self.root, command=self.clear_data,text='Clear',font=('goudy old style',15),fg='white',bg='#607d8b',
                       cursor='hand2').place(x=370,y=210,width=110,height=28)

        #============display scrollbar
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=670,y=110, height=100, width=410)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
 
        self.SupplierTable=ttk.Treeview(emp_frame,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,
                                        columns=('cid','name'))

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading('cid',text='Cat ID')
        self.SupplierTable.heading('name',text='Name')
        self.SupplierTable['show']='headings'
        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind('<ButtonRelease-1>',self.get_data)
        
        self.SupplierTable.column('cid',width=20)
        self.SupplierTable.column('name',width=100)
        #=======================show categories
        db.show_category(self.SupplierTable,END,self.root,messagebox)
        
       
if __name__=='__main__':
    root=Tk()
    empl=categoryClass(root)
    root.mainloop()
