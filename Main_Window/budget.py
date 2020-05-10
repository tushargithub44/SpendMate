from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3
from Main_Window.Currency import CurrentCurrr

tp = 0
tp1=0
pe=0.0
pert=0.0
po=0


def callBudget(root):
    CurrencyCurrent = CurrentCurrr()
    budgetframe1 = ttk.LabelFrame(root, text="Budget Information")  
    budgetframe1.grid(row=3,column = 0, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)
    db = sqlite3.connect('myspendmate.db')
    cursor = db.cursor()
    cursor.execute("select count(*) from budget")
    if cursor.fetchone()[0]!=0:
        cursor.execute("SELECT amount FROM budget ORDER BY ROWID DESC LIMIT 1")
        tp = cursor.fetchone()[0]
        print('tp------- : ' + str(tp))
            
        cursor.execute("SELECT percentage FROM budget ORDER BY ROWID DESC LIMIT 1")
        tp1 = cursor.fetchone()[0]
        print('tp1------- : ' + str(tp1))

        cursor.execute("select sum(amount) from expense")
        po = cursor.fetchone()[0]
        print('before po' + str(po))
        if(po == None):
            po = 0
        print('po : ' + str(po))            
            
        cursor.close()
        db.commit()
        db.close
        pe = (po*100) / tp
        print('pe : ' + str(pe))
        check = 1
    else:
        check=None

    cursor.close()
    db.commit()
    db.close()

    if check == 1:
        CurrencyCurrent = CurrentCurrr()
        budgetlabel = ttk.Label(budgetframe1, text="Total Budget :")  
        budgetlabel.grid(row = 3, column = 0)  
        budgetlabel1 = ttk.Label(budgetframe1, text=str(tp) + CurrencyCurrent)  
        budgetlabel1.grid(row = 3, column = 1)  
        budgetlabel1.config(font=("Courier", 13))  
        Spentlabel = ttk.Label(budgetframe1, text="Percentage Set :")  
        Spentlabel.grid(row = 4, column = 0)  
        Spentlabel1 = ttk.Label(budgetframe1, text=str(tp1) + "%")  
        Spentlabel1.grid(row = 4, column = 1)
        Spentlabel1.config(font=("Courier", 13))  
        if pe>tp1:
            budgetlabel2 = ttk.Label(budgetframe1, text="Current amount spend exceeds the budget",bg="red")  
            budgetlabel2.grid()
        else:
            budgetlabel2 = ttk.Label(budgetframe1, text="Budget under control")  
            budgetlabel2.grid()

    else:
        budgetlabel = ttk.Label(budgetframe1, text=" Total Budget : Not Set")  
        budgetlabel.grid()  
        Spentlabel = ttk.Label(budgetframe1, text="")  
        Spentlabel.grid()
        budgetlabel2 = ttk.Label(budgetframe1, text="")  
        budgetlabel2.grid()  
    budgetamt=0

    def ManageBudget():
        income = Tk()
        income.geometry('400x250')
        income.title("Manage Budget")

        label_1 = Label(income, text="Set Budget Value",width=20,font=("bold", 10))
        label_1.place(x=30,y=60)

        entry_1 = Entry(income, bd=5)
        entry_1.place(x=240,y=60)
        def printamount():
            s = entry_1.get()
            print('Budget: ' + s)
            return s


        label_2 = Label(income, text="Set Percentage to Notify:",width=20,font=("bold", 10))
        label_2.place(x=30,y=120)

        entry_2 = Entry(income, bd=5)
        entry_2.place(x=240,y=120)
        def printper():
            s = int(entry_2.get())
            if s>100 or s<0:
                messagebox.showinfo("Title", "Invalid Percentage! Set Between 0 to 100")
            print('Percentage: ' + str(s))
            return s

        def put():
            t1 =printamount()
            t2 =printper()
        
            u1 = int(t1)
            u2 = int(t2)
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("insert into budget values('%d','%d')"%(int(t1),int(t2)))
            
            
            cursor.close()
            db.commit()
            db.close
            get()
        
       
            
        def get():
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            total = cursor.rowcount
            cursor.execute("SELECT amount FROM budget ORDER BY ROWID DESC LIMIT 1")
            budgetamt = cursor.fetchone()[0]
            print("-------" + str(budgetamt))
            
            cursor.execute("SELECT percentage FROM budget ORDER BY ROWID DESC LIMIT 1")
            budgetper = cursor.fetchone()[0]
            print("-------" + str(budgetper))
            cursor.execute("select sum(amount) from expense")
            total_expense = cursor.fetchone()[0]
            if total_expense == None:
                total_expense = 0
            print(total_expense)            
            
            cursor.close()
            db.commit()
            db.close
            spentper = (total_expense*100)/budgetamt
            print(spentper)
            budgetlabel1.config(text=str(budgetamt) + CurrencyCurrent)
            Spentlabel1.config(text=str(budgetper) + "%")
            if budgetper<spentper:
                budgetlabel2.config(text="Current amount spend exceeds the budget", bg="red")
            else:
                budgetlabel2.config(text="Budget under control", bg='white')
            income.destroy()


        btn1 = Button(income, text = 'Set', command=put) 
        btn1.place(x = 150, y = 180)
        

    btn1 = ttk.Button(budgetframe1, text = 'Manage Budget', command=ManageBudget) 
    btn1.grid()
