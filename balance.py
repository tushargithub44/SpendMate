from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3

db = sqlite3.connect('myspendmate.db')
cursor = db.cursor()
sum_inc = 0
sum_exp =0
check1 =0
check2=0
cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='income';")
if cursor.fetchone()[0]==1 : 
    cursor.execute("select sum(amount) from incomeee")
    t = cursor.fetchone()[0]
    if(t=='None'):
        t=str(0)
        sum_inc=int(t)

    
else :
    print('Table does not exists.')
    sum_inc = 0

cursor.execute("SELECT count(*) FROM sqlite_master WHERE type='table' AND name='expense';")

if cursor.fetchone()[0]==1 : 
    cursor.execute("select sum(amount) from expense")
    t = cursor.fetchone()[0]
    if(t=='None'):
        t=str(0)
        sum_exp=int(t)
else :
    print('Table does not exists.')
    sum_exp=0
sum_tot = sum_inc - sum_exp
cursor.close()
db.commit()
db.close()


def callbalance(root):
    labelframe1 = LabelFrame(root, text="Balance Comments")  
    labelframe1.grid(row=1,column = 0,columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Your Current Balance is : "+str(sum_tot))  
    rootlabel.grid(pady = 10)  