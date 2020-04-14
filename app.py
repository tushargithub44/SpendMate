from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
root = Tk()  
root.geometry("900x600")  
  

tlabel = Label(root, text="Welcome to SpendMate")  
tlabel.grid(columnspan = 12,pady = 2)  
tlabel.config(font=("ubuntu", 25))

def hello():  
    print("hello!")


menubar = Menu(root)  
# menubar.add_command(label="Hello!", command=hello)  
# menubar.add_command(label="Quit!", command=root.quit)  


# ---------------- FUNCTION MENU---------------------------------------

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

#----------------------------------------------------------------------

#-----------------OTHERS MENU------------------------------------------

def AboutUs():
    print("About us")

def FeedBack():
    print("Feedback here")


othersmenu = Menu(menubar, tearoff = 0)
othersmenu.add_command(label = "Feedback!", command = FeedBack)
othersmenu.add_command(label = "About us", command = AboutUs)

menubar.add_cascade(label = "Others", menu = othersmenu)

#----------------------------------------------------------------------

root.config(menu=menubar)  

#----------------------------------------------------------------------


labelframe1 = LabelFrame(root, text="Balance Comments")  
labelframe1.grid(row=1,column = 0,columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
rootlabel = Label(labelframe1, text="Your Current Balance is : ")  
rootlabel.grid(pady = 10)  

# btn1 = Button(labelframe1, text = 'Button 1') 
# btn1.grid(padx=10, pady=10)

#-----------------------------INCOME SECTION-------------------------------------



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
  
rootlabel = Label(labelframe2, text="Total Income : ")  
rootlabel.grid()  

btn1 = Button(labelframe2, text = 'Add Income',command = AddIncome) 
btn1.grid()

#---------------------------------------------------------------------------------

#-----------------------------EXPENSE SECTION-------------------------------------

labelframe1 = LabelFrame(root, text="Expense Comments")  
labelframe1.grid(row=1,column = 6, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
rootlabel = Label(labelframe1, text="Total Expense : ")  
rootlabel.grid()  

btn1 = Button(labelframe1, text = 'Add Expense') 
btn1.grid()

#---------------------------------------------------------------------------------

labelframe1 = LabelFrame(root, text="Positive Comments")  
labelframe1.grid(row=3,column = 0, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
rootlabel = Label(labelframe1, text="Place to put the positive comments")  
rootlabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()



labelframe1 = LabelFrame(root, text="Positive Comments")  
labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
rootlabel = Label(labelframe1, text="Place to put the positive comments")  
rootlabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()



labelframe1 = LabelFrame(root, text="Positive Comments")  
labelframe1.grid(row=3,column = 6, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
rootlabel = Label(labelframe1, text="Place to put the positive comments")  
rootlabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()




# btn3 = Button(root, text = 'Button 1') 
# btn3.grid(row = 0, column = 3)


 
# labelframe2 = LabelFrame(root, text = "Negative Comments")  
# labelframe2.pack(fill="both", expand = "yes")  
  
# bottomlabel = Label(labelframe2,text = "Place to put the negative comments")  
# bottomlabel.pack()  
  

# root.rowconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)

root.mainloop()