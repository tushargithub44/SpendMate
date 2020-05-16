from tkinter import *  
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
from ttkthemes import ThemedTk
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sqlite3
from Main_Window.theme import ttk_theme



def callAnalysis(root):
    labelframe1 = ttk.LabelFrame(root, text="Analysis Section")  
    labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = ttk.Label(labelframe1, text="Analysis Plots of your Income and Expense")  
    rootlabel.grid(row =3, column = 1, pady =2)  

    def displaypie():
        # Data to plot
        dispie = ThemedTk(theme = ttk_theme, themebg = True)
        dispie.resizable(False, False)
        dispie.title('Set Month and Year')
        labelframe2 = ttk.LabelFrame(dispie, text="Set Month and Year")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Please provide the following: ", width=30, font=("bold", 10))  
        rootlabel.grid(row=2,column = 0,columnspan = 4,padx = 10, pady=4)

        label_1 = ttk.Label(labelframe2, text="Enter Month(Between 1-12): ",width=30,font=("bold", 10))
        label_1.configure(anchor="center") 
        label_1.grid(row=3,column = 0,columnspan = 4, pady=4)

        entry_1 = Entry(labelframe2, bd=5)
        entry_1.grid(row=4,column = 0, pady=4)
        def printmonth():
            s = entry_1.get()
            if s.isdigit():
                print('Month: ' + s)
                return s           
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"

        
        label_2 = ttk.Label(labelframe2, text="Enter Year",width=30,font=("bold", 10))
        label_2.configure(anchor="center") 
        label_2.grid(row=5,column = 0, pady=4)

        entry_2 = Entry(labelframe2, bd=5)
        entry_2.grid(row=6,column = 0, pady=4)

        def printyear():
            s = entry_2.get()
            if s.isdigit():
                print('Year: ' + s)
                return s          
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"

        
        def draw(monthgot,yeargot):
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute(" select sum(amount) from expense")
            total_expense = cursor.fetchone()[0]
            if total_expense == None:
                total_expense = 0 
            cursor.execute("select * from expense")
            expense_list=cursor.fetchall()
            
            labels = []
            amt_expe = []
            sizes = []
            count = -1

            for i in expense_list:
                category = str(i[3]) 
                print("category " + str(category))   
                amt_category = i[0]
                print("amt of category " + str(amt_category))
                if labels.count(category) == 0:
                    count+=1
                    labels.append(category)
                    amt_expe.append(amt_category)
                    sizes.append(float((amt_category*100)/total_expense))   
                else:
                    ppcount = labels.index(category)
                    amt_expe[ppcount] = amt_expe[ppcount] + amt_category
                    sizes[ppcount] = float((amt_expe[ppcount]*100)/total_expense)


            tobe = sizes.index(max(sizes))
            print('tobe is : ' + str(tobe))
            explode = []
            for i in range(count+1):
                if i == tobe:
                    explode.append(0.1)  
                else:
                    explode.append(0)
            explode = tuple(explode)
            print('label ' + str(labels))
            print('amt ' + str(amt_expe))
            print('sizes ' + str(sizes))
            print('explode ' + str(explode))
            
            # Plot
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            plt.show()
        def AllinOne():
            monthgot = printmonth()
            yeargot = printyear()
            if monthgot == "stop" or yeargot == "stop":
                messagebox.showinfo("Attention!","Month/Year Should be a number and not text or any Special Character!\nEntry Not Saved. Try Again!")
                return "stopped"
            dispie.destroy()
            draw(monthgot,yeargot)
        sbutton = ttk.Button(labelframe2, text = 'Continue',command = AllinOne) 
        sbutton.grid(row=7,column = 0, pady=4)


    btn1 = ttk.Button(labelframe1, text = 'Categorywise Expense Analysis', command = displaypie) 
    btn1.grid(row = 6,column = 1, pady = 2)

    def displaypie2():
        # Data to plot
        dispie2 = ThemedTk(theme = ttk_theme, themebg = True)
        dispie2.resizable(False, False)
        dispie2.title('Set Month and Year')
        labelframe2 = ttk.LabelFrame(dispie2, text="Set Month and Year")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Please provide the following: ", width=30, font=("bold", 10))  
        rootlabel.grid(row=2,column = 0,columnspan = 4,padx = 10, pady=4)

        label_1 = ttk.Label(labelframe2, text="Enter Month(Between 1-12): ",width=30,font=("bold", 10))
        label_1.configure(anchor="center") 
        label_1.grid(row=3,column = 0,columnspan = 4, pady=4)

        entry_1 = Entry(labelframe2, bd=5)
        entry_1.grid(row=4,column = 0, pady=4)
        def printmonth():
            s = entry_1.get()
            if s.isdigit():
                print('Month: ' + s)
                return s           
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"
        
        label_2 = ttk.Label(labelframe2, text="Enter Year",width=30,font=("bold", 10))
        label_2.configure(anchor="center") 
        label_2.grid(row=5,column = 0, pady=4)

        entry_2 = Entry(labelframe2, bd=5)
        entry_2.grid(row=6,column = 0, pady=4)

        def printyear():
            s = entry_2.get()
            if s.isdigit():
                print('Year: ' + s)
                return s          
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"
        
        def draw(monthgot,yeargot):
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute(" select sum(amount) from income where month=? AND year=?", (monthgot,yeargot))
            total_expense = cursor.fetchone()[0]
            if total_expense == None:
                total_expense = 0 
            cursor.execute("select * from income where month=? AND year=?", (monthgot,yeargot))
            expense_list=cursor.fetchall()
            
            labels = []
            amt_expe = []
            sizes = []
            count = -1

            for i in expense_list:
                category = str(i[3]) 
                print("category " + str(category))   
                amt_category = i[0]
                print("amt of category " + str(amt_category))
                if labels.count(category) == 0:
                    count+=1
                    labels.append(category)
                    amt_expe.append(amt_category)
                    sizes.append(float((amt_category*100)/total_expense))   
                else:
                    ppcount = labels.index(category)
                    amt_expe[ppcount] = amt_expe[ppcount] + amt_category
                    sizes[ppcount] = float((amt_expe[ppcount]*100)/total_expense)


            tobe = sizes.index(max(sizes))
            print('tobe is : ' + str(tobe))
            explode = []
            for i in range(count+1):
                if i == tobe:
                    explode.append(0.1)  
                else:
                    explode.append(0)
            explode = tuple(explode)
            print('label ' + str(labels))
            print('amt ' + str(amt_expe))
            print('sizes ' + str(sizes))
            print('explode ' + str(explode))
            
            # Plot
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
            ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

            plt.show()
        def AllinOne():
            monthgot = printmonth()
            yeargot = printyear()
            if monthgot == "stop" or yeargot == "stop":
                messagebox.showinfo("Attention!","Month/Year Should be a number and not text or any Special Character!\nEntry Not Saved. Try Again!")
                return "stopped"
            dispie2.destroy()
            draw(monthgot,yeargot)
        sbutton = ttk.Button(labelframe2, text = 'Continue',command = AllinOne) 
        sbutton.grid(row=7,column = 0, pady=4)

    btn1 = ttk.Button(labelframe1, text = 'Categorywise Income Analysis', command = displaypie2) 
    btn1.grid(row = 7,column = 1, pady = 2)

