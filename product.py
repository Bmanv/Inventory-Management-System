from tkinter import *
import tkinter
from PIL import Image, ImageTk
from datetime import date
from tkinter import ttk,messagebox

from create_db import DatabaseConnection

db=DatabaseConnection()
db.create_db_category()


class productClass:
    def add_product(self):
        try:
            if self.var_name.get()=='':
                messagebox.showerror('Error','Product name is required',parent=root)
            else:
                add_pr=db.add_product(self.var_category.get(),self.var_supplier.get(),
                                      self.var_name.get(),self.var_price.get(),
                                      self.var_quantity.get(),self.var_status.get())
                messagebox.showinfo('Success','Product Added Successfully',parent=self.root)
                db.show_product(self.EmployeeTable,END,self.root,messagebox)
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')
            
    def update_product(self):
        update_emp=db.update_product(self.var_category.get(),self.var_supplier.get(),
                                      self.var_name.get(),self.var_price.get(),
                                      self.var_quantity.get(),self.var_status.get(),self.var_pro_id.get(),
                                      messagebox,root)
        db.show_product(self.EmployeeTable,END,self.root,messagebox)

    def delete_poduct(self):
        if self.var_name.get()=='':
            messagebox.showerror('Error','Employee ID is Required',parent= self.root)
        else:
            delete_emp=db.delete_product(self.var_name.get(),messagebox,root)
            db.show_product(self.EmployeeTable,END,self.root,messagebox)
            self.clear_data()
        

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        
        self.var_pro_id.set(row[0])
        self.var_category.set(row[1])
        self.var_supplier.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_quantity.set(row[5])
        self.var_status.set(row[6])

    def clear_data(self):
        self.var_name.set('')
        self.cmb_cat.current(0)
        self.cmb_sup.current(0)
        self.var_price.set('')
        self.var_quantity.set('')
        self.cmb_status.current(0)
        
        db.show_product(self.EmployeeTable,END,self.root,messagebox)

    def search(self):
        search_emp=db.search(self.cmb_search.get(),messagebox,self.root,self.var_searchtxt.get(),END,self.EmployeeTable)

    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x520+220+130')
        self.root.title('Inventory Management System | Developed by Bman')
        root.config(bg='white')
        self.root.focus_force()

        #====variables
        self.var_pro_id=StringVar()
        self.var_category=StringVar()
        self.var_supplier=StringVar()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_quantity=StringVar()
        self.var_status=StringVar()

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
       

        #=====frames=====
        product_frame=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        product_frame.place(x=10,y=10,width=450,height=480)
        #=====title=====
        title=Label(product_frame, text='Product Details', bd=3,font=('goudy old style',18,'bold'), bg='#0f4d7d',
                    fg='white',relief=RIDGE).pack(side=TOP,fill=X)
        #==========content=================
        lbl_cat=Label(product_frame,text='Category',font=('times new roman',18),bg='white').place(x=30,y=60)
        lbl_supplier=Label(product_frame,text='Supplier',font=('times new roman',18),bg='white').place(x=30,y=110)
        lbl_name=Label(product_frame,text='Name',font=('times new roman',18),bg='white').place(x=30,y=160)
        lbl_price=Label(product_frame,text='Price',font=('times new roman',18),bg='white').place(x=30,y=210)
        lbl_qty=Label(product_frame,text='Quantity',font=('times new roman',18),bg='white').place(x=30,y=260)
        lbl_status=Label(product_frame,text='Status',font=('times new roman',18),bg='white').place(x=30,y=310)

        cat_names=db.show_category_sales(messagebox,root)
        self.cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_category,values=cat_names,state='readonly',justify=CENTER,
                             font=('times new roman',18))
        self.cmb_cat.place(x=150,y=60, width=200)
        self.cmb_cat.current(0)
        supplier_list=db.show_sales_suppliers(root,messagebox)
        self.cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_supplier,values=supplier_list,state='readonly',justify=CENTER,
                             font=('times new roman',18))
        self.cmb_sup.place(x=150,y=110, width=200)
        self.cmb_sup.current(0)
        txt_name=Entry(product_frame,textvariable=self.var_name,bg='lightyellow').place(x=150,y=160,width=200,height=30)
        txt_price=Entry(product_frame,textvariable=self.var_price,bg='lightyellow').place(x=150,y=210,width=200,height=30)
        txt_qty=Entry(product_frame,textvariable=self.var_quantity,bg='lightyellow').place(x=150,y=260,width=200,height=30)
        self.cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=('Active','Inactive'), state='readonly',justify=CENTER,
                                font=('times new roman',18))
        self.cmb_status.place(x=150,y=310,width=200)
        self.cmb_status.current(0)

    
        
        #=============buttons========
        btn_add=Button(product_frame,command=self.add_product,text='Save',font=('times new roman',18),bg='skyblue').place(x=10,y=390,width=100)
        btn_update=Button(product_frame,command=self.update_product,text='Update',font=('times new roman',18),bg='green').place(x=120,y=390,width=100)
        btn_delete=Button(product_frame,command=self.delete_poduct,text='Delete',font=('times new roman',18),bg='red').place(x=230,y=390,width=100)
        btn_clear=Button(product_frame,command=self.clear_data,text='Clear',font=('times new roman',18),bg='grey').place(x=340,y=390,width=100)
       
        #================================search frame
        search_frame=LabelFrame(self.root, text='Search Product', font=('times new roman',18),bd=2,bg='white')
        search_frame.place(x=480, y=10,width=600, height= 80)

        self.cmb_search=ttk.Combobox(search_frame,textvariable=self.var_searchby, values=('Select','Category','Supplier','Name'), state='readonly', justify=CENTER)
        self.cmb_search.place(x=10,y=10, width=180,height=30)
        self.cmb_search.current(0)

        txt_search=Entry(search_frame,textvariable=self.var_searchtxt,font=('times new roman',12),bg='lightyellow').place(x=210,y=10,width=200,height=30)
        btn_search=Button(search_frame,command=self.search, text='search', font=('times new roman',22),bg='green',fg='white').place(x=430,y=10,height=30, width=150)

        #============display scrollbar
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=480,y=100, height=390, width=600)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
 
        self.EmployeeTable=ttk.Treeview(emp_frame,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,
                                        columns=('pid','Category','Supplier','name','price','qty','status'))

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading('pid',text='Emp ID')
        self.EmployeeTable.heading('Category',text='Category')
        self.EmployeeTable.heading('Supplier',text='Supplier')
        self.EmployeeTable.heading('name',text='Name')
        self.EmployeeTable.heading('price',text='Price')
        self.EmployeeTable.heading('qty',text='Quantity')
        self.EmployeeTable.heading('status',text='Stutas')
       
        self.EmployeeTable['show']='headings'

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind('<ButtonRelease-1>',self.get_data)
        
        self.EmployeeTable.column('pid',width=100)
        self.EmployeeTable.column('Category',width=100)
        self.EmployeeTable.column('Supplier',width=100)
        self.EmployeeTable.column('name',width=100)
        self.EmployeeTable.column('price',width=100)
        self.EmployeeTable.column('qty',width=100)
        self.EmployeeTable.column('status',width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        #=======================show employees
        db.show_product(self.EmployeeTable,END,self.root,messagebox)
        
if __name__=='__main__':
    root=Tk()
    empl=productClass(root)
    root.mainloop()
