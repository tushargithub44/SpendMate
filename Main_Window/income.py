from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3
from Main_Window.balance import *
from Main_Window.Currency import *

db = sqlite3.connect('myspendmate.db')
cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS incomeee (amount INT NOT NULL, date TEXT NOT NULL, description TEXT , category TEXT NOT NULL ,account_type TEXT NOT NULL,day INT NOT NULL,month INT NOT NULL,year INT NOT NULL)")
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
    labelframe2 = ttk.LabelFrame(root, text="Income Comments")  
    labelframe2.grid(row=1,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)

    CurrencyCurrent = CurrentCurrr()
    rootlabel = ttk.Label(labelframe2, text="Total Income : " )  
    rootlabel.grid(row=1, column = 0)
    rootlabel.configure(anchor="center")
    rootlabel1 = ttk.Label(labelframe2, text= str(sum1) + CurrencyCurrent)  
    rootlabel1.config(font=("Courier", 13))  
    rootlabel1.grid(row=1, column = 1)
    rootlabel1.configure(anchor="center")

    def AddIncome():
        income = Tk()
        income.geometry('500x500')
        income.title("Add Income")
    
        label_1 = Label(income, text="Enter Amount",width=20,font=("bold", 10))
        label_1.place(x=60,y=60)

        entry_1 = Entry(income, bd=5)
        entry_1.place(x=240,y=60)
        def printamount():
            s = entry_1.get()
            print('Amount: ' + s)
            return s
            
        
        label_2 = Label(income, text="Select Date",width=20,font=("bold", 10))
        label_2.place(x=60,y=120)
        def dateSelector():
                
            def print_sel():
                global date_selected 
                dateselected = cal.selection_get()
                date_selected=dateselected
                print(dateselected)
                date = str(dateselected)
                print(date[6])
                labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                label_3 = Label(income, text=dateselected,width=20,font=("bold", 10))
                label_3.place(x=310,y=120)
                # cal.see(datetime.date(year=2016, month=2, day=5))
                date = str(cal.selection_get())
                    
                    

            top = Toplevel(income)
            # top.geometry('500x500')
            import datetime
            today = datetime.date.today()

            mindate = datetime.date(year=2020, month=5, day=1)
            maxdate = today + datetime.timedelta(days=5)
                # print(mindate, maxdate)

            cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            cursor="hand1", year=2020, month=5, day=5)
            cal.pack(fill="both", expand=True)
            incomebtn2 = Button(top, text="Select", command=print_sel).pack() 
            print("Date_new:"+str(date_selected))
            return date_selected
                # tk.top.destroy()



        incomebtn = Button(income, text='Enter Date', command = dateSelector)
        incomebtn.place(x=240,y=120)

        label_1 = Label(income, text="Description",width=20,font=("bold", 10))
        label_1.place(x=60,y=180)

        entry_2 = Entry(income,bd = 5)
        entry_2.place(x=240,y=180)
        def printdescription():
            s2 = entry_2.get()
            desc = str(entry_2.get())
            print('Description: ' + s2)
            return s2

        label_1 = Label(income, text="Category",width=20,font=("bold", 10))
        label_1.place(x=60,y=240)

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
        cb = ttk.Combobox(income,values=Category,width=10)
        cb.place(x = 240,y= 240)
        cb.current(0)

        label_1 = Label(income, text="Account",width=20,font=("bold", 10))
        label_1.place(x=60,y=300)
        
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
        accountbox = ttk.Combobox(income,values=Account,width=10)
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
            
            
        
        

        # label_1 = Label(income, text="Payment Recieved?",width=20,font=("bold", 10))
        # label_1.place(x=60,y=360)
        def incomeexit():
            income.destroy()

        def AllinOne():
            put()
            incomeexit()
            pass 

        savebutton = Button(income, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
        savebutton.place(x = 180, y = 350)


    


    def GetData():
        income = Tk()
        frm = Frame(income)
        frm.pack(side=tk.LEFT,padx=20)
        
        tv=ttk.Treeview(frm,columns=(1,2,3,4,5) ,show="headings", height ='30')
        tv.pack()
        tv.heading(1,text="Amount")
        tv.heading(2,text="Date")
        tv.heading(3,text="Description")
        tv.heading(4,text="Category")
        tv.heading(5,text="Account_type")
        income.geometry('1000x500')
        income.title("Income Details")
        income.resizable(False,False)
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
        income.mainloop()

    # -------------------------Income Main window Section---------------------
      

    btn1 = ttk.Button(labelframe2, text = 'Add Income',command = AddIncome) 
    btn1.grid(row = 2, column = 0,padx=2)
    btn2 = ttk.Button(labelframe2, text = 'Get Details',command = GetData) 
    btn2.grid(row = 2, column = 1, padx=2)
