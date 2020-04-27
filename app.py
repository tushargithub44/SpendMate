from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
from balance import *
from income import *
from budget import *
from goals import *
from analysis import *
from expense import *
from menuFunctions import *
from menuOthers import *

root = Tk()  
root.geometry("900x600")  
  

tlabel = Label(root, text="Welcome to SpendMate")  
tlabel.grid(columnspan = 12,pady = 2)  
tlabel.config(font=("ubuntu", 25))


menubar = Menu(root)  


# ---------------- FUNCTION MENU---------------------------------------

callmenuFunc(menubar)

# def showCategories():
#     print("Categories!!!")

# def setCurrency():
#     print("Set Currency here!")

# def Backup():
#     print("Take Backup")

# def Reports():
#     print("Take Reports here!")

# functionmenu = Menu(menubar, tearoff = 0)
# functionmenu.add_command(label = "Categories",command = showCategories)
# functionmenu.add_command(label = "Set Currency",command = setCurrency)
# functionmenu.add_command(label = "Reports", command = Reports)
# functionmenu.add_command(label = "Backup", command = Backup)

# menubar.add_cascade(label = "Functions", menu = functionmenu)

#----------------------------------------------------------------------

#-----------------OTHERS MENU------------------------------------------

callmenuOther(menubar)

# def AboutUs():
#     print("About us")

# def FeedBack():
#     print("Feedback here")


# othersmenu = Menu(menubar, tearoff = 0)
# othersmenu.add_command(label = "Feedback!", command = FeedBack)
# othersmenu.add_command(label = "About us", command = AboutUs)

# menubar.add_cascade(label = "Others", menu = othersmenu)

#----------------------------------------------------------------------

root.config(menu=menubar)  

#----------------------------------------------------------------------

callbalance(root)

# labelframe1 = LabelFrame(root, text="Balance Comments")  
# labelframe1.grid(row=1,column = 0,columnspan=2, sticky='WE', \
#              padx=20, pady=20, ipadx=30, ipady=30)  
  
# rootlabel = Label(labelframe1, text="Your Current Balance is : ")  
# rootlabel.grid(pady = 10)  



#-----------------------------INCOME SECTION-------------------------------------

callincome(root)

# def AddIncome():
#     income = Tk()
#     income.geometry('500x500')
#     income.title("Add Income")

#     label_1 = Label(income, text="Enter Amount",width=20,font=("bold", 10))
#     label_1.place(x=60,y=60)

#     entry_1 = Entry(income, bd=5)
#     entry_1.place(x=240,y=60)
#     def printamount():
#         s = entry_1.get()
#         print('Amount: ' + s)
     
#     label_2 = Label(income, text="Select Date",width=20,font=("bold", 10))
#     label_2.place(x=60,y=120)
#     def dateSelector():
#             def print_sel():
#                 dateselected = cal.selection_get()
#                 print(dateselected)
#                 labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
#                 label_3 = Label(income, text=dateselected,width=20,font=("bold", 10))
#                 label_3.place(x=310,y=120)
#                 cal.see(datetime.date(year=2016, month=2, day=5))
#                 return dateselected

#             top = Toplevel(income)
#             # top.geometry('500x500')
#             import datetime
#             today = datetime.date.today()

#             mindate = datetime.date(year=2018, month=1, day=21)
#             maxdate = today + datetime.timedelta(days=5)
#             # print(mindate, maxdate)

#             cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
#                         mindate=mindate, maxdate=maxdate, disabledforeground='red',
#                         cursor="hand1", year=2018, month=2, day=5)
#             cal.pack(fill="both", expand=True)
#             incomebtn2 = Button(top, text="Select", command=print_sel).pack() 
            
#             # tk.top.destroy()



#     incomebtn = Button(income, text='Enter Date', command = dateSelector)
#     incomebtn.place(x=240,y=120)

#     label_1 = Label(income, text="Description",width=20,font=("bold", 10))
#     label_1.place(x=60,y=180)

#     entry_2 = Entry(income,bd = 5)
#     entry_2.place(x=240,y=180)
#     def printdescription():
#         s2 = entry_2.get()
#         print('Description: ' + s2)

#     label_1 = Label(income, text="Category",width=20,font=("bold", 10))
#     label_1.place(x=60,y=240)

#     def printcategory():
#         print('Category: ' + cb.get())

#     Category=["Salary","Year Bonus","FDR"]
#     cb = ttk.Combobox(income,values=Category,width=10)
#     cb.place(x = 240,y= 240)
#     cb.current(0)

#     label_1 = Label(income, text="Account",width=20,font=("bold", 10))
#     label_1.place(x=60,y=300)

#     def printaccount():
#         print('Account: ' + accountbox.get())

