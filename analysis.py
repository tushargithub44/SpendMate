from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3

sum_expense=0
sum_amount=0
sum_total=0
db = sqlite3.connect('myspendmate.db')
cursor = db.cursor()
month_name=['jan','feb','mar','apr','may']
lis=[]
expens=[]
cursor.execute("select sum(amount) from incomeee")
sum_total = cursor.fetchone()[0]
if(sum_total== 'None'):
    sum_total=str(0)
print(sum_total)
for i in range(1,5):
    cursor.execute("select sum(amount) from incomeee where month= '%d'"%i)
    sum_mon=cursor.fetchone()[0]
    st=str(sum_mon)
    print("Initial:"+st)
   
    
    if(st == 'None'):
        st=str(0)
    print("price:"+st)
    perc =float((int(st)/int(sum_total))*100)
    print("per:"+str(perc))
    print(st)
    lis.append(month_name[i])
    expens.append(perc)




for i in expens:
    print(i)
    print("h")

    
cursor.close()
db.commit()
db.close()


def callAnalysis(root):
    labelframe1 = LabelFrame(root, text="Positive Comments")  
    labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Place to put the positive comments")  
    rootlabel.grid()  

    def printpie():
        # Data to plot
        labels = lis
        sizes = expens
        colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
        explode = (0.1, 0, 0, 0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()

    btn1 = Button(labelframe1, text = 'Daily Expense Analysis', command = printpie) 
    btn1.grid()

    btn1 = Button(labelframe1, text = 'Expense Analysis') 
    btn1.grid()

    btn1 = Button(labelframe1, text = 'Income Analysis') 
    btn1.grid()