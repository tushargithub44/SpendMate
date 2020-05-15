from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import PIL.Image
import sqlite3
from Main_Window.Currency import *
from Main_Window.theme import ttk_theme


def callbalance(root):
    labelframe1 = ttk.LabelFrame(root, text="Balance Section")  
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
    CurrencyCurrent = CurrentCurrr()
    print('balance :' + str(balance) + str(CurrencyCurrent))
    cursor.close()
    db.commit()
    db.close()

    rootlabel = ttk.Label(labelframe1, text="Your Current Balance is : ")
    # rootlabel.config(font=("Courier", 16))  
    rootlabel.grid(row = 1, column = 0, pady = 10)  
    print("current" + CurrencyCurrent)
    rootlabel1 = ttk.Label(labelframe1, text=str(balance) + str(CurrencyCurrent))
    rootlabel1.config(font=("Courier", 13))  
    rootlabel1.grid(row = 1, column = 1, pady = 10)  