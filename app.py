from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from ttkthemes import ThemedTk
from tkinter import messagebox
import matplotlib.pyplot as plt
from databasemaker import *
from PIL import Image, ImageTk
import PIL.Image
# Database Maker:
makedatabase()

from Main_Window.balance import *
from Main_Window.income import *
from Main_Window.budget import *
from Main_Window.goals import *
from Main_Window.analysis import *
from Main_Window.expense import *
from Menubar.menuFunctions import *
from Menubar.menuOthers import *




root = ThemedTk(theme = "xpnative", themebg = True)
# root.geometry("950x600")  
root.title("SpendMate - Your Money Manager")
root.iconphoto(True, tk.PhotoImage(file='SpendMate1.png'))
root.resizable(False, False)
img = ImageTk.PhotoImage(PIL.Image.open("SpendMate1.png"))
panel = tk.Label(root, image = img)
panel.grid(row = 0,column = 0, columnspan=4)

tlabel = ttk.Label(root, text="Welcome to SpendMate :)") 
tlabel.grid(row = 0,column = 1, columnspan = 8,pady = 2)  
tlabel.config(font=("Comic Sans MS", 25))

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


root.mainloop()