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
        Currency = Tk()
        Currency.geometry('500x500')
        Currency.title("Set Currency")

        label_1 = Label(Currency, text="Select Currency",width=20,font=("bold", 10))
        label_1.place(x=80,y=200)

        country_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 

        
        cb = ttk.Combobox(Currency,values=country_list,width=10)
        cb.place(x = 260,y= 200)
        cb.current(0)

        def SaveCurrency():
            print(cb.get()) #  Save this to database
            Currency.destroy()

        savebutton = Button(Currency, text = 'Save and Exit',command = SaveCurrency, padx=20, pady=20) 
        savebutton.place(x = 180, y = 320)
        

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