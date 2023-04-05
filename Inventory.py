import tkinter.messagebox
#mysql.connector.connect(host='localhost',user='root',database='inventory')
import sqlite3
from tkinter import*






class product:
    def __init__(self,root):

        p = Database()
        p.conn()

        

#create instances

        

        self.root=root
        self.root.title("Inventory System")
        self.root.geometry("1550x800+0+0")

        pID=StringVar()
        pName=StringVar()
        pPrice=StringVar()
        pQty=StringVar()
        pCompany=StringVar()
        pContact=StringVar()


        def Close():
            print("Product : close method called")
            Close = tkinter.messagebox.askyesno("Inventory System","Do you want to close the system")
            if Close > 0:
                root.destroy()
                print("Product : close method finished\n")
                return
        def clear():
            print("Product : clear method called")
            self.txtpID.delete(0,END)
            self.txtpName.delete(0,END)
            self.txtpPrice.delete(0,END)
            self.txtpQty.delete(0,END)
            self.txtpCompany.delete(0,END)
            self.txtpContact.delete(0,END)
            print("Product : clear method finished\n")
        def insert():
            print("Product : insert method called")
            if (len(pID.get())!=0) :
                p.insert(pID.get(),pName.get(),pQty.get(),pPrice.get(),
                        pCompany.get(),pContact.get())
                productList.delete(0,END)
                productList.insert(END,pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                
                showproducts()
            else:
                tkinter.messagebox.askyesno("Inventory System","Enter product id")
                print("Product : clear method finished")

        def showproducts():
            print("Product: showproducts method  called")
            productList.delete(0,END)
            for row in p.show():
                productList.insert(END ,row,str(""))
            print("Product: showproducts method  finished")


        def productRec(event):
            print("Product: ProductRec method  called")
            global pd
            searchpd = productList.curselection()[0]

            pd = productList.get(searchpd)

            self.txtpID.delete(0,END) 
            self.txtpID.insert(END,pd[0])
            
            self.txtpName.delete(0,END)
            self.txtpName.insert(END,pd[1])
            
            self.txtpPrice.delete(0,END)
            self.txtpPrice.insert(END,pd[2])
            self.txtpQty.delete(0,END)
            self.txtpQty.insert(END,pd[3])
            
            self.txtpCompany.delete(0,END)
            self.txtpCompany.insert(END,pd[4])


            self.txtpContact.delete(0,END)
            self.txtpContact.insert(END,pd[5])

            print('Product : productRec method finished')
            

        def delete():
            print("Product : insert method called")
            if (len(pID.get())!=0) :
                p.delete(pd[0])
                clear()
                showproducts()
            print("Product : insert method finished")

            ''' p.insert(pID.get(),pName.get(),pQty.get(),pPrice.get(),
                        pCompany.get(),pContact.get())
                productList.delete(0,END)
                productList.insert(END,pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get())
                
                showproducts()'''


        def search():
                print("Product : search method called")
                productList.delete(0,END)
                for row in p.search(pID.get(),pName.get(),pQty.get(),pPrice.get(),pCompany.get(),pContact.get()):

                    productList.insert(END,row,str(""))
                print("Product : search method finished")



                    




        MainFrame =Frame(self.root,bg="black")
        MainFrame.grid()

        HeadFrame =Frame(MainFrame,bd=1,padx=50,pady=10,bg='white',relief=RIDGE)
        HeadFrame.pack(side=TOP)

        self.title=Label(HeadFrame,text="Inventory SYSTEM",bg="black",fg="orange",relief=RIDGE,font=("ROBOTO",50,"bold"))
        self.title.grid()

        

        

        OperationalFrame=Frame(MainFrame,bd=1,relief=RIDGE,padx=20,bg="Cyan",width=1550,height=10)
        OperationalFrame.pack(side=BOTTOM)

        BodyFrame=Frame(MainFrame,bd=2,relief=RIDGE,padx=20,bg="Cyan",width=1500,height=400)
        BodyFrame.pack(side=BOTTOM)

        #HeadFrame = Frame(frame,bd=1,padx=50,pady=10,bg='white',relief=RIDGE)
        #HeadFrame.pack(side=TOP)

        #bottomframe=Frame(frame,bd=12,relief=RIDGE,padx=20,pady=20,bg="white",width=1350,height=100)
        #bottomframe.pack(side=BOTTOM)


        


        DataFrameLeft=LabelFrame(BodyFrame,text="BANKING SYSTEM",bg="Cyan",fg="orange",bd=20,relief=RIDGE,font=("ROBOTO",20,))
        DataFrameLeft.place(x=0,y=5,width=700,height=350)



        '''lblMember=Label(DataFrameLeft,bg="white",text="Customer",font=("ROBOTO",15,"bold"),padx=2,pady=6)
        lblMember.grid(row=0,column=0,sticky=W)'''
        self.laelpID=Label(DataFrameLeft,bg="white",fg="blue",text="Product ID",font=("ROBOTO",15,"bold"),padx=2,pady=2)
        self.laelpID.grid(row=0,column=0,sticky=W)

        self.txtpID = Entry (DataFrameLeft,font=('arial',15,"bold"), textvariable=pID, width=35)
        self.txtpID.grid(row=0,column=1,sticky=W)

        self.laelpName=Label(DataFrameLeft,bg="white",fg="blue",text="Product Name",font=("ROBOTO",15,"bold"),padx=2,pady=2)
        self.laelpName.grid(row=1,column=0,sticky=W)

        self.txtpName = Entry (DataFrameLeft,font=('arial',15,"bold"), textvariable=pName, width=35)
        self.txtpName.grid(row=1,column=1,sticky=W)
        
        self.laelpPrice=Label(DataFrameLeft,bg="white",fg="blue",text="Price",font=("ROBOTO",15,"bold"),padx=2,pady=2)
        self.laelpPrice.grid(row=2,column=0,sticky=W)

        self.txtpPrice = Entry (DataFrameLeft,font=('arial',15,"bold"), textvariable=pPrice, width=35)
        self.txtpPrice.grid(row=2,column=1,sticky=W)

        self.laelpQty=Label(DataFrameLeft,bg="white",fg="blue",text="Product Quantity",font=("ROBOTO",15,"bold"),padx=2,pady=2)
        self.laelpQty.grid(row=3,column=0,sticky=W)

        self.txtpQty = Entry (DataFrameLeft,font=('arial',15,"bold"), textvariable=pQty, width=35)
        self.txtpQty.grid(row=3,column=1,sticky=W)

        self.laelpCompany=Label(DataFrameLeft,bg="white",fg="blue",text="Company",font=("ROBOTO",15,"bold"),padx=2,pady=2)
        self.laelpCompany.grid(row=4,column=0,sticky=W)

        self.txtpCompany = Entry (DataFrameLeft,font=('arial',15,"bold"), textvariable=pCompany, width=35)
        self.txtpCompany.grid(row=4,column=1,sticky=W)

        self.laelpContact=Label(DataFrameLeft,bg="white",fg="blue",text="Contact",font=("ROBOTO",15,"bold"),padx=2,pady=2)
        self.laelpContact.grid(row=5,column=0,sticky=W)

        self.txtpContact = Entry (DataFrameLeft,font=('arial',15,"bold"), textvariable=pContact, width=35)
        self.txtpContact.grid(row=5,column=1,sticky=W)

       


        DataFrameRight=LabelFrame(BodyFrame,text="Account Detail",bg="Cyan",fg="orange",bd=20,relief=RIDGE,font=("ROBOTO",20,))
        DataFrameRight.place(x=710,y=5,width=600,height=750)



#===========
        scroll = Scrollbar (DataFrameRight)
        scroll.grid(row=0, column=1,sticky='ns')


        productList=Listbox(DataFrameRight, width=60, height=16, font=('arial',12,'bold'),yscrollcommand=scroll.set) 

        productList.bind ('<<ListboxSelect>>',productRec)
        
        productList.grid(row=0,column=0,padx=8)
        scroll.config(command=productList.yview)
            #======================Button======================
        self.buttonSave = Button(OperationalFrame, text='Save',font=('arial',12,'bold'),height=1,width='10',bd=4,command=insert)
        self.buttonSave.grid(row=0,column=0)

        self.buttonShow = Button(OperationalFrame, text='Show Data',font=('arial',12,'bold'),height=1,width='10',bd=4,command=showproducts)
        self.buttonShow.grid(row=0,column=1)

        self.buttonClear = Button(OperationalFrame, text='Reset',font=('arial',12,'bold'),height=1,width='10',bd=4,command=clear)
        self.buttonClear.grid(row=0,column=2)

        self.buttonDelete = Button(OperationalFrame, text='Delete',font=('arial',12,'bold'),height=1,width='10',bd=4,command=delete)
        self.buttonDelete.grid(row=0,column=3)

        self.buttonSearch = Button(OperationalFrame, text='Search',font=('arial',12,'bold'),height=1,width='10',bd=4,command=search)
        self.buttonSearch.grid(row=0,column=4)

        self.buttonUpdate = Button(OperationalFrame, text='Update',font=('arial',12,'bold'),height=1,width='10',bd=4)
        self.buttonUpdate.grid(row=0,column=5)

        self.buttonClose = Button(OperationalFrame, text='Close',font=('arial',12,'bold'),height=1,width='10',bd=4,command=Close)
        self.buttonClose.grid(row=0,column=6)

        
        connection=Button(root,text='database',width=23,font=("ROBOTO",20),bg="Cyan",fg="orange",bd=28,relief=RIDGE,
        activebackground='blue',activeforeground='white')
        connection.place(x=0,y=0)

    


    

            
    




        #Backend database

class Database:

    def conn(self):

        print("Database: connection called")    
        con = sqlite3.connect ("inventory.db") 
        cur =con.cursor()
             
        query ="create table if not exists product(pid integer primary key,pName text,price text,qty text,company text,contact text)"

        con.execute(query)
        con.commit()
        con.close()
        print("Database: connection finished") 

    def insert(self, pid,name,price,qty,company,contact):
        print("Database: insert method called")    
        con = sqlite3.connect ("inventory.db") 
        cur =con.cursor()
        query="insert into product values(?,?,?,?,?,?)"
        cur.execute(query,(pid,name,price,qty,company,contact))
        con.commit()
        con.close()
        print("Database: insert method finished/n")  
    def show(self):
        print("Database: show method called/n") 
        con = sqlite3.connect ("inventory.db") 
        cur = con.cursor()
        query="select * from product"
        cur.execute(query)
        rows=cur.fetchall()
        con.close()
        print("Database: show method finished/n")  
        return rows

    def delete(self,pid):
        print("Database: delete method called/n") 
        con = sqlite3.connect ("inventory.db") 
        cur = con.cursor()

        cur.execute("delete from product where pid=?",(pid,))
        con.commit()
        con.close()
        print("Database: delete method finished/n")  

    def search(self,pid="",name="",price="",qty="",company="",contact=""):
        print("Database: search method called/n",pid) 
        con = sqlite3.connect ("inventory.db") 
        cur = con.cursor()
        cur.execute("select * from product where pid=? or pname=? or price=? or qty=? or company=? or contact=?",(pid,name,price,qty,company,contact))
        row=cur.fetchall()
        con.close()
        print(pid,"Database:search method finished /n")
        return row

    def update(self,pid="",name="",price="",qty="",company="",contact=""):
        print("Database: update method called/n",pid) 
        con = sqlite3.connect ("inventory.db") 
        cur = con.cursor()
        cur.execute("update product set pid=? or pname=? or price=? or qty=? or company=? contact=? where pid=?"
                    ,(pid,name,price,qty,company,contact,pid))
        con.commit()
        con.colose
        print(pid,"Database:update method finished /n")




       
if __name__ == "__main__":
    root= Tk()
    application = product(root)
    root.mainloop()  




    