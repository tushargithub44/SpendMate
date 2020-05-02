from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
import sqlite3

sum_expense=0
sum_amount=0
sum_total=0
db = sqlite3.connect('myspendmate.db')
cursor = db.cursor()
cursor.execute("select sum(amount) from incomeee")
sum1 = cursor.fetchone()[0]
if(sum1=='None'):
    sum1=str(0)
sum_total = sum1
print("sum:"+str(sum_total))
cate_cont=[]
cate_cont_per=[]
count=-1
cate_list=[]
cursor.execute("SELECT * FROM incomeee")
list12=cursor.fetchall()
for j in list12:
    print(j[3])
    category=str(j[3])
    amtt=int(j[0])
    if cate_list.count(category)==0:
        cate_list.append(category)
        count=count+1
        sum_cate=amtt
        cate_cont.append(sum_cate)
        sum_cate= float((sum_cate/sum_total)*100)
        cate_cont_per.append(sum_cate)
        
    else:
        cate_cont[count]= cate_cont[count]+amtt
        sum_cate = cate_cont[count]
        sum_cate= float((sum_cate/sum_total)*100)
        cate_cont_per[count]=sum_cate


print(cate_list)
print(cate_cont)
print(cate_cont_per)

    

    
    


month_name=['jan','feb','mar','apr','may']
lis=[]
expens=[]

for i in range(1,5):
    cursor.execute("select sum(amount) from incomeee where month= '%d'"%i)
    sum_mon=cursor.fetchone()[0]
    st=str(sum_mon)
    print("Initial:"+st)
   
    
    if(st == 'None'):
        st=str(0)
    print("price:"+st)
    if sum_total==0:
        lis.append(month_name[i])
        perc=0.0
        expens.append(perc)
    else:
        perc =float((int(st)/sum_total)*100)
        print("per:"+str(perc))
        print(st)
        lis.append(month_name[i])
        expens.append(perc)
    




for i in expens:
    print(i)
    print("h")

    
cursor.close()
db.commit()
db.close()


def callAnalysis(root):
    labelframe1 = LabelFrame(root, text="Positive Comments")  
    labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Place to put the positive comments")  
    rootlabel.grid()  

    def printpie():
        # Data to plot
        
        labels = cate_list
        sizes = cate_cont_per
        colors = ['gold']
        explode = (0)  # explode 1st slice

        # Plot
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

        plt.axis('equal')
        plt.show()

    btn1 = Button(labelframe1, text = 'Daily Expense Analysis', command = printpie) 
    btn1.grid()

    btn1 = Button(labelframe1, text = 'Expense Analysis') 
    btn1.grid()

    btn1 = Button(labelframe1, text = 'Income Analysis') 
    btn1.grid()