from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import PIL.Image
import sqlite3
from Main_Window.balance import *
from Main_Window.Currency import *
from Main_Window.theme import ttk_theme
from ttkthemes import ThemedTk

db = sqlite3.connect('myspendmate.db')
cursor = db.cursor()
cursor.execute("select sum(amount) from income")
sum1 = cursor.fetchone()[0]
if(sum1=='None'):
    sum1=str(0)

print(sum1)
cursor.close()
db.commit()
db.close()
date_selected=None

def callincome(root):
    labelframe2 = ttk.LabelFrame(root, text="Income Section")  
    labelframe2.grid(row=1,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)

    CurrencyCurrent = CurrentCurrr()
    rootlabel = ttk.Label(labelframe2, text="Total Income : ")  
    rootlabel.grid(row=1, column = 0)
    rootlabel.configure(anchor="center")
    rootlabel1 = ttk.Label(labelframe2, text= str(sum1) + CurrencyCurrent)  
    rootlabel1.config(font=("Courier", 13))  
    rootlabel1.grid(row=1, column = 1)
    rootlabel1.configure(anchor="center")

    def AddIncome():
        income = ThemedTk(theme = ttk_theme, themebg = True)
        income.title("Add Income")
        print("Inside Button add income-------------------------")
        income.resizable(False, False)
        
        labelframe_2 = ttk.LabelFrame(income, text="Add Income Entry")  
        labelframe_2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe_2, text="Enter the following fields ", width=30, font=("bold", 10))  
        rootlabel.grid(row=2,column = 0,columnspan = 4,padx = 10, pady=4)

        label_1 = ttk.Label(labelframe_2, text="Enter Amount ",width=30,font=("bold", 10))
        label_1.grid(row=3,column = 0,columnspan = 4, pady=4)

        entry_1 = Entry(labelframe_2, bd=5)
        entry_1.grid(row=3,column = 4, pady=4)

        def printamount():
            s = entry_1.get()
            print("s")
            print(s)
            print(type(s))
            if s.isdigit():
                print('Amount: ' + s)
                return s
            else:
                messagebox.showinfo("Attention!","Amount Should be a number and not text or any Special Character!\nEntry Not Saved. Try Again!")
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"

            
        label_2 = ttk.Label(labelframe_2, text="Select Date",width=30,font=("bold", 10))
        label_2.grid(row=4,column = 0,columnspan = 4, pady=4)
        
    
        def dateSelector():
                
            def print_sel():
                global date_selected 
                dateselected = cal.selection_get()
                date_selected=dateselected
                print(dateselected)
                date = str(dateselected)
                print(date[6])
                labelstatus = ttk.Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                label_3 = ttk.Label(labelframe_2, text=dateselected,width=30,font=("bold", 10))
                label_3.grid(row=4,column = 6, pady=4)
                date = str(cal.selection_get())
                top.destroy()
                    
                    

            top = Toplevel(income)
            import datetime
            today = datetime.date.today()

            mindate = datetime.date(year=2000, month=5, day=1)
            maxdate = today + datetime.timedelta(days=5)
                # print(mindate, maxdate)

            cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            cursor="hand1", year=2020, month=5, day=5)
            cal.pack(fill="both", expand=True)
            incomebtn2 = ttk.Button(top, text="Select", command=print_sel).pack() 
            print("Date_new:"+str(date_selected))
            return date_selected
                # tk.top.destroy()



        incomebtn = ttk.Button(labelframe_2, text='Enter Date', command = dateSelector)
        incomebtn.grid(row=4,column = 4, pady=4)

        label_1 = ttk.Label(labelframe_2, text="Description (Max Char = 32)",width=30,font=("bold", 10))
        label_1.grid(row=5,column = 0,columnspan = 4, pady=4)

        entry_2 = Entry(labelframe_2, bd=5)
        entry_2.grid(row=5,column = 4, pady=4)

        def printdescription():
            s2 = entry_2.get()
            desc = str(entry_2.get())
            print('Description: ' + s2)
            return s2

        label_1 = ttk.Label(labelframe_2, text="Category",width=30,font=("bold", 10))
        label_1.grid(row=6,column=0,columnspan = 4, pady=4)

        def printcategory():
            print('Category: ' + cb.get())
            return cb.get()

        db = sqlite3.connect('myspendmate.db')
        cursor = db.cursor()
        cursor.execute("select * from incomeCat")
        cat_list=cursor.fetchall()
        print("-------------incomeCat--------------")
        print(cat_list)
        Category = []
        for i in cat_list:
            Category.append(i[0])
        cb = ttk.Combobox(labelframe_2,values=Category,width=10)
        cb.grid(row=6,column = 4, pady=4)
        cb.current(0)

        label_1 = ttk.Label(labelframe_2, text="Account",width=30,font=("bold", 10))
        label_1.grid(row=7,column = 0,columnspan = 4, pady=10)
        
        def printaccount():
            print('Account: ' + accountbox.get())
            return accountbox.get()
        db = sqlite3.connect('myspendmate.db')
        cursor = db.cursor()
        cursor.execute("select * from Account")
        acc_list=cursor.fetchall()

        Account = []
        for i in acc_list:
            Account.append(i[0])
        accountbox = ttk.Combobox(labelframe_2,values=Account,width=10)
        accountbox.grid(row=7,column = 4, pady=10)
        accountbox.current(0)

        def put():
            t1 = printamount()
            if t1 == "stop":
                return "stopped"
            t2 = str(printdescription())
            t3 = str(printcategory())
            t4 = str(printaccount())
            t5 = str(date_selected)
            if date_selected == None:
                messagebox.showinfo("Attention!","Date Field Should be not be empty.\nEntry Not Saved.\nPlease Select the Date and Try Again!")
                return "stopped"
            print('date selected :' + str(t5))
            info = str(t5)
            day = info[8]+info[9]
            mon = info[5]+info[6]
            yr = info[0]+info[1]+info[2]+info[3]
            print('day: ' + str(day))
            print('mon: ' + str(mon))
            print('yr: ' + str(yr))
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("insert into income values('%d','%s','%s','%s','%s','%d','%d','%d')"%(int(t1),t5,t2,t3,t4,int(day),int(mon),int(yr)))
            cursor.execute("select sum(amount) from income")
            sum1 = cursor.fetchone()[0]
            if(sum1=='None'):
                sum1=str(0)
            rootlabel1.config(text=str(sum1) + CurrencyCurrent)
            cursor.close()
            db.commit()
            db.close
            callbalance(root)
            return "done"
            

        def incomeexit():
            income.destroy()

        def AllinOne():
            status = put()
            if status == "done":
                messagebox.showinfo("Success!!","Income Entry have been saved")
            incomeexit()
            pass 

        savebutton = ttk.Button(labelframe_2, text = 'Save and Exit',command = AllinOne) 
        savebutton.grid(row=8,column = 0,columnspan = 6, pady=4)
    


    def GetData():
        income1 = ThemedTk(theme = ttk_theme, themebg = True)
        frm = ttk.Frame(income1)
        frm.pack(side=tk.LEFT,padx=20)
        
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5) ,show="headings", height ='30')
        tv.pack()
        tv.heading(1,text="Amount")
        tv.heading(2,text="Date")
        tv.heading(3,text="Description")
        tv.heading(4,text="Category")
        tv.heading(5,text="Account_type")
        # income1.geometry('1000x500')
        income1.title("Income Details")
        db = sqlite3.connect('myspendmate.db')
        cursor = db.cursor()
        cursor.execute("SELECT amount,date,description,category,account_type FROM income ")
        list1 = cursor.fetchall()
        total = cursor.rowcount
         
        for i in list1:
            tv.insert('','end',values=i)

        cursor.close()
        db.commit()
        db.close
        print(list1)
        income1.mainloop()

    # -------------------------Income Main window Section---------------------
      

    btn1 = ttk.Button(labelframe2, text = 'Add Income',command = AddIncome) 
    btn1.grid(row = 2, column = 1, pady=4)
    # btn1.configure(anchor="center")
    btn2 = ttk.Button(labelframe2, text = 'Income Details',command = GetData) 
    btn2.grid(row = 3, column = 1, pady=4)
    # btn2.configure(anchor="center")
