from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import PIL.Image
import matplotlib.pyplot as plt
import sqlite3
from Main_Window.Currency import *
from Main_Window.balance import *
from Main_Window.budget import *
from Main_Window.theme import ttk_theme


db = sqlite3.connect('myspendmate.db')
cursor = db.cursor()
cursor.execute("select sum(amount) from expense")
sum1 = cursor.fetchone()[0]
if(sum1=='None'):
    sum1=str(0)
print(sum1)
cursor.close()
db.commit()
db.close()
date_selected=None

def callExpense(root):
    labelframe1 = ttk.LabelFrame(root, text="Expense Section")  
    labelframe1.grid(row=1,column = 6, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30) 

    rootlabel = ttk.Label(labelframe1, text="Total Expense : ")  
    rootlabel.grid()  
    CurrencyCurrent = CurrentCurrr()
    rootlabel.grid(row=1, column = 0)
    rootlabel1 = ttk.Label(labelframe1, text= str(sum1) + CurrencyCurrent)  
    rootlabel1.config(font=("Courier", 13))  
    rootlabel1.grid(row=1, column = 1)

    
    def AddExpense():
        expense = ThemedTk(theme = ttk_theme, themebg = True)
        expense.title("Add Expense")
        expense.resizable(False, False)
        labelframe_2 = ttk.LabelFrame(expense, text="Add Expense Entry")  
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
                    labelstatus = ttk.Label(top, text="****Close this window.",width=20,font=("bold", 12)).grid(column = 0)
                    label_3 = ttk.Label(labelframe_2, text=dateselected,width=30,font=("bold", 10))
                    label_3.grid(row=4,column = 6, pady=4)
                    top.destroy()
                    # cal.see(datetime.date(year=2020, month=2, day=5))
                    return dateselected

                top = Toplevel(expense)
                # top.geometry('500x500')
                import datetime
                today = datetime.date.today()

                mindate = datetime.date(year=2000, month=1, day=1)
                maxdate = today + datetime.timedelta(days=5)
                # print(mindate, maxdate)

                cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            cursor="hand1", year=2020, month=5, day=5)
                # cal.pack(fill="both", expand=True)
                cal.grid()
                expensebtn2 = ttk.Button(top, text="Select", command=print_sel).grid()
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
            print('Description: ' + s2)
            return s2

        label_1 = ttk.Label(labelframe_2, text="Category",width=30,font=("bold", 10))
        label_1.grid(row=6,column=0,columnspan = 4, pady=4)

        def printcategory():
            print('Category: ' + cb.get())
            return cb.get()

        db = sqlite3.connect('myspendmate.db')
        cursor = db.cursor()
        cursor.execute("select * from expenseCat")
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
        # print("-------------incomeCat--------------")
        # print(cat_list)
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
            print('date selected' + str(t5))
            info = str(t5)
            day = info[8]+info[9]
            mon = info[5]+info[6]
            yr = info[0]+info[1]+info[2]+info[3]
            print('day ' + str(day))
            print('mon ' + str(mon))
            print('yr ' + str(yr))
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("insert into expense values('%d','%s','%s','%s','%s','%d','%d','%d')"%(int(t1),t5,t2,t3,t4,int(day),int(mon),int(yr)))
            cursor.execute("select sum(amount) from expense")
            sum1 = cursor.fetchone()[0]
            if(sum1=='None'):
                sum1=str(0)
            rootlabel1.config(text=str(sum1) + CurrencyCurrent)
            cursor.close()
            db.commit()
            db.close
            callbalance(root)
            return "done"
            # callBudget(root)
        

        # label_1 = Label(expense, text="Payment Recieved?",width=20,font=("bold", 10))
        # label_1.place(x=60,y=360)
        def expenseexit():
            expense.destroy()

        def AllinOne():
            # put()
            status = put()
            # if status == "stopped":
            #     AllinOne()
            if status == "done":
                messagebox.showinfo("Success!!","Expense Entry have been saved")
            print("After Expense Update Budget----------")
            callBudget(root)
            expenseexit()
            pass 

        savebutton = ttk.Button(labelframe_2, text = 'Save and Exit',command = AllinOne) 
        savebutton.grid(row=8,column = 0,columnspan = 6, pady=4)
        

    def GetData():
        expense1 = Tk()
        frm = ttk.Frame(expense1)
        frm.pack(side=tk.LEFT,padx=20)
        
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5) ,show="headings", height ='30')
        tv.pack()
        tv.heading(1,text="Amount")
        tv.heading(2,text="Date")
        tv.heading(3,text="Description")
        tv.heading(4,text="Category")
        tv.heading(5,text="Account_type")
        # expense1.geometry('1000x500')
        expense1.title("Expense Details")
        expense1.resizable(False,False)
        db = sqlite3.connect('myspendmate.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM expense ")
        list1 = cursor.fetchall()
        total = cursor.rowcount
        
        for i in list1:
            tv.insert('','end',values=i)

        cursor.close()
        db.commit()
        db.close
        print(list1)
        expense1.mainloop()

                
    #------------------------------------------------------------------ 
    btn1 = ttk.Button(labelframe1, text = 'Add Expense', command = AddExpense) 
    btn1.grid(row = 2, column = 1,padx=2, pady=4)
    btn2 = ttk.Button(labelframe1, text = 'Expense Details', command = GetData) 
    btn2.grid(row = 3, column = 1,padx=2, pady=4)
