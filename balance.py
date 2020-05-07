from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3



def callbalance(root):
    labelframe1 = LabelFrame(root, text="Balance Comments")  
    labelframe1.grid(row=1,column = 0,columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    db = sqlite3.connect('myspendmate.db')
    cursor = db.cursor()
    total_income = 0
    total_expense = 0

    cursor.execute("select sum(amount) from income")
    total_income = cursor.fetchone()[0]
    if(str(total_income) == 'None'):
        total_income = 0
    print('total_income :' + str(total_income))

    cursor.execute("select sum(amount) from expense")
    total_expense = cursor.fetchone()[0]
    if(str(total_expense)=='None'):
        total_expense=0

    print('total_expense :' + str(total_expense))


    balance = total_income - total_expense
    print('balance :' + str(balance))
    cursor.close()
    db.commit()
    db.close()

    rootlabel = Label(labelframe1, text="Your Current Balance is : " + str(balance) )  
    rootlabel.grid(pady = 10)  