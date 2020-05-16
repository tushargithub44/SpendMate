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
from Main_Window.Currency import CurrentCurrr
from Main_Window.theme import ttk_theme

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
        print('Check is 1')
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
            style = ttk.Style()
            style.configure("BW.TLabel", background="yellow")
            budgetlabel2 = ttk.Label(budgetframe1, text="Message :")  
            budgetlabel2.grid(row = 5, column = 0, pady =2)
            budgetlabel2 = ttk.Label(budgetframe1, text="!!BUDGET EXCEEDED!!", style="BW.TLabel")  
            budgetlabel2.grid(row = 5, column = 1, pady =2)
        else:
            budgetlabel2 = ttk.Label(budgetframe1, text="Message :")  
            budgetlabel2.grid(row = 5, column = 0, pady =2)
            budgetlabel2 = ttk.Label(budgetframe1, text="Budget under control")  
            budgetlabel2.grid(row = 5, column = 1, pady =2)

    else:
        print('Check is None')
        budgetlabel = ttk.Label(budgetframe1, text="Total Budget :")  
        budgetlabel.grid(row = 3, column = 0)  
        budgetlabel1 = ttk.Label(budgetframe1, text="Not set" + CurrencyCurrent)  
        budgetlabel1.grid(row = 3, column = 1)  
        budgetlabel1.config(font=("Courier", 13))  
        Spentlabel = ttk.Label(budgetframe1, text="Percentage Set :")  
        Spentlabel.grid(row = 4, column = 0)  
        Spentlabel1 = ttk.Label(budgetframe1, text="Not set%")  
        Spentlabel1.grid(row = 4, column = 1)
        Spentlabel1.config(font=("Courier", 13))  
    budgetamt=0

    def ManageBudget():
        income = ThemedTk(theme = ttk_theme, themebg = True)
        income.title("Manage Budget")
        income.resizable(False, False)
        labelframe2 = ttk.LabelFrame(income, text="Set Month and Year")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Please provide the following: ", width=30, font=("bold", 10))  
        rootlabel.grid(row=2,column = 0,columnspan = 4,padx = 10, pady=4)

        label_1 = ttk.Label(labelframe2, text="Set Budget Value ",width=30,font=("bold", 10))
        label_1.grid(row=3,column = 0,columnspan = 4, pady=4)

        entry_1 = Entry(labelframe2, bd=5)
        entry_1.grid(row=4,column = 0, pady=4)


        # label_1 = ttk.Label(income, text="Set Budget Value",width=20,font=("bold", 10))
        # label_1.place(x=30,y=60)

        # entry_1 = Entry(income, bd=5)
        # entry_1.place(x=240,y=60)
        def printamount():
            s = entry_1.get()
            if s.isdigit():
                print('Budget: ' + s)
                return s
            else:
                messagebox.showinfo("Attention!","Budget Value Should be a number and not text or any Special Character!\nEntry Not Saved. Try Again!")
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"

        label_2 = ttk.Label(labelframe2, text="Set Percentage to Notify:",width=30,font=("bold", 10))
        label_2.grid(row=5, column = 0, columnspan = 4, pady=4)

        entry_2 = Entry(labelframe2, bd=5)
        entry_2.grid(row=6, column = 0, pady=4)

        def printper():
            s = int(entry_2.get())
            if s>100 or s<0:
                messagebox.showinfo("Title", "Invalid Percentage! Set Between 0 to 100")
                return 1
            print('Percentage: ' + str(s))
            return s

        def put():
            t1 =printamount()
            if t1 == "stop":
                get()
            else:
                t2 = printper()
                if t2 == 1:
                    get()
                else:
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
                budgetlabel2 = ttk.Label(budgetframe1, text="Message :")  
                budgetlabel2.grid(row = 5, column = 0, pady =2)
                budgetlabel2 = ttk.Label(budgetframe1, text="!!!BUDGET EXCEEDED!!!")  
                budgetlabel2.grid(row = 5, column = 1, pady =2)
                # budgetlabel2.config(bg="Red")
            else:
                budgetlabel2 = ttk.Label(budgetframe1, text="Message :")  
                budgetlabel2.grid(row = 5, column = 0, pady =2)
                budgetlabel2 = ttk.Label(budgetframe1, text="Budget under control")  
                budgetlabel2.grid(row = 5, column = 1, pady =2)
            income.destroy()


        btn1 = ttk.Button(labelframe2, text = 'Set', command=put) 
        btn1.grid(row=7,column = 0, pady=4)
        

    btn1 = ttk.Button(budgetframe1, text = 'Manage Budget', command=ManageBudget) 
    btn1.grid(row = 7, column = 0, columnspan = 3)