# =========================================================================================

    def barexpense():
        bar = ThemedTk(theme = ttk_theme, themebg = True)
        bar.resizable(False, False)
        bar.title('Set Month and Year')
        labelframe2 = ttk.LabelFrame(bar, text="Set Month and Year")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Please provide the following: ", width=30, font=("bold", 10))  
        rootlabel.grid(row=2,column = 0,columnspan = 4,padx = 10, pady=4)

        label_1 = ttk.Label(labelframe2, text="Enter Month(Between 1-12): ",width=30,font=("bold", 10))
        label_1.configure(anchor="center") 
        label_1.grid(row=3,column = 0,columnspan = 4, pady=4)

        entry_1 = Entry(labelframe2, bd=5)
        entry_1.grid(row=4,column = 0, pady=4)
        def printmonth():
            s = entry_1.get()
            if s.isdigit():
                print('Month: ' + s)
                return s           
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"
        
        label_2 = ttk.Label(labelframe2, text="Enter Year",width=30,font=("bold", 10))
        label_2.configure(anchor="center") 
        label_2.grid(row=5,column = 0, pady=4)

        entry_2 = Entry(labelframe2, bd=5)
        entry_2.grid(row=6,column = 0, pady=4)

        def printyear():
            s = entry_2.get()
            if s.isdigit():
                print('Year: ' + s)
                return s          
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"
        
        def draw(monthgot,yeargot):
            dates = []
            expense_cost=[]
            for i in range(30):
                dates.append(i+1)
            dates = tuple(dates)
            y_pos = np.arange(len(dates))

            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            for i in range(30):
                val = i+1
                cursor.execute("select sum(amount) from expense where day=? AND month=? AND year=?", (val,monthgot,yeargot))
                total_expense = cursor.fetchone()[0]
                if total_expense == None:
                    total_expense = 0 
                expense_cost.append(total_expense)

            print("ob1"  + str(dates[0]))

            plt.bar(y_pos, expense_cost, align='center', alpha=0.5)
            plt.xticks(y_pos, dates)
            plt.ylabel('Expense Cost')
            plt.xlabel('Date')
            plt.title('Day Wise Expense Analysis')
            figManager = plt.get_current_fig_manager()
            figManager.full_screen_toggle()
            plt.show()


        def AllinOne():
            monthgot = printmonth()
            yeargot = printyear()
            if monthgot == "stop" or yeargot == "stop":
                messagebox.showinfo("Attention!","Month/Year Should be a number and not text or any Special Character!\nEntry Not Saved. Try Again!")
                return "stopped"
            bar.destroy()
            draw(monthgot,yeargot)
        sbutton = ttk.Button(labelframe2, text = 'Continue',command = AllinOne) 
        sbutton.grid(row=7,column = 0, pady=4)
        
    btn1 = ttk.Button(labelframe1, text = 'Daywise Expense Analysis', command = barexpense) 
    btn1.grid(row = 4,column = 1, pady = 2)

