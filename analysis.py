from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt


def callAnalysis(root):
    labelframe1 = LabelFrame(root, text="Positive Comments")  
    labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Place to put the positive comments")  
    rootlabel.grid()  

    def printpie():
        # Data to plot
        labels = '', 'C++', 'Ruby', 'Java'
        sizes = [215, 130, 245, 210]
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