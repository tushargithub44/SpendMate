from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt


def callmenuFunc(menubar): 

    def showCategories():
        print("Categories!!!")

    def setCurrency():
        print("Set Currency here!")

    def Backup():
        print("Take Backup")

    def Reports():
        print("Take Reports here!")

    functionmenu = Menu(menubar, tearoff = 0)
    functionmenu.add_command(label = "Categories",command = showCategories)
    functionmenu.add_command(label = "Set Currency",command = setCurrency)
    functionmenu.add_command(label = "Reports", command = Reports)
    functionmenu.add_command(label = "Backup", command = Backup)

    menubar.add_cascade(label = "Functions", menu = functionmenu)