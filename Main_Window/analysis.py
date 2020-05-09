from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import sqlite3



def callAnalysis(root):
    labelframe1 = LabelFrame(root, text="Positive Comments")  
    labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Place to put the positive comments")  
    rootlabel.grid()  

    def displaypie():
        # Data to plot
        
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

        # colors_all = []
        # colors = []
        # for j in count:
        #     colors.append()

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

    btn1 = Button(labelframe1, text = 'Categorywise Expense Analysis', command = displaypie) 
    btn1.grid()

    def displaypie2():
        # Data to plot
        
        db = sqlite3.connect('myspendmate.db')
        cursor = db.cursor()
        cursor.execute(" select sum(amount) from income")
        total_expense = cursor.fetchone()[0]
        if total_expense == None:
            total_expense = 0 
        cursor.execute("select * from income")
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

        # colors_all = []
        # colors = []
        # for j in count:
        #     colors.append()

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

    btn1 = Button(labelframe1, text = 'Categorywise Income Analysis', command = displaypie2) 
    btn1.grid()

    def barexpense():
        bar = Tk()
        label_1 = Label(bar, text="Enter Month (Between 1-12)",width=20,font=("bold", 10))
        label_1.grid()

        entry_1 = Entry(bar, bd=5)
        entry_1.grid()
        def printmonth():
            s = entry_1.get()
            print('Month: ' + s)
            return s
        
        label_2 = Label(bar, text="Enter Year",width=20,font=("bold", 10))
        label_2.grid()

        entry_2 = Entry(bar, bd=5)
        entry_2.grid()
        def printyear():
            s = entry_2.get()
            print('Year: ' + s)
            return s
        
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
            yeargot = int(printyear())
            bar.destroy()
            draw(monthgot,yeargot)
        sbutton = Button(bar, text = 'Continue',command = AllinOne, padx=20, pady=20) 
        sbutton.grid()
        
    btn1 = Button(labelframe1, text = 'Day Wise Expense Analysis', command = barexpense) 
    btn1.grid()

    def barincome():
        bar = Tk()
        label_1 = Label(bar, text="Enter Month (Between 1-12)",width=20,font=("bold", 10))
        label_1.grid()

        entry_1 = Entry(bar, bd=5)
        entry_1.grid()
        def printmonth():
            s = entry_1.get()
            print('Month: ' + s)
            return s
        
        label_2 = Label(bar, text="Enter Year",width=20,font=("bold", 10))
        label_2.grid()

        entry_2 = Entry(bar, bd=5)
        entry_2.grid()
        def printyear():
            s = entry_2.get()
            print('Year: ' + s)
            return s
        
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
            yeargot = int(printyear())
            bar.destroy()
            draw(monthgot,yeargot)
        sbutton = Button(bar, text = 'Continue',command = AllinOne, padx=20, pady=20) 
        sbutton.grid()

    btn1 = Button(labelframe1, text = 'Day Wise Income Analysis', command = barincome) 
    btn1.grid()