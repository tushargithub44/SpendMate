from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3
tp = 0
tp1=0
pe=0.0
pert=0.0
po=0
db = sqlite3.connect('myspendmate.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS budgettt (amount INT NOT NULL, percentage INT NOT NULL)")
cursor.execute("select count(*) from budgettt")
if cursor.fetchone()[0]!=0:
    cursor.execute("SELECT amount FROM budgettt ORDER BY ROWID DESC LIMIT 1")
    tp = cursor.fetchone()[0]
    print(tp)
            
    cursor.execute("SELECT percentage FROM budgettt ORDER BY ROWID DESC LIMIT 1")
    tp1 = cursor.fetchone()[0]
    print(tp1)
    cursor.execute("select sum(amount) from expense")
    po = cursor.fetchone()[0]
    print(po)            
            
    cursor.close()
    db.commit()
    db.close
    pe = ((tp - po)*100)/tp
    print(pe)
    check =1
     

cursor.close()
db.commit()
db.close()

def callBudget(root):
    budgetframe1 = LabelFrame(root, text="Budget Information")  
    budgetframe1.grid(row=3,column = 0, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)
    
    if check ==1 :
        budgetlabel = Label(budgetframe1, text=" TotalBudget :" + str(tp))  
        budgetlabel.grid()  
        Spentlabel = Label(budgetframe1, text="Amount Spent :"+ str(po))  
        Spentlabel.grid()  
        if pe<tp1:
            budgetlabel2 = Label(budgetframe1, text="Current amount spend exceeds the budget",bg="red")  
            budgetlabel2.grid()
        else:
            budgetlabel2 = Label(budgetframe1, text="Budget under control")  
            budgetlabel2.grid()

    else:
        budgetlabel = Label(budgetframe1, text=" TotalBudget :")  
        budgetlabel.grid()  
        Spentlabel = Label(budgetframe1, text="Amount Spent :")  
        Spentlabel.grid()
        budgetlabel2 = Label(budgetframe1, text="Budget under control")  
        budgetlabel2.grid()  
    amt=0

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
        
            u1=int(t1)
            u2 = int(t2)
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("insert into budgettt values('%d','%d')"%(int(t1),int(t2)))
            
            
            cursor.close()
            db.commit()
            db.close
            get()
        
       
            
        def get():
            
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            total = cursor.rowcount
            cursor.execute("SELECT amount FROM budgettt ORDER BY ROWID DESC LIMIT 1")
            amt = cursor.fetchone()[0]
            print(amt)
            
            cursor.execute("SELECT percentage FROM budgettt ORDER BY ROWID DESC LIMIT 1")
            per = cursor.fetchone()[0]
            print(per)
            cursor.execute("select sum(amount) from expense")
            sum_expense = cursor.fetchone()[0]
            print(sum_expense)            
            
            cursor.close()
            db.commit()
            db.close
            perc1 = ((amt - sum_expense)*100)/amt
            print(perc1)
            budgetlabel.config(text=" TotalBudget :"+ str(amt))
            Spentlabel.config(text="Amount Spent :"+ str(sum_expense))
            if perc1<per:
                budgetlabel2.config(text="Current amount spend exceeds the budget",bg="red")
            else:
                budgetlabel2.config(text="Budget under control",bg='white')

              

        btn1 = Button(income, text = 'Set', command=put) 
        btn1.place(x = 150, y = 180)
        
        
            
    

    


    btn1 = Button(budgetframe1, text = 'Manage Budget', command=ManageBudget) 
    btn1.grid()
