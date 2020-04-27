from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt


def callincome(root):
    def AddIncome():
        income = Tk()
        income.geometry('500x500')
        income.title("Add Income")

        label_1 = Label(income, text="Enter Amount",width=20,font=("bold", 10))
        label_1.place(x=60,y=60)

        entry_1 = Entry(income, bd=5)
        entry_1.place(x=240,y=60)
        def printamount():
            s = entry_1.get()
            print('Amount: ' + s)
        
        label_2 = Label(income, text="Select Date",width=20,font=("bold", 10))
        label_2.place(x=60,y=120)
        def dateSelector():
                def print_sel():
                    dateselected = cal.selection_get()
                    print(dateselected)
                    labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                    label_3 = Label(income, text=dateselected,width=20,font=("bold", 10))
                    label_3.place(x=310,y=120)
                    cal.see(datetime.date(year=2016, month=2, day=5))
                    return dateselected

                top = Toplevel(income)
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



        incomebtn = Button(income, text='Enter Date', command = dateSelector)
        incomebtn.place(x=240,y=120)

        label_1 = Label(income, text="Description",width=20,font=("bold", 10))
        label_1.place(x=60,y=180)

        entry_2 = Entry(income,bd = 5)
        entry_2.place(x=240,y=180)
        def printdescription():
            s2 = entry_2.get()
            print('Description: ' + s2)

        label_1 = Label(income, text="Category",width=20,font=("bold", 10))
        label_1.place(x=60,y=240)

        def printcategory():
            print('Category: ' + cb.get())

        Category=["Salary","Year Bonus","FDR"]
        cb = ttk.Combobox(income,values=Category,width=10)
        cb.place(x = 240,y= 240)
        cb.current(0)

        label_1 = Label(income, text="Account",width=20,font=("bold", 10))
        label_1.place(x=60,y=300)

        def printaccount():
            print('Account: ' + accountbox.get())

        Account=["Cash","Card","Paytm"]
        accountbox = ttk.Combobox(income,values=Account,width=10)
        accountbox.place(x = 240,y= 300)
        accountbox.current(0)

        # label_1 = Label(income, text="Payment Recieved?",width=20,font=("bold", 10))
        # label_1.place(x=60,y=360)
        def incomeexit():
            income.destroy()

        def AllinOne():
            printamount()
            printdescription()
            printcategory()
            printaccount()
            incomeexit()
            pass 

        savebutton = Button(income, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
        savebutton.place(x = 180, y = 350)

    labelframe2 = LabelFrame(root, text="Income Comments")  
    labelframe2.grid(row=1,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  


    # -------------------------Income Main window Section---------------------
    rootlabel = Label(labelframe2, text="Total Income : ")  
    rootlabel.grid()  

    btn1 = Button(labelframe2, text = 'Add Income',command = AddIncome) 
    btn1.grid()