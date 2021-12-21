import sqlite3

class DatabaseConnection:
    def __init__(self):
        self.create_db()
    def create_db(self):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS employees(
                  eid INTEGER PRIMARY KEY AUTOINCREMENT,
                  name text,
                  email text,
                  gender text,
                  contact text,
                  dob text,
                  doj text,
                  pass text,
                  utype text,
                  address text,
                  salary INTEGER
                  )""")
        c.execute("""CREATE TABLE IF NOT EXISTS product(
                  pid INTEGER PRIMARY KEY AUTOINCREMENT,
                  Category text,
                  Supplier text,
                  name text,
                  price text,
                  quantity text,
                  status text
                  )""")
        self.con.commit()

    def add_employees(self,eid,gender,contact,name,dob,doj,email,password,utype,address,salary):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        c.execute("""INSERT INTO employees 
                (eid,gender,contact,name,dob,doj,email,pass,utype,address,salary) 
                values (?,?,?,?,?,?,?,?,?,?,?)""",
                (eid,
                gender,
                contact,
                name,
                dob,
                doj,
                email,
                password,
                utype,
                address,
                salary,))

        self.con.commit()
        self.number_of_emp()

    def show_employees(self,table,e,root,messagebox):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute("SELECT *FROM employees")
            rows=c.fetchall()
            table.delete(*table.get_children())
            rows.reverse()
            for row in rows:
                table.insert('',e, values=row)
            self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error','Error due to: {str(ex)}', parent=root)



    def update(self,eid,gender,contact,name,dob,doj,email,password,utype,address,salary,messagebox,root):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            if eid!='':
                if eid!=None:
                    c.execute("""UPDATE employees SET
                            gender=?,contact=?,name=?,dob=?,doj=?,email=?,pass=?,utype=?,address=?,salary=?
                            WHERE eid=? 
                            """,
                            (gender,
                            contact,
                            name,
                            dob,
                            doj,
                            email,
                            password,
                            utype,
                            address,
                            salary,
                             eid,))
                    messagebox.showinfo('Success','Employee Updated Successfully',parent=root) 
                else:
                    messagebox.showerror('Error','Invalid Employee ID', parent=root)
            else:
                messagebox.showerror('Error','Employee ID is requied',parent=root)
            self.con.commit()
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')
       
    def delete(self,eid,messagebox,root,name):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute('SELECT * FROM employees WHERE eid=?',(eid,))
            row=c.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Employee ID',parent=root)
            else:
                confirm=messagebox.askyesno('Delete',f'Are you sure you want to delete:\nEmployeeID: {eid}\nName: {name}',parent=root)
                if confirm==True:
                    c.execute('DELETE FROM employees WHERE eid=?',(eid,))
                    self.con.commit()
                    messagebox.showinfo('Delete','Employee Deleted Successfully',parent=root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}', parent=root)

    def search(self,option,messagebox,root,search_txt,e,table):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            if option=='Select':
                messagebox.showerror('Error','Select Search by Option', parent=root)
            elif search_txt=='':
                messagebox.showerror('Error','Search input is Required')
            else:
                c.execute("SELECT *FROM employees WHERE "+option+" LIKE '%"+search_txt+"%'")
                rows=c.fetchall()
                if len(rows)!=0:
                    table.delete(*table.get_children())
                    for row in rows:
                        table.insert('',e, values=row)
                else:
                    messagebox.showerror('Error','No Record Found!!!',parent=root)
                self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}')

    def number_of_emp(self):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute("SELECT *FROM employees WHERE utype=?",('Employee',))
            rows=c.fetchall()
            if len(rows)!=0:
                return str(len(rows))
            else:
                return 0
            self.con.commit()
        except Exception as ex:
            print('Error',f'Error due to: {str(ex)}')


#===================================suppliers
    def create_db_supplier(self):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS suppliers(
                  invoice INTEGER PRIMARY KEY AUTOINCREMENT,
                  name text,
                  contact text,
                  description text
                  )""")
        self.con.commit()
        
    def add_suppliers(self,invoice,name,contact,description):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()

        c.execute("""INSERT INTO suppliers 
                (invoice,name,contact,description) 
                values (?,?,?,?)""",
                (invoice,
                name,
                contact,
                description,
                ))
        self.con.commit()

    def show_suppliers(self,table,e,root,messagebox):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute("SELECT *FROM suppliers")
            rows=c.fetchall()
            table.delete(*table.get_children())
            rows.reverse()
            for row in rows:
                table.insert('',e, values=row)
            self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error','Error due to: {str(ex)}', parent=root)

        

    def update_suppliers(self,invoice,name,contact,desc,messagebox,root):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            if invoice!='':
                if invoice!=None:
                    c.execute("""UPDATE suppliers SET
                            name=?,contact=?,description=?
                            WHERE invoice=? 
                            """,
                            (name,
                            contact,
                            desc,
                            invoice,
                           ))
                    messagebox.showinfo('Success','Employee Updated Successfully',parent=root)
                else:
                    messagebox.showerror('Error','Invalid Employee ID', parent=root)
            else:
                messagebox.showerror('Error','Employee ID is requied',parent=root)
            self.con.commit()
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')

    def delete_suppliers(self,invoice,messagebox,root,name):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute('SELECT * FROM suppliers WHERE invoice=?',(invoice,))
            row=c.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Supplier ID',parent=root)
            else:
                confirm=messagebox.askyesno('Delete',f'Are you sure you want to delete:\nInvoice No.: {invoice}\nName: {name}',parent=root)
                if confirm==True:
                    c.execute('DELETE FROM suppliers WHERE invoice=?',(invoice,))
                    self.con.commit()
                    messagebox.showinfo('Delete','Supplier Deleted Successfully',parent=root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}', parent=root)

    def search_suppliers(self,messagebox,root,search_txt,e,table):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            if search_txt=='':
                messagebox.showerror('Error','Invoice Number is Required', parent=root)
            else:
                c.execute("SELECT *FROM suppliers WHERE invoice=?",(search_txt,))
                row=c.fetchone()
                if row!=None:
                    table.delete(*table.get_children())
                    table.insert('',e, values=row)
                else:
                    messagebox.showerror('Error','No Record Found!!!',parent=root)
                self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}')