# ===================================================================================================

    def barincome():
        bar = ThemedTk(theme = ttk_theme, themebg = True)
        bar.resizable(False, False)
        bar.title('Set Month and Year')
        labelframe2 = ttk.LabelFrame(bar, text="Set Month and Year")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe2, text="Please provide the following: ", width=30, font=("bold", 10))  
        rootlabel.grid(row=2,column = 0,columnspan = 4,padx = 10, pady=4)

        label_1 = ttk.Label(labelframe2, text="Enter Month(Between 1-12): ",width=30,font=("bold", 10))
        label_1.configure(anchor="center") 
        label_1.grid(row=3,column = 0,columnspan = 4, pady=4)

        entry_1 = Entry(labelframe2, bd=5)
        entry_1.grid(row=4,column = 0, pady=4)

        def printmonth():
            s = entry_1.get()
            if s.isdigit():
                print('Month: ' + s)
                return s           
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"
        
        label_2 = ttk.Label(labelframe2, text="Enter Year",width=30,font=("bold", 10))
        label_2.configure(anchor="center") 
        label_2.grid(row=5,column = 0, pady=4)

        entry_2 = Entry(labelframe2, bd=5)
        entry_2.grid(row=6,column = 0, pady=4)
        def printyear():
            s = entry_2.get()
            if s.isdigit():
                print('Year: ' + s)
                return s          
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"
        
        def draw(monthgot,yeargot):
            dates = []
            expense_cost=[]
            for i in range(30):
                dates.append(i+1)
            dates = tuple(dates)
            y_pos = np.arange(len(dates))

            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            for i in range(30):
                val = i+1
                cursor.execute("select sum(amount) from income where day=? AND month=? AND year=?", (val,monthgot,yeargot))
                total_expense = cursor.fetchone()[0]
                if total_expense == None:
                    total_expense = 0 
                expense_cost.append(total_expense)

            plt.bar(y_pos, expense_cost, align='center', alpha=0.5)
            plt.xticks(y_pos, dates)
            plt.ylabel('Expense Cost')
            plt.xlabel('Date')
            plt.title('Day Wise Income Analysis')
            figManager = plt.get_current_fig_manager()
            figManager.full_screen_toggle()
            plt.show()


        def AllinOne():
            monthgot = printmonth()
            yeargot = printyear()
            if monthgot == "stop" or yeargot == "stop":
                messagebox.showinfo("Attention!","Month/Year Should be a number and not text or any Special Character!\nEntry Not Saved. Try Again!")
                return "stopped"
            bar.destroy()
            draw(monthgot,yeargot)
        sbutton = ttk.Button(labelframe2, text = 'Continue',command = AllinOne) 
        sbutton.grid(row=7,column = 0, pady=4)

    btn1 = ttk.Button(labelframe1, text = 'Daywise Income Analysis', command = barincome) 
    btn1.grid(row = 5,column = 1, pady = 2)