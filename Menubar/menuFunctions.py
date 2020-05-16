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
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib
from pylab import title, figure, xlabel, ylabel, xticks, bar, legend, axis, savefig
from fpdf import FPDF
from Main_Window.balance import *
from Main_Window.income import *
from Main_Window.budget import *
from Main_Window.expense import *
from Main_Window.theme import ttk_theme

def callmenuFunc(menubar, root): 

    def showCategories():
        categ = ThemedTk(theme = ttk_theme, themebg = True)
        # categ.geometry('650x230')
        categ.resizable(False, False)
        categ.title("Categories")


# ============================= Income-Categories ========================================================
        labelframe2 = ttk.LabelFrame(categ, text="Income")  
        labelframe2.grid(row=1,column = 3, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Category Details")  
        rootlabel.grid()


        def AddCategories():
            Ac = ThemedTk(theme = ttk_theme, themebg = True)
            # Ac.geometry('250x150')
            Ac.resizable(False, False)
            Ac.title('Add Categories')

            labelframe2 = ttk.LabelFrame(Ac, text="Add Category")  
            labelframe2.grid(row=1,column = 3, rowspan = 2, columnspan=2, sticky='WE', \
                    padx=30, pady=30, ipadx=30, ipady=30)

            label_1 = ttk.Label(labelframe2, text="Enter Category Name",width=20,font=("bold", 10))
            label_1.grid()

            entry_1 = Entry(labelframe2, bd=5)
            entry_1.grid()
            
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

            savebutton = ttk.Button(labelframe2, text = 'Save and Exit',command = addCat) 
            savebutton.grid()
            # Ac.destroy()
            

        def GetCategories():
            GetC = ThemedTk(theme = ttk_theme, themebg = True)
            frm = ttk.Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Category Name")
            # GetC.geometry('250x600')
            GetC.title("Category List")
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
            Ac = ThemedTk(theme = ttk_theme, themebg = True)
            # Ac.geometry('250x150')
            Ac.resizable(False, False)
            Ac.title('Add Categories')

            labelframe2 = ttk.LabelFrame(Ac, text="Add Category")  
            labelframe2.grid(row=1,column = 3, rowspan = 2, columnspan=2, sticky='WE', \
                    padx=30, pady=30, ipadx=30, ipady=30)

            label_1 = ttk.Label(labelframe2, text="Enter Category Name",width=20,font=("bold", 10))
            label_1.grid()

            entry_1 = Entry(labelframe2, bd=5)
            entry_1.grid()
            
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

            savebutton = ttk.Button(labelframe2, text = 'Save and Exit',command = addCat) 
            savebutton.grid()
            # Ac.destroy()

        def Get():
            GetC = ThemedTk(theme = ttk_theme, themebg = True)
            frm = ttk.Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Category Name")
            # GetC.geometry('250x600')
            GetC.title("Category List")
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
        Currency = ThemedTk(theme = ttk_theme, themebg = True)
        Currency.resizable(False, False)
        # Currency.geometry('250x100')
        Currency.title("Set Currency")

        labelframe3 = ttk.LabelFrame(Currency, text="Expense")  
        labelframe3.grid(row=1,column = 6, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe3, text="Categories Details")  
        rootlabel.grid()

        label_1 = ttk.Label(labelframe3, text="Select Currency here",width=20,font=("bold", 10))
        label_1.grid(row = 0, column = 1, pady = 2)

        country_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 
        Symbol = ["₹", "$", "$", "¥", "kr", "€"]
        
        cb = ttk.Combobox(labelframe3,values=country_list,width=10)
        cb.grid(row = 1, column = 1, pady = 2)
        cb.current(0)

        def SaveCurrency():
            getCountry = cb.get()
            index = country_list.index(str(getCountry))
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

        savebutton = ttk.Button(labelframe3, text = 'Save and Exit',command = SaveCurrency) 
        savebutton.grid(row = 2, column = 1, pady = 2)
        
# ============================= Account Setup ========================================================
    def AccountSetup():
        print("Account Setup")
        accsetup = ThemedTk(theme = ttk_theme, themebg = True)
        accsetup.resizable(False, False)
        # accsetup.geometry('500x230')
        accsetup.title("Accounts")

        labelframe2 = ttk.LabelFrame(accsetup, text="Accounts")  
        labelframe2.grid(row=1,column = 2, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Account Details")  
        rootlabel.grid()

        def Add():
            Ac = Tk()
            Ac.resizable(False, False)
            # Ac.geometry('250x150')
            Ac.title('Add Account')

            labelframe2 = ttk.LabelFrame(Ac, text="Add Category")  
            labelframe2.grid(row=1,column = 3, rowspan = 2, columnspan=2, sticky='WE', \
                    padx=30, pady=30, ipadx=30, ipady=30)

            label_1 = ttk.Label(labelframe2, text="Enter Account Name",width=20,font=("bold", 10))
            label_1.grid()

            entry_1 = Entry(labelframe2, bd=5)
            entry_1.grid()

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

            savebutton = ttk.Button(labelframe2, text = 'Save and Exit',command = addCat) 
            savebutton.grid()

        def Get():
            GetC = ThemedTk(theme = ttk_theme, themebg = True)
            frm = ttk.Frame(GetC)
            frm.pack(side=tk.LEFT,padx=20)
            
            treev=ttk.Treeview(frm,columns=(1) ,show="headings", height ='30')
            treev.pack()
            treev.heading(1,text="Account Name")
            # GetC.geometry('250x600')
            GetC.title("Accounts List")
            # GetC.resizable(False,False)
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
        print("Account Setup")
        accsetup = ThemedTk(theme = ttk_theme, themebg = True)
        # accsetup.geometry('500x230')
        accsetup.title("Reports")

        labelframe2 = ttk.LabelFrame(accsetup, text="Reports")  
        labelframe2.grid(row=1,column = 2, rowspan = 2, columnspan=2, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Take your Reports here!", width=20, font=("bold", 10))  
        rootlabel.grid()
        print("Take Reports here!")

        label_1 = ttk.Label(labelframe2, text="Enter Month (1-12): ", width=20, font=("bold", 10))
        label_1.grid(row=2,column = 0, pady=4)

        entry_1 = Entry(labelframe2, bd=5)
        entry_1.grid(row=3,column = 0, pady=4)

        label_2 = ttk.Label(labelframe2, text="Enter Year: ", width=20, font=("bold", 10))
        label_2.grid(row=4,column = 0, pady=4)

        entry_2 = Entry(labelframe2, bd=5)
        entry_2.grid(row=5,column = 0, pady=4)

        label_3 = ttk.Label(labelframe2, text="Name your Report file: ", width=20, font=("bold", 10))
        label_3.grid(row=6,column = 0,columnspan = 2, pady=4)

        entry_3 = Entry(labelframe2, bd=5)
        entry_3.grid(row=7,column = 0, pady=7)

        def Add(): 
            mon = entry_1.get()
            monint = int(mon)
            yr = entry_2.get()
            yrint = int(yr)
            name = entry_3.get()
            conn = sqlite3.connect("myspendmate.db")
            df = pd.read_sql_query("select * from income where month='%s' AND year='%s';"%(mon, yr), conn,)
            print(df)
            df1 = pd.read_sql_query("select * from expense where month='%s' AND year='%s';"%(mon, yr), conn,)
            print(df1)

            np.random.seed(19680801)

            plt.rcdefaults()
            fig, ax = plt.subplots()

            dates = []
            income_cost=[]
            print('monint')
            print(monint)
            if monint == 2:
                if (yrint % 4) == 0 and (yrint % 100) == 0 and (yrint % 400) == 0:
                    days_num = 28
                else:
                    days_num = 29
            elif monint == 1 or monint ==  3 or monint == 5 or monint == 7 or monint == 8 or monint == 10 or monint == 12: 
                days_num = 31
            elif monint == 4 or monint == 6 or monint == 9 or monint == 11:
                days_num = 30
                print('days are 30')
            print(days_num)
            for i in range(days_num):
                dates.append(i+1)
            dates = tuple(dates)

            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            for i in range(days_num):
                val = i+1
                cursor.execute("select sum(amount) from income where day=? AND month=? AND year=?", (val,mon,yr))
                total_income = cursor.fetchone()[0]
                if total_income == None:
                    total_income = 0 
                income_cost.append(total_income)

            y_pos = np.arange(days_num)
            ax.barh(y_pos, income_cost, align='center', alpha =0.5)
            ax.set_yticks(y_pos)
            ax.set_yticklabels(dates)
            ax.invert_yaxis()
            ax.set_ylabel('Date')
            print(income_cost)
            ax.set_xlabel('Income')
            ax.set_title('Day Wise Income')
            plt.savefig('barincome.png',dpi=100)  
            # plt.show()

            # ======================================================================================
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute(" select sum(amount) from income where month='%s' AND year='%s';"%(mon, yr))
            total_expense = cursor.fetchone()[0]
            if total_expense == None:
                total_expense = 0 
            cursor.execute("select * from income where month='%s' AND year='%s';"%(mon, yr))
            expense_list=cursor.fetchall()

            labels = []
            amt_expe = []
            sizes = []
            count = -1

            for i in expense_list:
                category = str(i[3]) 
                print("category " + str(category))   
                amt_category = i[0]
                print("amt of category " + str(amt_category))
                if labels.count(category) == 0:
                    count+=1
                    labels.append(category)
                    amt_expe.append(amt_category)
                    sizes.append(float((amt_category*100)/total_expense))   
                else:
                    ppcount = labels.index(category)
                    amt_expe[ppcount] = amt_expe[ppcount] + amt_category
                    sizes[ppcount] = float((amt_expe[ppcount]*100)/total_expense)

            tobe = sizes.index(max(sizes))
            print('tobe is : ' + str(tobe))
            explode = []
            for i in range(count+1):
                if i == tobe:
                    explode.append(0.1)  
                else:
                    explode.append(0)
            explode = tuple(explode)
            print('label ' + str(labels))
            print('amt ' + str(amt_expe))
            print('sizes ' + str(sizes))
            print('explode ' + str(explode))

            # Plot
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.set_title('Category Wise Analysis of Income')
            plt.savefig('pieincome.png',dpi=100)
            # plt.show()
            # ==========================================================================================

            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute(" select sum(amount) from expense where month='%s' AND year='%s';"%(mon, yr))
            total_expense = cursor.fetchone()[0]
            if total_expense == None:
                total_expense = 0 
            cursor.execute("select * from expense where month='%s' AND year='%s';"%(mon, yr))
            expense_list=cursor.fetchall()

            labels = []
            amt_expe = []
            sizes = []
            count = -1

            for i in expense_list:
                category = str(i[3]) 
                print("category " + str(category))   
                amt_category = i[0]
                print("amt of category " + str(amt_category))
                if labels.count(category) == 0:
                    count+=1
                    labels.append(category)
                    amt_expe.append(amt_category)
                    sizes.append(float((amt_category*100)/total_expense))   
                else:
                    ppcount = labels.index(category)
                    amt_expe[ppcount] = amt_expe[ppcount] + amt_category
                    sizes[ppcount] = float((amt_expe[ppcount]*100)/total_expense)

            tobe = sizes.index(max(sizes))
            print('tobe is : ' + str(tobe))
            explode = []
            for i in range(count+1):
                if i == tobe:
                    explode.append(0.1)  
                else:
                    explode.append(0)
            explode = tuple(explode)
            print('label ' + str(labels))
            print('amt ' + str(amt_expe))
            print('sizes ' + str(sizes))
            print('explode ' + str(explode))

            # Plot
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax1.set_title('Category Wise Analysis of Expense')
            plt.savefig('pieexpense.png',dpi=100)
            # plt.show()

            # ==================================================================================

            plt.rcdefaults()
            fig, ax = plt.subplots()

            dates = []
            expense_cost=[]
            print('days')
            print(days_num)
            for i in range(days_num):
                dates.append(i+1)
            dates = tuple(dates)

            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            for i in range(days_num):
                val = i+1
                cursor.execute("select sum(amount) from expense where day=? AND month=? AND year=?", (val,mon,yr))
                total_income = cursor.fetchone()[0]
                if total_income == None:
                    total_income = 0 
                expense_cost.append(total_income)

            y_pos = np.arange(days_num)
            ax.barh(y_pos, expense_cost, align='center', alpha =0.5)
            ax.set_yticks(y_pos)
            ax.set_yticklabels(dates)
            ax.invert_yaxis()
            ax.set_ylabel('Date')
            ax.set_xlabel('Expense')
            ax.set_title('Day Wise Expense')
            plt.savefig('barexpense.png',dpi=100)  
            # plt.show()
            # =========================================================================================
                
            mon_name = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

            # ==========================================================================================
            pdf = FPDF()
            pdf.add_page()
            pdf.set_xy(0, 0)
            pdf.set_font('arial', 'B', 12) 
            pdf.cell(60)
            pdf.cell(75, 10, " ", 0, 2, 'C')
            pdf.cell(90, 3, " ", 0, 2, 'C')
            pdf.cell(75, 10, "SpendMate - Your Money Manager", 0, 2, 'C')
            pdf.cell(90, 3, " ", 0, 2, 'C')
            pdf.cell(75, 10, "A Tabular and Graphical Report of Income for "+ str(mon_name[int(mon)-1]) + " " + str(yr), 0, 2, 'C')
            pdf.cell(90, 5, " ", 0, 2, 'C')
            pdf.cell(-40)
            pdf.cell(20, 10, 'amount', 1, 0, 'C')
            pdf.cell(30, 10, 'date', 1, 0, 'C')
            pdf.cell(75, 10, 'description', 1, 0, 'C')
            pdf.cell(30, 10, 'category', 1, 0, 'C')
            pdf.cell(30, 10, 'account_type', 1, 2, 'C')
            pdf.cell(-155)
            pdf.set_font('arial', '', 12)
            for i in range(0, len(df)):
                pdf.cell(20, 10, '%s' % (df['amount'].iloc[i]), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (str(df.date.iloc[i])), 1, 0, 'C')
                pdf.cell(75, 10, '%s' % (str(df.description.iloc[i])), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (str(df.category.iloc[i])), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (str(df.account_type.iloc[i])), 1, 2, 'C')
                pdf.cell(-155)
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.cell(-20)
            pdf.image('pieincome.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.cell(-5)
            pdf.image('barincome.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
            # ======================================================================================

            pdf.add_page()
            pdf.set_font('arial', 'B', 12)
            pdf.cell(45)
            pdf.cell(90, 3, " ", 0, 2, 'C')
            pdf.cell(75, 10, "A Tabular and Graphical Report of Expense for "+ str(mon_name[int(mon)-1])+ " " + str(yr), 0, 2, 'C')
            pdf.cell(90, 5, " ", 0, 2, 'C')
            pdf.cell(-40)
            pdf.cell(20, 10, 'amount', 1, 0, 'C')
            pdf.cell(30, 10, 'date', 1, 0, 'C')
            pdf.cell(75, 10, 'description', 1, 0, 'C')
            pdf.cell(30, 10, 'category', 1, 0, 'C')
            pdf.cell(30, 10, 'account_type', 1, 2, 'C')
            pdf.cell(-155)
            pdf.set_font('arial', '', 12)
            for i in range(0, len(df1)):
                pdf.cell(20, 10, '%s' % (df1['amount'].iloc[i]), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (str(df1.date.iloc[i])), 1, 0, 'C')
                pdf.cell(75, 10, '%s' % (str(df1.description.iloc[i])), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (str(df1.category.iloc[i])), 1, 0, 'C')
                pdf.cell(30, 10, '%s' % (str(df1.account_type.iloc[i])), 1, 2, 'C')
                pdf.cell(-155)
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.cell(-20)
            pdf.image('pieexpense.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
            pdf.cell(90, 10, " ", 0, 2, 'C')
            pdf.cell(-5)
            pdf.image('barexpense.png', x = None, y = None, w = 0, h = 0, type = '', link = '')
            print('name---------------------------' + str(name))
            pdf.output('{}.pdf'.format(name), 'F')
            messagebox.showinfo("Success!!","Your Report have been saved in Root Directory.\nCheck it out!!")
            Acexit()

        def Acexit():
            accsetup.destroy()

        btn1 = ttk.Button(labelframe2, text = 'Get Report!',command = Add) 
        btn1.grid(row=8,column = 0, pady=4)
        # pass

# ============================= Menu-Configs ========================================================
    functionmenu = Menu(menubar, tearoff = 0, activeborderwidth = 3, bd = 3)
    functionmenu.add_command(label = "Categories",command = showCategories)
    functionmenu.add_command(label = "Set Currency",command = setCurrency)
    functionmenu.add_command(label = "Accounts", command = AccountSetup)
    functionmenu.add_command(label = "Reports", command = Reports)

    menubar.add_cascade(label = "Functions", menu = functionmenu)