#=================================================categories
    def create_db_category(self):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS categories(
                  cid INTEGER PRIMARY KEY AUTOINCREMENT,
                  name text
                  )""")
        self.con.commit()

    def add_category(self,name):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()

        c.execute("""INSERT INTO categories (name) values (?)""",(name,))
        self.con.commit()

    def show_category(self,table,e,root,messagebox):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute("SELECT *FROM categories")
            rows=c.fetchall()
            table.delete(*table.get_children())
            rows.reverse()
            for row in rows:
                table.insert('',e, values=row)
            self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error','Error due to: {str(ex)}', parent=root)

        

    def update_category(self,name,cat_id,messagebox,root):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            if name!='':
                if name!=None:
                    c.execute("""UPDATE categories SET
                            name=? WHERE cid=? """,(name,cat_id,))
                    messagebox.showinfo('Success','Category Updated Successfully',parent=root)
                else:
                    messagebox.showerror('Error','Invalid Category Name', parent=root)
            else:
                messagebox.showerror('Error','Category name is requied',parent=root)
            self.con.commit()
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')

    def delete_category(self,messagebox,root,name):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute('SELECT * FROM categories WHERE name=?',(name,))
            row=c.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Employee name',parent=root)
            else:
                confirm=messagebox.askyesno('Delete',f'Are you sure you want to delete:\nName: {name}',parent=root)
                if confirm==True:
                    c.execute('DELETE FROM categories WHERE name=?',(name,))
                    self.con.commit()
                    messagebox.showinfo('Delete','Category Deleted Successfully',parent=root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}', parent=root)

#=========================================sales++++++++

    #def create_db_product(self):
     #   self.con=sqlite3.connect(database=r'ims.db')
      #  c=self.con.cursor()
       # c.execute("""CREATE TABLE IF NOT EXISTS product(
        #          pid INTEGER PRIMARY KEY AUTOINCREMENT,
         #         Category text,
          #        Supplier text,
           #       name text,
            ##     quantity text,
              #    status text
               #   )""")
        #self.con.commit()
    def show_category_sales(self,messagebox,root):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute("SELECT name FROM categories")
            rows=c.fetchall()
            rows.insert(0,'Select')
            self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error','Error due to: {str(ex)}', parent=root)
        return  rows

    def show_sales_suppliers(self,root,messagebox):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            sup=['Select']
            c.execute("SELECT name FROM suppliers")
            rows=c.fetchall()
            for i in range(len(rows)):
                sup.append(rows[i][0])
            self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error','Error due to: {str(ex)}', parent=root)
        return sup



    def add_product(self,cat,sup,name,price,qty,status):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        c.execute("""INSERT INTO product 
                (Category,Supplier,name,price,quantity,status) 
                values (?,?,?,?,?,?)""",
                (cat,
                sup,
                name,
                price,
                qty,
                status,))

        self.con.commit()
        

    def show_product(self,table,e,root,messagebox):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute("SELECT *FROM product")
            rows=c.fetchall()
            table.delete(*table.get_children())
            rows.reverse()
            for row in rows:
                table.insert('',e, values=row)
            self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error','Error due to: {str(ex)}', parent=root)



    def update_product(self,cat,sup,name,price,qty,status,pid,messagebox,root):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            if pid!='':
                if pid!=None:
                    c.execute("""UPDATE product SET
                            Category=?,Supplier=?,name=?,price=?,quantity=?,status=?
                            WHERE pid=? 
                            """,
                            (cat,
                            sup,
                            name,
                            price,
                            qty,
                            status,
                            pid,
                            ))
                    messagebox.showinfo('Success','Product Updated Successfully',parent=root) 
                else:
                    messagebox.showerror('Error','Invalid Product ID', parent=root)
            else:
                messagebox.showerror('Error','Product ID is requied',parent=root)
            self.con.commit()
        except Exception as e:
            messagebox.showerror('Error',f'Error due to: {str(e)}')
       
    def delete_product(self,name,messagebox,root):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute('SELECT name FROM product WHERE name=?',(name,))
            row=c.fetchone()
            if row==None:
                messagebox.showerror('Error','Invalid Product Name',parent=root)
            else:
                confirm=messagebox.askyesno('Delete',f'Are you sure you want to delete:\nProduct name: {name}',parent=root)
                if confirm==True:
                    c.execute('DELETE FROM product WHERE name=?',(name,))
                    self.con.commit()
                    messagebox.showinfo('Delete','Product Deleted Successfully',parent=root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}', parent=root)

    def search(self,option,messagebox,root,search_txt,e,table):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            if option=='Select':
                messagebox.showerror('Error','Select Search by Option', parent=root)
            elif search_txt=='':
                messagebox.showerror('Error','Search input is Required')
            else:
                c.execute("SELECT *FROM product WHERE "+option+" LIKE '%"+search_txt+"%'")
                rows=c.fetchall()
                if len(rows)!=0:
                    table.delete(*table.get_children())
                    for row in rows:
                        table.insert('',e, values=row)
                else:
                    messagebox.showerror('Error','No Record Found!!!',parent=root)
                self.con.commit()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to: {str(ex)}')

    def number_of_emp(self):
        self.con=sqlite3.connect(database=r'ims.db')
        c=self.con.cursor()
        try:
            c.execute("SELECT *FROM employees WHERE utype=?",('Employee',))
            rows=c.fetchall()
            if len(rows)!=0:
                return str(len(rows))
            else:
                return 0
            self.con.commit()
        except Exception as ex:
            print('Error',f'Error due to: {str(ex)}')



