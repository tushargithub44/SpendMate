from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3
from balance import *
from Currency import *
from budget import *

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
    labelframe1 = LabelFrame(root, text="Expense Comments")  
    labelframe1.grid(row=1,column = 6, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30) 

    rootlabel = Label(labelframe1, text="Total Expense : ")  
    rootlabel.grid()  
    CurrencyCurrent = CurrentCurrr()
    rootlabel.grid(row=1, column = 0)
    rootlabel1 = Label(labelframe1, text= str(sum1) + CurrencyCurrent)  
    rootlabel1.config(font=("Courier", 13))  
    rootlabel1.grid(row=1, column = 1)

    
    def AddExpense():
        expense = Tk()
        expense.geometry('500x500')
        expense.title("Add Expense")

        label_1 = Label(expense, text="Enter Amount",width=20,font=("bold", 10))
        label_1.place(x=60,y=60)

        entry_1 = Entry(expense, bd=5)
        entry_1.place(x=240,y=60)
        def printamount():
            s = entry_1.get()
            print('Amount: ' + s)
            return s
        
        label_2 = Label(expense, text="Select Date",width=20,font=("bold", 10))
        label_2.place(x=60,y=120)
        def dateSelector():
                def print_sel():
                    global date_selected
                    dateselected = cal.selection_get()
                    date_selected=dateselected
                    print(dateselected)
                    labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                    label_3 = Label(expense, text=dateselected,width=20,font=("bold", 10))
                    label_3.place(x=310,y=120)
                    cal.see(datetime.date(year=2020, month=2, day=5))
                    return dateselected

                top = Toplevel(expense)
                # top.geometry('500x500')
                import datetime
                today = datetime.date.today()

                mindate = datetime.date(year=2018, month=1, day=21)
                maxdate = today + datetime.timedelta(days=5)
                # print(mindate, maxdate)

                cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            cursor="hand1", year=2020, month=2, day=5)
                cal.pack(fill="both", expand=True)
                expensebtn2 = Button(top, text="Select", command=print_sel).pack() 
                print("Date_new:"+str(date_selected))
                return date_selected
                # tk.top.destroy()



        expensebtn = Button(expense, text='Enter Date', command = dateSelector)
        expensebtn.place(x=240,y=120)

        label_1 = Label(expense, text="Description",width=20,font=("bold", 10))
        label_1.place(x=60,y=180)

        entry_2 = Entry(expense,bd = 5)
        entry_2.place(x=240,y=180)
        def printdescription():
            s2 = entry_2.get()
            print('Description: ' + s2)
            return s2

        label_1 = Label(expense, text="Category",width=20,font=("bold", 10))
        label_1.place(x=60,y=240)

        def printcategory():
            print('Category: ' + cb.get())
            return cb.get()

        Category=["Salary","Year Bonus","FDR"]
        cb = ttk.Combobox(expense,values=Category,width=10)
        cb.place(x = 240,y= 240)
        cb.current(0)

        label_1 = Label(expense, text="Account",width=20,font=("bold", 10))
        label_1.place(x=60,y=300)

        def printaccount():
            print('Account: ' + accountbox.get())
            return accountbox.get()

        Account=["Cash","Card","Paytm"]
        accountbox = ttk.Combobox(expense,values=Account,width=10)
        accountbox.place(x = 240,y= 300)
        accountbox.current(0)

        def put():
            t1 = printamount()
            t2 = printdescription()
            t3 = printcategory()
            t4 = printaccount()
            t5 = date_selected
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
            # callBudget(root)
        

        # label_1 = Label(expense, text="Payment Recieved?",width=20,font=("bold", 10))
        # label_1.place(x=60,y=360)
        def expenseexit():
            expense.destroy()

        def AllinOne():
            put()
            print("After Expense Update Budget----------")
            callBudget(root)
            expenseexit()
            pass 

        savebutton = Button(expense, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
        savebutton.place(x = 180, y = 350)
     

    def GetData():
        expense1 = Tk()
        frm = Frame(expense1)
        frm.pack(side=tk.LEFT,padx=20)
        
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5) ,show="headings", height ='30')
        tv.pack()
        tv.heading(1,text="Amount")
        tv.heading(2,text="Date")
        tv.heading(3,text="Description")
        tv.heading(4,text="Category")
        tv.heading(5,text="Account_type")
        expense1.geometry('1000x500')
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
    btn1 = Button(labelframe1, text = 'Add Expense', command = AddExpense) 
    btn1.grid(row = 2, column = 0,padx=2)
    btn2 = Button(labelframe1, text = 'Expense Details', command = GetData) 
    btn2.grid(row = 2, column = 1,padx=2)