#     Account=["Cash","Card","Paytm"]
#     accountbox = ttk.Combobox(income,values=Account,width=10)
#     accountbox.place(x = 240,y= 300)
#     accountbox.current(0)

#     # label_1 = Label(income, text="Payment Recieved?",width=20,font=("bold", 10))
#     # label_1.place(x=60,y=360)
#     def incomeexit():
#         income.destroy()

#     def AllinOne():
#         printamount()
#         printdescription()
#         printcategory()
#         printaccount()
#         incomeexit()
#         pass 

#     savebutton = Button(income, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
#     savebutton.place(x = 180, y = 350)

# labelframe2 = LabelFrame(root, text="Income Comments")  
# labelframe2.grid(row=1,column = 3, columnspan=2, sticky='WE', \
#              padx=20, pady=20, ipadx=30, ipady=30)  


# # -------------------------Income Main window Section---------------------
# rootlabel = Label(labelframe2, text="Total Income : ")  
# rootlabel.grid()  

# btn1 = Button(labelframe2, text = 'Add Income',command = AddIncome) 
# btn1.grid()

#---------------------------------------------------------------------------------

#-----------------------------EXPENSE SECTION-------------------------------------

callExpense(root)
# labelframe1 = LabelFrame(root, text="Expense Comments")  
# labelframe1.grid(row=1,column = 6, columnspan=2, sticky='WE', \
#              padx=20, pady=20, ipadx=30, ipady=30)  
  
# rootlabel = Label(labelframe1, text="Total Expense : ")  
# rootlabel.grid()  

# btn1 = Button(labelframe1, text = 'Add Expense') 
# btn1.grid()

#---------------------------------------------------------------------------------

callBudget(root)

# budgetframe1 = LabelFrame(root, text="Budget Information")  
# budgetframe1.grid(row=3,column = 0, columnspan=2, sticky='WE', \
#              padx=20, pady=20, ipadx=30, ipady=30)  
  
# budgetlabel = Label(budgetframe1, text="Total Budget :")  
# budgetlabel.grid()  
# Spentlabel = Label(budgetframe1, text="Amount Spent :")  
# Spentlabel.grid() 

# def ManageBudget():
#     income = Tk()
#     income.geometry('400x250')
#     income.title("Manage Budget")

#     label_1 = Label(income, text="Set Budget Value",width=20,font=("bold", 10))
#     label_1.place(x=30,y=60)

#     entry_1 = Entry(income, bd=5)
#     entry_1.place(x=240,y=60)
#     def printamount():
#         s = entry_1.get()
#         print('Budget: ' + s)


#     label_2 = Label(income, text="Set Percentage to Notify:",width=20,font=("bold", 10))
#     label_2.place(x=30,y=120)

#     entry_2 = Entry(income, bd=5)
#     entry_2.place(x=240,y=120)
#     def printper():
#         s = int(entry_2.get())
#         if s>100 or s<0:
#             messagebox.showinfo("Title", "Invalid Percentage! Set Between 0 to 100")
#         print('Percentage: ' + str(s))

#     def printall():
#         printamount()
#         printper()
#     btn1 = Button(income, text = 'Set', command=printall) 
#     btn1.place(x = 150, y = 180)
    

# btn1 = Button(budgetframe1, text = 'Manage Budget', command=ManageBudget) 
# btn1.grid()



#---------------------------------------------------------------------------------
callAnalysis(root)
# labelframe1 = LabelFrame(root, text="Positive Comments")  
# labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
#              padx=20, pady=20, ipadx=30, ipady=30)  
  
# rootlabel = Label(labelframe1, text="Place to put the positive comments")  
# rootlabel.grid()  

# def printpie():
#     # Data to plot
#     labels = '', 'C++', 'Ruby', 'Java'
#     sizes = [215, 130, 245, 210]
#     colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
#     explode = (0.1, 0, 0, 0)  # explode 1st slice

#     # Plot
#     plt.pie(sizes, explode=explode, labels=labels, colors=colors,
#     autopct='%1.1f%%', shadow=True, startangle=140)

#     plt.axis('equal')
#     plt.show()

# btn1 = Button(labelframe1, text = 'Daily Expense Analysis', command = printpie) 
# btn1.grid()

# btn1 = Button(labelframe1, text = 'Expense Analysis') 
# btn1.grid()

# btn1 = Button(labelframe1, text = 'Income Analysis') 
# btn1.grid()

# ------------------------------GOALS SECTION BELOW---------------------------------------------

callGoals(root)

# labelframe1 = LabelFrame(root, text="Positive Comments")  
# labelframe1.grid(row=3,column = 6, columnspan=2, sticky='WE', \
#              padx=20, pady=20, ipadx=30, ipady=30)  
  
