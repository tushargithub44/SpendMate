from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import PIL.Image
import sqlite3
from Main_Window.balance import *
from Main_Window.theme import ttk_theme

date_selected=None

def callGoals(root):
    labelframe1 = ttk.LabelFrame(root, text="Manage your Goals here")  
    labelframe1.grid(row=3,column = 6, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    db = sqlite3.connect('myspendmate.db')
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM goals;") 
    countgoals = cursor.fetchone()[0]
    if(countgoals=='None'):
        countgoals=str(0)
    rootlabel = ttk.Label(labelframe1, text="Total Goals : ") 
    rootlabel.grid(row=3,column = 0)
    rootlabel1 = ttk.Label(labelframe1, text=str(countgoals)) 
    rootlabel1.grid(row=3,column = 1)
    rootlabel1.config(font=("Courier", 13))  
    cursor.close()
    db.commit()
    db.close   

    
    def SeeGoals():
        seegoals = ThemedTk(theme = ttk_theme, themebg = True)

        def Modifyit():
            selected_item = tv.selection()[0] ## get selected item
            print(tv.selection)
            curItem = tv.focus()
            print('-------------------going in--------------------')
            qas = tv.item(curItem)
            name = qas['values'][0]
            newwin = Tk()
            label_1 = ttk.Label(newwin, text="Goal Name : ",width=20,font=("bold", 10))
            label_1.grid(column = 0, row = 0)
            label_1 = ttk.Label(newwin, text=str(name),width=20,font=("bold", 10))
            label_1.grid(column = 1, row = 0)
            label_1 = ttk.Label(newwin, text="New Current Value : ",width=20,font=("bold", 10))
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
            changebtn = ttk.Button(newwin, text="Save Changes",command = change)
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
            callGoals(root)
            
        def selectItem(a):
            curItem = tv.focus()
            # print(tv.item(curItem))

        button_del = ttk.Button(seegoals, text="Delete entry", command=deleteit)
        button_del.pack()
        button_del = ttk.Button(seegoals, text="Modify Current Value for a Goal", command=Modifyit)
        button_del.pack()
        label_1 = ttk.Label(seegoals, text="**Note: Make sure to select a goal before any operation",width=20,font='Helvetica 10 bold')
        label_1.pack(expand=1, fill=tk.X)
        label_1.config(anchor="center")
        gframe = ttk.Frame(seegoals)
        gframe.pack(padx=20)
        tv=ttk.Treeview(gframe,columns=(1,2,3,4,5) ,show="headings", height ='30')
        tv.pack()
 

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
      
        tv.bind('<ButtonRelease-1>', selectItem)
        seegoals.mainloop()



    def SetGoals():
        ingoal = ThemedTk(theme = ttk_theme, themebg = True)
        ingoal.title("Add Goal")
        ingoal.resizable(False, False)
        labelframe_2 = ttk.LabelFrame(ingoal, text="Add Goal ")  
        labelframe_2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        rootlabel = ttk.Label(labelframe_2, text="Enter the following fields ", width=30, font=("bold", 10))  
        rootlabel.grid(row=2,column = 0,columnspan = 4,padx = 10, pady=4)

        label_1 = ttk.Label(labelframe_2, text="Goal Name (Max Char = 32)",width=30,font=("bold", 10))
        label_1.grid(row=3,column = 0,columnspan = 4, pady=4)

        entry_1 = Entry(labelframe_2, bd=5)
        entry_1.grid(row=3,column = 4, pady=4)

        def printamount():
            s = entry_1.get()
            print('Goal Name: ' + s)
            return s
        
        label_2 = ttk.Label(labelframe_2, text="Select Date",width=30,font=("bold", 10))
        label_2.grid(row=4,column = 0,columnspan = 4, pady=4)

        def dateSelector():
                def print_sel():
                    global date_selected
                    dateselected = cal.selection_get()
                    date_selected = dateselected
                    print(dateselected)
                    labelstatus = ttk.Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                    label_3 = ttk.Label(labelframe_2, text=dateselected,width=30,font=("bold", 10))
                    label_3.grid(row=4,column = 6, pady=4)
            
                    top.destroy()
                    return dateselected

                top = Toplevel(ingoal)
     
                import datetime
                today = datetime.date.today()

                mindate = datetime.date(year=2000, month=5, day=1)
                maxdate = today + datetime.timedelta(days=100)
        

                cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                            mindate=mindate, maxdate=maxdate, disabledforeground='red',
                            cursor="hand1", year=2020, month=5, day=5)
                cal.pack(fill="both", expand=True)
                incomebtn2 = ttk.Button(top, text="Select", command=print_sel).pack() 
                




        incomebtn = ttk.Button(labelframe_2, text='Enter Date', command = dateSelector)
        incomebtn.grid(row=4,column = 4, pady=4)

     
        label_1 = ttk.Label(labelframe_2, text="Goal Target Value",width=30,font=("bold", 10))
        label_1.grid(row=5,column = 0,columnspan = 4, pady=4)

        entry_2 = Entry(labelframe_2, bd=5)
        entry_2.grid(row=5,column = 4, pady=4)
        def printdescription():
            s2 = entry_2.get()
            if s2.isdigit():
                print('Goal Value: ' + s2)
                return s2
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"


        label_1 = ttk.Label(labelframe_2, text="Current Value",width=30,font=("bold", 10))
        label_1.grid(row=6,column=0,columnspan = 4, pady=4)

        entry_3 = Entry(labelframe_2,bd = 5)
        entry_3.grid(row=6,column = 4, pady=4)
        def printcategory():
            s3 = entry_3.get()
            if s3.isdigit():
                print('Initial Value: ' + s3)
                return s3
            else:
                entry_1.delete(0, END)
                entry_1.insert(0, "")
                return "stop"


        label_1 = ttk.Label(labelframe_2, text="Description",width=30,font=("bold", 10))
        label_1.grid(row=7,column=0,columnspan = 4, pady=4)

        entry_4 = Entry(labelframe_2,bd = 5)
        entry_4.grid(row=7,column = 4, pady=4)
        def printaccount():
            s3 = entry_4.get()
            print('Description: ' + s3)
            return s3


        def put():
            t1 = str(printamount())
            t2 = printdescription()
            t3 = printcategory()
            t4 = str(printaccount())
            if t3 == "stop" or t4 == "stop":
                messagebox.showinfo("Attention!","Value Should be a number and not text or any Special Character!\nEntry Not Saved. Try Again!")
                return "stopped"
            t5 = str(date_selected)
            if date_selected == None:
                messagebox.showinfo("Attention!","Date Field Should be not be empty.\nEntry Not Saved.\nPlease Select the Date and Try Again!")
                return "stopped"
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
            return "done"

        def incomeexit():
            ingoal.destroy()

        def AllinOne():


            status = put()
            if status == "done":
                messagebox.showinfo("Success!!","Goal Entry have been saved")
  
            incomeexit()
            pass 

        savebutton = ttk.Button(labelframe_2, text = 'Save and Exit',command = AllinOne) 
        savebutton.grid(row=8, column = 0, columnspan = 6, pady=4)


    seegoalbtn = ttk.Button(labelframe1, text = 'See Your Goals', command = SeeGoals) 
    seegoalbtn.grid(row = 5, column = 1,pady=4)

    addgoalbtn = ttk.Button(labelframe1, text = 'Add a Goal', command = SetGoals) 
    addgoalbtn.grid(row = 4, column = 1,pady=4)
