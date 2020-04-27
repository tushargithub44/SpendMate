from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt

def callExpense(root):
    def AddExpense():
        expense = Tk()
        expense.geometry('500x500')
        expense.title("Add Income")

        label_1 = Label(expense, text="Enter Amount",width=20,font=("bold", 10))
        label_1.place(x=60,y=60)

        entry_1 = Entry(expense, bd=5)
        entry_1.place(x=240,y=60)
        def printamount():
            s = entry_1.get()
            print('Amount: ' + s)
        
        label_2 = Label(expense, text="Select Date",width=20,font=("bold", 10))
        label_2.place(x=60,y=120)
        def dateSelector():
                def print_sel():
                    dateselected = cal.selection_get()
                    print(dateselected)
                    labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
                    label_3 = Label(expense, text=dateselected,width=20,font=("bold", 10))
                    label_3.place(x=310,y=120)
                    cal.see(datetime.date(year=2016, month=2, day=5))
                    return dateselected

                top = Toplevel(expense)
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
                expensebtn2 = Button(top, text="Select", command=print_sel).pack() 
                
                # tk.top.destroy()



        expensebtn = Button(expense, text='Enter Date', command = dateSelector)
        expensebtn.place(x=240,y=120)

        label_1 = Label(expense, text="Description",width=20,font=("bold", 10))
        label_1.place(x=60,y=180)

        entry_2 = Entry(expense,bd = 5)
        entry_2.place(x=240,y=180)
        def printdescription():
            s2 = entry_2.get()
            print('Description: ' + s2)

        label_1 = Label(expense, text="Category",width=20,font=("bold", 10))
        label_1.place(x=60,y=240)

        def printcategory():
            print('Category: ' + cb.get())

        Category=["Salary","Year Bonus","FDR"]
        cb = ttk.Combobox(expense,values=Category,width=10)
        cb.place(x = 240,y= 240)
        cb.current(0)

        label_1 = Label(expense, text="Account",width=20,font=("bold", 10))
        label_1.place(x=60,y=300)

        def printaccount():
            print('Account: ' + accountbox.get())

        Account=["Cash","Card","Paytm"]
        accountbox = ttk.Combobox(expense,values=Account,width=10)
        accountbox.place(x = 240,y= 300)
        accountbox.current(0)

        # label_1 = Label(expense, text="Payment Recieved?",width=20,font=("bold", 10))
        # label_1.place(x=60,y=360)
        def expenseexit():
            expense.destroy()

        def AllinOne():
            printamount()
            printdescription()
            printcategory()
            printaccount()
            expenseexit()
            pass 

        savebutton = Button(expense, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
        savebutton.place(x = 180, y = 350)
    labelframe1 = LabelFrame(root, text="Expense Comments")  
    labelframe1.grid(row=1,column = 6, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Total Expense : ")  
    rootlabel.grid()  

    btn1 = Button(labelframe1, text = 'Add Expense', command = AddExpense) 
    btn1.grid()