# rootlabel = Label(labelframe1, text="Place to put the positive comments")  
# rootlabel.grid()  

# def ManageGoals():
#     Goals = Tk()
#     Goals.geometry('500x500')
#     Goals.title("Manage Budget")

#     label_1 = Label(Goals, text="Your Goals",width=20,font=("bold", 10))
#     label_1.place(x=170,y=20)

    
#     def SetGoals():
#         print('hello')
#         ingoal = Tk()
#         ingoal.geometry('500x500')
#         ingoal.title("Add Income")

#         label_1 = Label(ingoal, text="Goal Name",width=20,font=("bold", 10))
#         label_1.place(x=60,y=60)

#         entry_1 = Entry(ingoal, bd=5)
#         entry_1.place(x=240,y=60)
#         def printamount():
#             s = entry_1.get()
#             print('Goal Name: ' + s)
        
#         label_2 = Label(ingoal, text="Select End Date",width=20,font=("bold", 10))
#         label_2.place(x=60,y=120)
#         def dateSelector():
#                 def print_sel():
#                     dateselected = cal.selection_get()
#                     print(dateselected)
#                     labelstatus = Label(top, text="Close this window.",width=20,font=("bold", 12)).pack()
#                     label_3 = Label(ingoal, text=dateselected,width=20,font=("bold", 10))
#                     label_3.place(x=310,y=120)
#                     cal.see(datetime.date(year=2016, month=2, day=5))
#                     return dateselected

#                 top = Toplevel(ingoal)
#                 # top.geometry('500x500')
#                 import datetime
#                 today = datetime.date.today()

#                 mindate = datetime.date(year=2018, month=1, day=21)
#                 maxdate = today + datetime.timedelta(days=5)
#                 # print(mindate, maxdate)

#                 cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
#                             mindate=mindate, maxdate=maxdate, disabledforeground='red',
#                             cursor="hand1", year=2018, month=2, day=5)
#                 cal.pack(fill="both", expand=True)
#                 incomebtn2 = Button(top, text="Select", command=print_sel).pack() 
                
#                 # tk.top.destroy()



#         incomebtn = Button(ingoal, text='Enter End Date', command = dateSelector)
#         incomebtn.place(x=240,y=120)

#         label_1 = Label(ingoal, text="Goal Target Value",width=20,font=("bold", 10))
#         label_1.place(x=60,y=180)

#         entry_2 = Entry(ingoal,bd = 5)
#         entry_2.place(x=240,y=180)
#         def printdescription():
#             s2 = entry_2.get()
#             print('Goal Value: ' + s2)

#         label_1 = Label(ingoal, text="Current Value",width=20,font=("bold", 10))
#         label_1.place(x=60,y=240)

#         entry_3 = Entry(ingoal,bd = 5)
#         entry_3.place(x=240,y=240)
#         def printcategory():
#             s3 = entry_3.get()
#             print('Initial Value: ' + s3)

#         label_1 = Label(ingoal, text="Description",width=20,font=("bold", 10))
#         label_1.place(x=60,y=300)

#         entry_4 = Entry(ingoal,bd = 5)
#         entry_4.place(x=240,y=300)
#         def printaccount():
#             s3 = entry_4.get()
#             print('Description: ' + s3)

#         # label_1 = Label(income, text="Payment Recieved?",width=20,font=("bold", 10))
#         # label_1.place(x=60,y=360)
#         def incomeexit():
#             ingoal.destroy()

#         def AllinOne():
#             printamount()
#             printdescription()
#             printcategory()
#             printaccount()
#             incomeexit()
#             pass 

#         savebutton = Button(ingoal, text = 'Save and Exit',command = AllinOne, padx=20, pady=20) 
#         savebutton.place(x = 180, y = 350)


#     addgoalbtn = Button(Goals, text = 'Add a Goals', command = SetGoals) 
#     addgoalbtn.place(x = 190, y = 450)
#     # progress = Progressbar(root, orient = HORIZONTAL, 
#     #         length = 100, mode = 'indeterminate') 
#     # progress['value'] = 20



# btn1 = Button(labelframe1, text = 'Goals', command = ManageGoals) 
# btn1.grid()

# ----------------------------------------------------------------------------------------



# btn3 = Button(root, text = 'Button 1') 
# btn3.grid(row = 0, column = 3)


 
# labelframe2 = LabelFrame(root, text = "Negative Comments")  
# labelframe2.pack(fill="both", expand = "yes")  
  
# bottomlabel = Label(labelframe2,text = "Place to put the negative comments")  
# bottomlabel.pack()  
  

# root.rowconfigure(1, weight=1)
# root.columnconfigure(2, weight=1)

root.mainloop()