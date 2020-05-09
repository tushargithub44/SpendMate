from tkinter import * 
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
from databasemaker import *

# Database Maker:
makedatabase()  

from balance import *
from income import *
from budget import *
from goals import *
from analysis import *
from expense import *
from menuFunctions import *
from menuOthers import *




root = Tk()  
root.geometry("950x600")  
root.resizable(False, False)

tlabel = Label(root, text="Welcome to SpendMate")  
tlabel.grid(columnspan = 12,pady = 2)  
tlabel.config(font=("ubuntu", 25))

menubar = Menu(root)  
# Function menu
callmenuFunc(menubar, root)
# Others menu
callmenuOther(menubar)
root.config(menu=menubar)  

#  Balance Portion of Main Window
callbalance(root)

# Income Section of Main Window
callincome(root)

# Income Section of Main Window
callExpense(root)

# Budget Section of Main Window
callBudget(root)

# Analysis Section of Main Window
callAnalysis(root)

# Goals Section of Main Window
callGoals(root)




# root.rowconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)

root.mainloop()