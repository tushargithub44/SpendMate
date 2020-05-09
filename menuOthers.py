from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt
from tkhtmlview import HTMLLabel
import webbrowser


def callback(url):
    webbrowser.open_new(url)


def callmenuOther(menubar):
    def AboutUs():
        AboutUs = Tk()
        AboutUs.geometry('300x200')
        AboutUs.title('About Us')
        rootlabel = Label(AboutUs, text="We are Enthusiast CS Undergrads.", width=30,font=("bold", 10))
        rootlabel.configure(anchor="center") 
        rootlabel.grid()
        rootlabel = Label(AboutUs, text="This Application is made by : \n -- Akshat Gandhi \n -- Rugved Bongale \n -- Tushar Bapecha", width=30,font=("bold", 10))
        rootlabel.configure(anchor="center") 
        rootlabel.grid()

    def FeedBack():
        print("Feedback here")
        FeedBack = Tk()
        FeedBack.title("Feedback")
        FeedBack.geometry('300x150')
        FeedBackLabel = Label(FeedBack, text="We are always open to feedback :)",width=30,font=("bold", 10))
        FeedBackLabel.configure(anchor="center")  
        FeedBackLabel.place(x = 30, y = 20)
        link1 = Label(FeedBack, text="Click here",width=30,font=("bold", 10), fg="blue", cursor="hand2")
        link1.configure(anchor="center")
        link1.place(x = 30, y = 50)
        link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))


    othersmenu = Menu(menubar, tearoff = 0)
    othersmenu.add_command(label = "Feedback!", command = FeedBack)
    othersmenu.add_command(label = "About us", command = AboutUs)

    menubar.add_cascade(label = "Others", menu = othersmenu)