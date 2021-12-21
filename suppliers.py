from tkinter import *
import tkinter
from PIL import Image, ImageTk
from datetime import date
from tkinter import ttk,messagebox

from create_db import DatabaseConnection

db=DatabaseConnection()
db.create_db_supplier()


class supplierClass:
    def add_suppliers(self):
        try:
            if self.var_sup_invoice.get()=='':
                messagebox.showerror('Error','Employee ID is required',parent=root)
            else:
                add_emp=db.add_suppliers(int(self.var_sup_invoice.get()),
                                             self.var_name.get(),
                                             self.var_contact.get(),                  
                                             self.txt_description.get('1.0',END))
                messagebox.showinfo('Success','Supplier Added Successfully',parent=self.root)
                db.show_suppliers(self.SupplierTable,END,self.root,messagebox)
            
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')
            
    def update_suppliers(self):
        
        update_emp=db.update_suppliers(int(self.var_sup_invoice.get()),
                             self.var_name.get(),
                             self.var_contact.get(),
                             self.txt_description.get('1.0',END),
                            messagebox,self.root)
        db.show_suppliers(self.SupplierTable,END,self.root,messagebox)

    def delete_suppliers(self):
        if self.var_sup_invoice.get()=='':
            messagebox.showerror('Error','Employee ID is Required',parent= self.root)
        else:
            delete_emp=db.delete_suppliers(int(self.var_sup_invoice.get()),messagebox,self.root,self.var_name.get())
            db.show_suppliers(self.SupplierTable,END,self.root,messagebox)
            self.clear_data()
        

    def get_data(self,ev):
        f=self.SupplierTable.focus()
        content=(self.SupplierTable.item(f))
        row=content['values']
        
        self.var_sup_invoice.set(row[0])
        self.var_contact.set(row[2])
        self.var_name.set(row[1])                  
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[3])


    def clear_data(self):
        self.var_sup_invoice.set('')
        self.var_contact.set('')
        self.var_name.set('')                   
        self.txt_description.delete('1.0',END)
        self.var_searchtxt.set('')
        
        db.show_suppliers(self.SupplierTable,END,self.root,messagebox)

    def search_suppliers(self):
        search_emp=db.search_suppliers(messagebox,self.root,self.var_searchtxt.get(),END,self.SupplierTable)

    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x520+220+130')
        self.root.title('Inventory Management System | Developed by Bman')
        root.config(bg='white')
        self.root.focus_force()

        #====variables
        self.var_sup_invoice=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_searchtxt=StringVar()

        #====================search Label=========
        lbl_search=Label(self.root, text='Invoice No.',font=('goudy old style',15),bg='white').place(x=670,y=70)
        txt_search=Entry(self.root,textvariable=self.var_searchtxt,font=('goudy old style',15),bg='lightyellow').place(x=770,y=70,width=150)
        btn_search=Button(self.root,command=self.search_suppliers, text='Search',font=('goudy old style',15),bg='#4caf50',cursor='hand2',
                          fg='white').place(x=930,y=70, width=150,height=30)

        #=====title=====
        title=Label(self.root, text='Manage Supplier Details', font=('goudy old style',20), bg='#0f4d7d',
                    fg='white').place(x=10,y=10,width=1070)
        #==========content=================
        lbl_sup_invoice=Label(self.root, text='Invoice No.',font=('goudy old style',15),bg='white').place(x=10,y=70)
        lbl_name=Label(self.root, text='Name',font=('goudy old style',15),bg='white').place(x=10,y=110)
        lbl_contact=Label(self.root, text='Contact',font=('goudy old style',15),bg='white').place(x=10,y=150)
        lbl_description=Label(self.root, text='Description',font=('goudy old style',15),bg='white').place(x=10,y=190)
        
        
        lbl_sup_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=('goudy old style',15),
                         bg='lightgrey').place(x=147,y=70)
        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15),
                         bg='lightyellow').place(x=147,y=110)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15),
                         bg='lightyellow').place(x=147,y=150)
        self.txt_description=Text(self.root,font=('goudy old style',15),
                         bg='lightyellow')
        self.txt_description.place(x=147,y=190,width=470,height=130)
        
        #=====================buttons
        
        btn_add=Button(self.root,command=self.add_suppliers, text='Save', font=('goudy old style',15),fg='white',bg='#2196f3',
                       cursor='hand2').place(x=147,y=450,width=110,height=28)
        btn_update=Button(self.root,command=self.update_suppliers, text='Update',font=('goudy old style',15),fg='white',bg='#4caf50',
                       cursor='hand2').place(x=267,y=450,width=110,height=28)
        btn_delete=Button(self.root,command=self.delete_suppliers,text='Delete',font=('goudy old style',15),fg='white',bg='#f44336',
                       cursor='hand2').place(x=387,y=450,width=110,height=28)
        btn_clear=Button(self.root, command=self.clear_data,text='Clear',font=('goudy old style',15),fg='white',bg='#607d8b',
                       cursor='hand2').place(x=507,y=450,width=110,height=28)

        
        #============display scrollbar
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=670,y=110, height=370, width=410)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
 
        self.SupplierTable=ttk.Treeview(emp_frame,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,
                                        columns=('invoice','name','contact','description'))

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)
        
        self.SupplierTable.heading('invoice',text='Sup ID')
        self.SupplierTable.heading('name',text='Name')
        self.SupplierTable.heading('contact',text='Contact')
        self.SupplierTable.heading('description',text='Description')
        self.SupplierTable['show']='headings'

        self.SupplierTable.pack(fill=BOTH, expand=1)
        self.SupplierTable.bind('<ButtonRelease-1>',self.get_data)
        
        self.SupplierTable.column('invoice',width=20)
        self.SupplierTable.column('name',width=100)
        self.SupplierTable.column('description',width=100)
        self.SupplierTable.column('contact',width=50)
        #=======================show employees
        db.show_suppliers(self.SupplierTable,END,self.root,messagebox)
        
       
if __name__=='__main__':
    root=Tk()
    empl=supplierClass(root)
    root.mainloop()
