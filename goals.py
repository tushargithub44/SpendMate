from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt


def callGoals(root):
    labelframe1 = LabelFrame(root, text="Positive Comments")  
    labelframe1.grid(row=3,column = 6, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Place to put the positive comments")  
    rootlabel.grid()  

    def ManageGoals():
        Goals = Tk()
        Goals.geometry('500x500')
        Goals.title("Manage Budget")

        label_1 = Label(Goals, text="Your Goals",width=20,font=("bold", 10))
        label_1.place(x=170,y=20)

        
        def SetGoals():
            print('hello')
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
            
            label_2 = Label(ingoal, text="Select End Date",width=20,font=("bold", 10))
            label_2.place(x=60,y=120)
            def dateSelector():
                    def print_sel():
                        dateselected = cal.selection_get()
                        print(dateselected)
                        labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                        label_3 = Label(ingoal, text=dateselected,width=20,font=("bold", 10))
                        label_3.place(x=310,y=120)
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

            label_1 = Label(ingoal, text="Current Value",width=20,font=("bold", 10))
            label_1.place(x=60,y=240)

            entry_3 = Entry(ingoal,bd = 5)
            entry_3.place(x=240,y=240)
            def printcategory():
                s3 = entry_3.get()
                print('Initial Value: ' + s3)

            label_1 = Label(ingoal, text="Description",width=20,font=("bold", 10))
            label_1.place(x=60,y=300)

            entry_4 = Entry(ingoal,bd = 5)
            entry_4.place(x=240,y=300)
            def printaccount():
                s3 = entry_4.get()
                print('Description: ' + s3)

            # label_1 = Label(income, text="Payment Recieved?",width=20,font=("bold", 10))
            # label_1.place(x=60,y=360)
            def incomeexit():
                ingoal.destroy()

            def AllinOne():
                printamount()
                printdescription()
                printcategory()
                printaccount()
                incomeexit()
                pass 

            savebutton = Button(ingoal, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
            savebutton.place(x = 180, y = 350)


        addgoalbtn = Button(Goals, text = 'Add a Goals', command = SetGoals) 
        addgoalbtn.place(x = 190, y = 450)
        # progress = Progressbar(root, orient = HORIZONTAL, 
        #         length = 100, mode = 'indeterminate') 
        # progress['value'] = 20



    btn1 = Button(labelframe1, text = 'Goals', command = ManageGoals) 
    btn1.grid()
