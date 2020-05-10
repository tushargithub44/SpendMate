from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import PIL.Image
import sqlite3
from Main_Window.balance import *
from Main_Window.income import *
from Main_Window.budget import *
from Main_Window.expense import *

def callmenuFunc(menubar, root): 

    def showCategories():
        categ = ThemedTk(theme = "xpnative", themebg = True)
        categ.geometry('650x230')
        categ.title("Categories")


# ============================= Income-Categories ========================================================
        labelframe2 = ttk.LabelFrame(categ, text="Income")  
        labelframe2.grid(row=1,column = 3, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Category Details")  
        rootlabel.grid()


        def AddCategories():
            Ac = ThemedTk(theme = "xpnative", themebg = True)
            Ac.geometry('250x150')
            Ac.title('Add Categories')

            label_1 = ttk.Label(Ac, text="Enter Category Name",width=20,font=("bold", 10))
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

            savebutton = ttk.Button(Ac, text = 'Save and Exit',command = addCat) 
            savebutton.pack(padx=20, pady=20)
            # Ac.destroy()
            

        def GetCategories():
            GetC = ThemedTk(theme = "xpnative", themebg = True)
            frm = ttk.Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Category Name")
            GetC.geometry('250x600')
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


        btn1 = ttk.Button(labelframe2, text = 'Add Category',command = AddCategories) 
        btn1.grid(row=2,column = 3, pady = 4)
        btn2 = ttk.Button(labelframe2, text = 'See all Categories',command = GetCategories) 
        btn2.grid(row=3,column = 3, pady = 4)

# ============================= Expense-Categories ========================================================

        labelframe3 = ttk.LabelFrame(categ, text="Expense")  
        labelframe3.grid(row=1,column = 6, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe3, text="Categories Details")  
        rootlabel.grid()

        def Add():
            Ac = ThemedTk(theme = "xpnative", themebg = True)
            Ac.geometry('250x150')
            Ac.title('Add Categories')

            label_1 = ttk.Label(Ac, text="Enter Category Name",width=20,font=("bold", 10))
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

            savebutton = ttk.Button(Ac, text = 'Save and Exit',command = addCat) 
            savebutton.pack(padx=20, pady=20)
            # Ac.destroy()

        def Get():
            GetC = ThemedTk(theme = "xpnative", themebg = True)
            frm = ttk.Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Category Name")
            GetC.geometry('250x600')
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

        btn1 = ttk.Button(labelframe3, text = 'Add Category',command = Add) 
        btn1.grid(row=2,column = 6, pady = 4)
        btn2 = ttk.Button(labelframe3, text = 'See all Categories',command = Get) 
        btn2.grid(row=3,column = 6, pady = 4)

        print("Categories!!!")


# ============================= Set-Currency ========================================================
    def setCurrency():
        print("Set Currency here!")
        Currency = ThemedTk(theme = "xpnative", themebg = True)
        Currency.geometry('250x100')
        Currency.title("Set Currency")

        label_1 = ttk.Label(Currency, text="Select Currency here",width=20,font=("bold", 10))
        label_1.grid(row = 0, column = 1, pady = 2)

        country_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 
        Symbol = ["₹", "$", "$", "¥", "kr", "€"]
        
        cb = ttk.Combobox(Currency,values=country_list,width=10)
        cb.grid(row = 1, column = 1, pady = 2)
        cb.current(0)

        def SaveCurrency():
            getCountry = cb.get()
            index = country_list.index(str(getCountry))
            # print("country: " + str(cb.get()))
            # print("index : " + str(index))
            # print("Symbol: " + str(Symbol[index]))
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("select * from Currency")
            PreviousCurr = str(cursor.fetchone()[0])
            Latest = (Symbol[index])
            cursor.execute("update Currency set Symbol=? where Symbol=?" , (Latest, PreviousCurr))
            cursor.close()
            db.commit()
            db.close()
            Currency.destroy()
            messagebox.showinfo("Message","Operation Successful!")
            callbalance(root)
            callincome(root)
            callExpense(root)
            callBudget(root)

        savebutton = ttk.Button(Currency, text = 'Save and Exit',command = SaveCurrency) 
        savebutton.grid(row = 2, column = 1, pady = 2)
        
# ============================= Account Setup ========================================================
    def AccountSetup():
        print("Account Setup")
        accsetup = ThemedTk(theme = "xpnative", themebg = True)
        # accsetup.geometry('500x230')
        accsetup.title("Accounts")

        labelframe2 = ttk.LabelFrame(accsetup, text="Accounts")  
        labelframe2.grid(row=1,column = 2, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Account Details")  
        rootlabel.grid()

        def Add():
            Ac = Tk()
            Ac.geometry('250x150')
            Ac.title('Add Account')

            label_1 = ttk.Label(Ac, text="Enter Account Name",width=20,font=("bold", 10))
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

            savebutton = ttk.Button(Ac, text = 'Save and Exit',command = addCat) 
            savebutton.pack(padx=20, pady=20)

        def Get():
            GetC = ThemedTk(theme = "xpnative", themebg = True)
            frm = ttk.Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Account Name")
            GetC.geometry('250x600')
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

        btn1 = ttk.Button(labelframe2, text = 'Add Accounts',command = Add) 
        btn1.grid(row=2,column = 1, pady=4)
        btn2 = ttk.Button(labelframe2, text = 'See all Accounts',command = Get) 
        btn2.grid(row=3,column = 1)

# ===================================== Reports ======================================================

    def Reports():
        print("Take Reports here!")

# ============================= Menu-Configs ========================================================
    functionmenu = Menu(menubar, tearoff = 0, activeborderwidth = 3, bd = 3)
    functionmenu.add_command(label = "Categories",command = showCategories)
    functionmenu.add_command(label = "Set Currency",command = setCurrency)
    functionmenu.add_command(label = "Accounts", command = AccountSetup)
    functionmenu.add_command(label = "Reports", command = Reports)

    menubar.add_cascade(label = "Functions", menu = functionmenu)