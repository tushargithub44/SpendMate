from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt


def callmenuOther(menubar):
    def AboutUs():
        print("About us")

    def FeedBack():
        print("Feedback here")
        FeedBack = Tk()
        FeedBack.geometry('500x500')
        FeedBack.title("Feedback")

        label_1 = Label(FeedBack, text="We are always open to feedback :)",width=30,font=("bold", 10))
        label_1.configure(anchor="center")
        label_1.place(x=120,y=160)
        #label_1.pack(fill='both', expand=True)

        entry_1 = Text(FeedBack ,bd=5)
        #entry_1.pack(fill='side', expand=True)
        entry_1.place(x=80,y=200, height = 70,width = 320)

        def SaveFeedback():
            print(entry_1.get(1.0,END)) # Save this to feedback database
            FeedBack.destroy()
            messagebox.showinfo("Message","Thanks For Sharing Your Feedback!")  

        savebutton = Button(FeedBack, text = 'Done!',command = SaveFeedback, padx=20, pady=20) 
        savebutton.place(x = 180, y = 400)
        # savebutton.pack(fill='both', expand=True)


    othersmenu = Menu(menubar, tearoff = 0)
    othersmenu.add_command(label = "Feedback!", command = FeedBack)
    othersmenu.add_command(label = "About us", command = AboutUs)

    menubar.add_cascade(label = "Others", menu = othersmenu)