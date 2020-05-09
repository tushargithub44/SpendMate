from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3
from balance import *

date_selected=None

def callGoals(root):
    labelframe1 = LabelFrame(root, text="Manage your Goals here")  
    labelframe1.grid(row=3,column = 6, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    db = sqlite3.connect('myspendmate.db')
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM goals;")  # (name TEXT NOT NULL, enddate TEXT NOT NULL, target_value INT NOT NULL, current_value INT NOT NULL, description TEXT,day INT NOT NULL,month INT NOT NULL,year INT NOT NULL)"
    countgoals = cursor.fetchone()[0]
    if(countgoals=='None'):
        countgoals=str(0)
    rootlabel = Label(labelframe1, text="Total Goals : ") 
    rootlabel.grid(row=3,column = 0)
    rootlabel1 = Label(labelframe1, text=str(countgoals)) 
    rootlabel1.grid(row=3,column = 1)
    rootlabel1.config(font=("Courier", 13))  
    cursor.close()
    db.commit()
    db.close   

    # def ManageGoals():
        # Goals = Tk()
        # Goals.geometry('300x300')
        # Goals.title("Manage Budget")

        # label_1 = Label(Goals, text="Your Goals",width=20,font=("bold", 10))
        # label_1.place(x=170,y=20)
    
    def SeeGoals():
        seegoals = Tk()

        def Modifyit():
            selected_item = tv.selection()[0] ## get selected item
            print(tv.selection)
            curItem = tv.focus()
            print('-------------------going in--------------------')
            qas = tv.item(curItem)
            name = qas['values'][0]
            newwin = Tk()
            label_1 = Label(newwin, text="Goal Name : ",width=20,font=("bold", 10))
            label_1.grid(column = 0, row = 0)
            label_1 = Label(newwin, text=str(name),width=20,font=("bold", 10))
            label_1.grid(column = 1, row = 0)
            label_1 = Label(newwin, text="New Current value",width=20,font=("bold", 10))
            label_1.grid(column = 0, row = 1)
            entry_1 = Entry(newwin, bd=5)
            entry_1.grid(column = 1, row = 1)   
            
            def change():
                value = entry_1.get()
                print('value' + str(value))
                db = sqlite3.connect('myspendmate.db')
                cursor = db.cursor()
                cursor.execute("update goals set current_value=? where name=?", (value,name))
                cursor.close()
                db.commit()
                db.close()
                newwin.destroy()
            changebtn = Button(newwin, text="Save Changes",command = change)
            # changebtn.grid(column = 1, row = 3)
            changebtn.grid(row=2, columnspan = 2)
            print(qas['values'][0])
            print('-------------------going out-------------------')
            print(tv.item(curItem))
            seegoals.destroy()

        def deleteit():
            selected_item = tv.selection()[0] ## get selected item
            print(tv.selection)
            curItem = tv.focus()
            print('-------------------going in--------------------')
            qas = tv.item(curItem)
            Goal_name = qas['values'][0]
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("delete from goals where name=?", (Goal_name,))
            cursor.close()
            db.commit()
            db.close()
            print(qas['values'][0])
            print('-------------------going out-------------------')
            # print(tv.item(curItem))
            tv.delete(selected_item)
            seegoals.destroy()
            
        def selectItem(a):
            curItem = tv.focus()
            # print(tv.item(curItem))

        button_del = Button(seegoals, text="Delete entry", command=deleteit)
        button_del.pack()
        button_del = Button(seegoals, text="Modify Current Value for a Goal", command=Modifyit)
        button_del.pack()
        label_1 = Label(seegoals, text="**Note: Make sure to select a goal before any operation",width=20,font='Helvetica 10 bold')
        label_1.pack(expand=1, fill=tk.X)
        gframe = Frame(seegoals)
        gframe.pack(padx=20)
        tv=ttk.Treeview(gframe,columns=(1,2,3,4,5) ,show="headings", height ='30')
        tv.pack()
        # scrlbar = ttk.Scrollbar(seegoals,  
        #                orient ="vertical",  
        #                command = tv.yview) 
        
        # scrlbar.pack(side ='right', fill ='x')
        # tv.configure(xscrollcommand = scrlbar.set)

        tv.heading(1,text="Goal Name")
        tv.heading(2,text="Date")
        tv.heading(3,text="Goal Target Value")
        tv.heading(4,text="Current Value")
        tv.heading(5,text="Description")
        
        seegoals.title("Your Goals")
        db = sqlite3.connect('myspendmate.db')
        cursor = db.cursor()
        cursor.execute("SELECT * FROM goals ")
        list1 = cursor.fetchall()
        total = cursor.rowcount
        
        for i in list1:
            tv.insert('','end',values=i)

        cursor.close()
        db.commit()
        db.close
        print(list1)
        # tv.bind("<ButtonRelease-1>", deleteit)
        tv.bind('<ButtonRelease-1>', selectItem)
        seegoals.mainloop()



    def SetGoals():
        ingoal = Tk()
        ingoal.geometry('500x500')
        ingoal.title("Add Income")

        label_1 = Label(ingoal, text="Goal Name",width=20,font=("bold", 10))
        label_1.place(x=60,y=60)

        entry_1 = Entry(ingoal, bd=5)
        entry_1.place(x=240,y=60)
        def printamount():
            s = entry_1.get()
            print('Goal Name: ' + s)
            return s
        
        label_2 = Label(ingoal, text="Select End Date",width=20,font=("bold", 10))
        label_2.place(x=60,y=120)

        def dateSelector():
                def print_sel():
                    global date_selected
                    dateselected = cal.selection_get()
                    date_selected = dateselected
                    print(dateselected)
                    labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                    label_3 = Label(ingoal, text=dateselected,width=20,font=("bold", 10))
                    label_3.place(x=330,y=120)
                    cal.see(datetime.date(year=2016, month=2, day=5))
                    return dateselected

                top = Toplevel(ingoal)
                # top.geometry('500x500')
                import datetime
                today = datetime.date.today()

                mindate = datetime.date(year=2018, month=1, day=21)
                maxdate = today + datetime.timedelta(days=5)
                # print(mindate, maxdate)

                cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            cursor="hand1", year=2018, month=2, day=5)
                cal.pack(fill="both", expand=True)
                incomebtn2 = Button(top, text="Select", command=print_sel).pack() 
                
                # tk.top.destroy()



        incomebtn = Button(ingoal, text='Enter End Date', command = dateSelector)
        incomebtn.place(x=240,y=120)

        label_1 = Label(ingoal, text="Goal Target Value",width=20,font=("bold", 10))
        label_1.place(x=60,y=180)

        entry_2 = Entry(ingoal,bd = 5)
        entry_2.place(x=240,y=180)
        def printdescription():
            s2 = entry_2.get()
            print('Goal Value: ' + s2)
            return s2

        label_1 = Label(ingoal, text="Current Value",width=20,font=("bold", 10))
        label_1.place(x=60,y=240)

        entry_3 = Entry(ingoal,bd = 5)
        entry_3.place(x=240,y=240)
        def printcategory():
            s3 = entry_3.get()
            print('Initial Value: ' + s3)
            return s3

        label_1 = Label(ingoal, text="Description",width=20,font=("bold", 10))
        label_1.place(x=60,y=300)

        entry_4 = Entry(ingoal,bd = 5)
        entry_4.place(x=240,y=300)
        def printaccount():
            s3 = entry_4.get()
            print('Description: ' + s3)
            return s3


        def put():
            t1 = printamount()
            t2 = printdescription()
            t3 = printcategory()
            t4 = printaccount()
            t5 = date_selected
            print('date selected' + str(t5))
            info = str(t5)
            day = info[8]+info[9]
            mon = info[5]+info[6]
            yr = info[0]+info[1]+info[2]+info[3]
            print('day ' + str(day))
            print('mon ' + str(mon))
            print('yr ' + str(yr))
            db = sqlite3.connect('myspendmate.db')
            cursor = db.cursor()
            cursor.execute("insert into goals values('%s','%s','%d','%d','%s','%d','%d','%d')"%(str(t1),str(t5),int(t2),int(t3),t4,int(day),int(mon),int(yr)))
            cursor.execute("SELECT COUNT(*) FROM goals;")  # (name TEXT NOT NULL, enddate TEXT NOT NULL, target_value INT NOT NULL, current_value INT NOT NULL, description TEXT,day INT NOT NULL,month INT NOT NULL,year INT NOT NULL)"
            countgoals = cursor.fetchone()[0]
            if(countgoals=='None'):
                countgoals=str(0)
            rootlabel1.config(text=str(countgoals))
            cursor.close()
            db.commit()
            db.close

        # label_1 = Label(income, text="Payment Recieved?",width=20,font=("bold", 10))
        # label_1.place(x=60,y=360)
        def incomeexit():
            ingoal.destroy()

        def AllinOne():
            # printamount()
            # printdescription()
            # printcategory()
            # printaccount()
            put()

            incomeexit()
            pass 

        savebutton = Button(ingoal, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
        savebutton.place(x = 180, y = 350)


        # seegoalbtn = Button(Goals, text = 'See Your Goals', command = SeeGoals) 
        # seegoalbtn.pack()

        # addgoalbtn = Button(Goals, text = 'Add a Goal', command = SetGoals) 
        # addgoalbtn.pack()

        # progress = Progressbar(root, orient = HORIZONTAL, 
        #         length = 100, mode = 'indeterminate') 
        # progress['value'] = 20



    # btn1 = Button(labelframe1, text = 'Manage Goals', command = ManageGoals) 
    # btn1.grid()
    seegoalbtn = Button(labelframe1, text = 'See Your Goals', command = SeeGoals) 
    seegoalbtn.grid(row = 4, column = 0,padx=2)

    addgoalbtn = Button(labelframe1, text = 'Add a Goal', command = SetGoals) 
    addgoalbtn.grid(row = 4, column = 1,padx=2)
