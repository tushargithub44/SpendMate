from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt


def callBudget(root):
    budgetframe1 = LabelFrame(root, text="Budget Information")  
    budgetframe1.grid(row=3,column = 0, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    budgetlabel = Label(budgetframe1, text="Total Budget :")  
    budgetlabel.grid()  
    Spentlabel = Label(budgetframe1, text="Amount Spent :")  
    Spentlabel.grid() 

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


        label_2 = Label(income, text="Set Percentage to Notify:",width=20,font=("bold", 10))
        label_2.place(x=30,y=120)

        entry_2 = Entry(income, bd=5)
        entry_2.place(x=240,y=120)
        def printper():
            s = int(entry_2.get())
            if s>100 or s<0:
                messagebox.showinfo("Title", "Invalid Percentage! Set Between 0 to 100")
            print('Percentage: ' + str(s))

        def printall():
            printamount()
            printper()
        btn1 = Button(income, text = 'Set', command=printall) 
        btn1.place(x = 150, y = 180)
        

    btn1 = Button(budgetframe1, text = 'Manage Budget', command=ManageBudget) 
    btn1.grid()
