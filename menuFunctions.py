from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3


def callmenuFunc(menubar): 

    def showCategories():
        categ = Tk()
        categ.geometry('500x230')
        categ.title("Categories")

        labelframe2 = LabelFrame(categ, text="Income")  
        labelframe2.grid(row=1,column = 3, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = Label(labelframe2, text="Manage Your Categories here")  
        rootlabel.grid()


# ============================= Income-Categories ========================================================
        def AddCategories():
            Ac = Tk()
            Ac.geometry('250x150')
            Ac.title('Add Categories')

            label_1 = Label(Ac, text="Enter Category Name",width=20,font=("bold", 10))
            label_1.pack()

            entry_1 = Entry(Ac, bd=5)
            entry_1.pack()
            
            def addCat():
                s = entry_1.get()
                db = sqlite3.connect('myspendmate.db')
                cursor = db.cursor()
                cursor.execute("insert into incomeCat values('%s')"%(s))
                cursor.close()
                db.commit()
                db.close()
                Acexit()

            def Acexit():
                Ac.destroy()

            savebutton = Button(Ac, text = 'Save and Exit',command = addCat, padx=20, pady=20) 
            savebutton.pack()
            # Ac.destroy()
            

        def GetCategories():
            GetC = Tk()
            frm = Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Category Name")
            # GetC.geometry('1000x100')
            GetC.title("Income Details")
            GetC.resizable(False,False)
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("select * from incomeCat")
            list1 = cursor.fetchall()
            total = cursor.rowcount
            
            for i in list1:
                treev.insert('','end',values=i)

            cursor.close()
            db.commit()
            db.close
            print(list1)
            GetC.mainloop()

            cursor.close()
            db.commit()
            db.close()


        btn1 = Button(labelframe2, text = 'Add Category',command = AddCategories) 
        btn1.grid()
        btn2 = Button(labelframe2, text = 'See all Categories',command = GetCategories) 
        btn2.grid()

# ============================= Expense-Categories ========================================================

        labelframe3 = LabelFrame(categ, text="Expense")  
        labelframe3.grid(row=1,column = 6, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = Label(labelframe3, text="Categories Details")  
        rootlabel.grid()

        def Add():
            Ac = Tk()
            Ac.geometry('250x150')
            Ac.title('Add Categories')

            label_1 = Label(Ac, text="Enter Category Name",width=20,font=("bold", 10))
            label_1.pack()

            entry_1 = Entry(Ac, bd=5)
            entry_1.pack()
            
            def addCat(): 
                s = entry_1.get()
                db = sqlite3.connect('myspendmate.db')
                cursor = db.cursor()
                cursor.execute("insert into expenseCat values('%s')"%(s))
                cursor.close()
                db.commit()
                db.close()
                Acexit()

            def Acexit():
                Ac.destroy()

            savebutton = Button(Ac, text = 'Save and Exit',command = addCat, padx=20, pady=20) 
            savebutton.pack()
            # Ac.destroy()

        def Get():
            GetC = Tk()
            frm = Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Category Name")
            # GetC.geometry('1000x100')
            GetC.title("Income Details")
            GetC.resizable(False,False)
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("select * from expenseCat")
            list1 = cursor.fetchall()
            total = cursor.rowcount
            
            for i in list1:
                treev.insert('','end',values=i)

            cursor.close()
            db.commit()
            db.close
            print(list1)
            GetC.mainloop()

            cursor.close()
            db.commit()
            db.close()

        btn1 = Button(labelframe3, text = 'Add Category',command = Add) 
        btn1.grid()
        btn2 = Button(labelframe3, text = 'See all Categories',command = Get) 
        btn2.grid()

        print("Categories!!!")


# ============================= Set-Currency ========================================================
    def setCurrency():
        print("Set Currency here!")
        Currency = Tk()
        Currency.geometry('500x500')
        Currency.title("Set Currency")

        label_1 = Label(Currency, text="Select Currency",width=20,font=("bold", 10))
        label_1.place(x=80,y=200)

        country_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 

        
        cb = ttk.Combobox(Currency,values=country_list,width=10)
        cb.place(x = 260,y= 200)
        cb.current(0)

        def SaveCurrency():
            print(cb.get()) #  Save this to database
            Currency.destroy()
            messagebox.showinfo("Message","Operation Successful!")  

        savebutton = Button(Currency, text = 'Save and Exit',command = SaveCurrency, padx=20, pady=20) 
        savebutton.place(x = 180, y = 320)
        
# ============================= Account Setup ========================================================
    def AccountSetup():
        print("Account Setup")
        accsetup = Tk()
        # accsetup.geometry('500x230')
        accsetup.title("Accounts")

        labelframe2 = LabelFrame(accsetup, text="Accounts")  
        labelframe2.grid(row=1,column = 3, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = Label(labelframe2, text="Account Details")  
        rootlabel.grid()

        def Add():
            Ac = Tk()
            Ac.geometry('250x150')
            Ac.title('Add Account')

            label_1 = Label(Ac, text="Enter Account Name",width=20,font=("bold", 10))
            label_1.pack()

            entry_1 = Entry(Ac, bd=5)
            entry_1.pack()
            def addCat(): 
                s = entry_1.get()
                db = sqlite3.connect('myspendmate.db')
                cursor = db.cursor()
                cursor.execute("insert into Account values('%s')"%(s))
                cursor.close()
                db.commit()
                db.close()
                Acexit()

            def Acexit():
                Ac.destroy()

            savebutton = Button(Ac, text = 'Save and Exit',command = addCat, padx=20, pady=20) 
            savebutton.pack()

        def Get():
            GetC = Tk()
            frm = Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Account Name")
            # GetC.geometry('1000x100')
            GetC.title("Income Details")
            GetC.resizable(False,False)
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("select * from Account")
            list1 = cursor.fetchall()
            total = cursor.rowcount
            
            for i in list1:
                treev.insert('','end',values=i)

            cursor.close()
            db.commit()
            db.close
            print(list1)
            GetC.mainloop()

            cursor.close()
            db.commit()
            db.close()

        btn1 = Button(labelframe2, text = 'Add Accounts',command = Add) 
        btn1.grid()
        btn2 = Button(labelframe2, text = 'See all Accounts',command = Get) 
        btn2.grid()

# ===================================== Reports ======================================================

    def Reports():
        print("Take Reports here!")

# ============================= Menu-Configs ========================================================
    functionmenu = Menu(menubar, tearoff = 0)
    functionmenu.add_command(label = "Categories",command = showCategories)
    functionmenu.add_command(label = "Set Currency",command = setCurrency)
    functionmenu.add_command(label = "Accounts", command = AccountSetup)
    functionmenu.add_command(label = "Reports", command = Reports)

    menubar.add_cascade(label = "Functions", menu = functionmenu)