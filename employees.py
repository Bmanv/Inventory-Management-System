from tkinter import *
import tkinter
from PIL import Image, ImageTk
from datetime import date
from tkinter import ttk,messagebox

from create_db import DatabaseConnection

db=DatabaseConnection()



class employeeClass:
    def add_employee(self):
        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error','Employee ID is required',parent=root)
            else:
                add_emp=db.add_employees(int(self.var_emp_id.get()),
                                            self.var_gender.get(),
                                            self.var_contact.get(),
                                         
                                            self.var_name.get(),
                                            self.var_dob.get(),
                                            self.var_doj.get(),
                                                         
                                            self.var_email.get(),
                                            self.var_pass.get(),
                                            self.var_utype.get(),
                                                                     
                                            self.txt_address.get('1.0',END),
                                            int(self.var_salary.get()))
                
                messagebox.showinfo('Success','Employee Added Successfully',parent=self.root)
                db.show_employees(self.EmployeeTable,END,self.root,messagebox)
                db.number_of_emp()
            
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')
            
    def updates(self):
        update_emp=db.update(int(self.var_emp_id.get()),
                            self.var_gender.get(),
                            self.var_contact.get(),

                            self.var_name.get(),
                            self.var_dob.get(),
                            self.var_doj.get(),
                                         
                            self.var_email.get(),
                            self.var_pass.get(),
                            self.var_utype.get(),
                                            
                            self.txt_address.get('1.0',END),
                            int(self.var_salary.get()),
                            messagebox,self.root)
        db.show_employees(self.EmployeeTable,END,self.root,messagebox)
        db.number_of_emp()

    def delete(self):
        if self.var_emp_id.get()=='':
            messagebox.showerror('Error','Employee ID is Required',parent= self.root)
        else:
            delete_emp=db.delete(int(self.var_emp_id.get()),messagebox,self.root,self.var_name.get())
            db.show_employees(self.EmployeeTable,END,self.root,messagebox)
            self.clear_data()
            db.number_of_emp()
        

    def get_data(self,ev):
        f=self.EmployeeTable.focus()
        content=(self.EmployeeTable.item(f))
        row=content['values']
        
        self.var_emp_id.set(row[0])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])

        self.var_name.set(row[1])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
                     
        self.var_email.set(row[2])
        self.var_pass.set(row[7])
        self.var_utype.set(row[8])
                             
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])

    def clear_data(self):
        self.var_emp_id.set('')
        self.cmb_gender.current(0)
        self.var_contact.set('')

        self.var_name.set('')
        self.var_dob.set('')
        self.var_doj.set('')
                     
        self.var_email.set('')
        self.var_pass.set('')
        self.cmb_utype.current(0)
                             
        self.txt_address.delete('1.0',END)
        self.var_salary.set('')
        self.var_searchtxt.set('')
        self.cmb_search.current(0)
        db.show_employees(self.EmployeeTable,END,self.root,messagebox)

    def search(self):
        search_emp=db.search(self.cmb_search.get(),messagebox,self.root,self.var_searchtxt.get(),END,self.EmployeeTable)

    def __init__(self,root):
        self.root=root
        self.root.geometry('1100x520+220+130')
        self.root.title('Inventory Management System | Developed by Bman')
        root.config(bg='white')
        self.root.focus_force()

        #====variables
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_doj=StringVar()
        self.var_salary=StringVar()

        #====================search Label=========
        SearchFrame=LabelFrame(self.root,text='Searh Employee', bg='white', font=('gould old style', 12), bd=2, relief=RIDGE)
        SearchFrame.place(x=250, y=20, width=600,height=70)

        #==================options==========
        self.cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=('Select','Email','Name','Contact'),
                                state='readonly',justify=CENTER,font=('goudy old style',15))
        self.cmb_search.place(x=10,y=10,width=180)
        self.cmb_search.current(0)

        txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=('goudy old style',15),bg='lightyellow').place(x=200,y=10)
        btn_search=Button(SearchFrame,command=self.search, text='Search',font=('goudy old style',15),bg='#4caf50',cursor='hand2',
                          fg='white').place(x=410,y=10, width=150,height=30)

        #=====title=====
        title=Label(self.root, text='Employee Details', font=('goudy old style',15), bg='#0f4d7d',
                    fg='white').place(x=50,y=100,width=1000)
        #==========content=================
        lbl_emp_id=Label(self.root, text='Emp ID',font=('goudy old style',15),bg='white').place(x=50,y=150)
        lbl_gender=Label(self.root, text='Gender',font=('goudy old style',15),bg='white').place(x=390,y=150)
        lbl_contact=Label(self.root, text='Contact',font=('goudy old style',15),bg='white').place(x=750,y=150)
        
        txt_emp_id=Entry(self.root,textvariable=self.var_emp_id,font=('goudy old style',15),
                         bg='lightyellow').place(x=147,y=150)
        self.cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=('Select','Male','Female','other'),
                                state='readonly',justify=CENTER,font=('goudy old style',15))
        self.cmb_gender.place(x=500,y=150,width=200)
        self.cmb_gender.current(0)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=('goudy old style',15),
                         bg='lightyellow').place(x=850,y=150)


        lbl_name=Label(self.root, text='Name',font=('goudy old style',15),bg='white').place(x=50,y=190)
        lbl_dob=Label(self.root, text='D.O.B',font=('goudy old style',15),bg='white').place(x=390,y=190)
        lbl_doj=Label(self.root, text='D.O.J',font=('goudy old style',15),bg='white').place(x=750,y=190)

        txt_name=Entry(self.root,textvariable=self.var_name,font=('goudy old style',15),
                         bg='lightyellow').place(x=147,y=185)
        txt_dob=Entry(self.root,textvariable=self.var_dob,font=('goudy old style',15),
                         bg='lightyellow').place(x=500,y=185)
        txt_doj=Entry(self.root,textvariable=self.var_doj,font=('goudy old style',15),
                         bg='lightyellow').place(x=850,y=185)

        lbl_email=Label(self.root, text='Email',font=('goudy old style',15),bg='white').place(x=50,y=220)
        lbl_pass=Label(self.root, text='Password',font=('goudy old style',15),bg='white').place(x=390,y=220)
        lbl_utype=Label(self.root, text='User Type',font=('goudy old style',15),bg='white').place(x=750,y=220)

        txt_email=Entry(self.root,textvariable=self.var_email,font=('goudy old style',15),
                         bg='lightyellow').place(x=147,y=220)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=('goudy old style',15),
                         bg='lightyellow').place(x=500,y=220)
        self.cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=('Admin','Employee'),
                                state='readonly',justify=CENTER,font=('goudy old style',15))
        self.cmb_utype.place(x=850,y=220,width=200)
        self.cmb_utype.current(0)

        lbl_address=Label(self.root, text='Address',font=('goudy old style',15),bg='white').place(x=50,y=260)
        lbl_salary=Label(self.root, text='Salary',font=('goudy old style',15),bg='white').place(x=750,y=260)
        
        self.txt_address=Text(self.root,font=('goudy old style',15),
                         bg='lightyellow')
        self.txt_address.place(x=147,y=260,width=300,height=100)
        txt_salary=Entry(self.root,textvariable=self.var_salary,font=('goudy old style',15),
                         bg='lightyellow').place(x=850,y=260)

        
        #=====================buttons
        
        btn_add=Button(self.root, text='Save', command=self.add_employee,font=('goudy old style',15),fg='white',bg='#2196f3',
                       cursor='hand2').place(x=500,y=305,width=110,height=28)
        btn_update=Button(self.root,command=self.updates, text='Update',font=('goudy old style',15),fg='white',bg='#4caf50',
                       cursor='hand2').place(x=620,y=305,width=110,height=28)
        btn_delete=Button(self.root,command=self.delete, text='Delete',font=('goudy old style',15),fg='white',bg='#f44336',
                       cursor='hand2').place(x=740,y=305,width=110,height=28)
        btn_clear=Button(self.root, command=self.clear_data, text='Clear',font=('goudy old style',15),fg='white',bg='#607d8b',
                       cursor='hand2').place(x=860,y=305,width=110,height=28)

        
        #============display scrollbar
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=370, relwidth=1, height=150)

        scrolly=Scrollbar(emp_frame, orient=VERTICAL)
        scrollx=Scrollbar(emp_frame, orient=HORIZONTAL)
 
        self.EmployeeTable=ttk.Treeview(emp_frame,yscrollcommand=scrolly.set,xscrollcommand=scrollx.set,
                                        columns=('eid','name','email','gender','contact','dob','doj','pass','utype','address','salary'))

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)
        
        self.EmployeeTable.heading('eid',text='Emp ID')
        self.EmployeeTable.heading('name',text='Name')
        self.EmployeeTable.heading('email',text='Email')
        self.EmployeeTable.heading('gender',text='Gender')
        self.EmployeeTable.heading('contact',text='Contact')
        self.EmployeeTable.heading('dob',text='D.O.B')
        self.EmployeeTable.heading('doj',text='D.O.J')
        self.EmployeeTable.heading('pass',text='Password')
        self.EmployeeTable.heading('utype',text='User Type')
        self.EmployeeTable.heading('address',text='Address')
        self.EmployeeTable.heading('salary',text='Salary')
        self.EmployeeTable['show']='headings'

        self.EmployeeTable.pack(fill=BOTH, expand=1)
        self.EmployeeTable.bind('<ButtonRelease-1>',self.get_data)
        
        self.EmployeeTable.column('eid',width=100)
        self.EmployeeTable.column('name',width=100)
        self.EmployeeTable.column('email',width=100)
        self.EmployeeTable.column('gender',width=100)
        self.EmployeeTable.column('contact',width=100)
        self.EmployeeTable.column('dob',width=100)
        self.EmployeeTable.column('doj',width=100)
        self.EmployeeTable.column('pass',width=100)
        self.EmployeeTable.column('utype',width=100)
        self.EmployeeTable.column('address',width=100)
        self.EmployeeTable.column('salary',width=100)
        #=======================show employees
        db.show_employees(self.EmployeeTable,END,self.root,messagebox)
        
       
#if __name__=='__main__':
#    root=Tk()
#    empl=employeeClass(root)
#    root.mainloop()
