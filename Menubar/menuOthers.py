from tkinter import *  
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from ttkthemes import ThemedTk
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import PIL.Image
from tkhtmlview import HTMLLabel
import webbrowser


def callback(url):
    webbrowser.open_new(url)


def callmenuOther(menubar):
    def AboutUs():
        AboutUs = ThemedTk(theme = "xpnative", themebg = True)
        AboutUs.geometry('330x150')
        AboutUs.title('About Us')
        rootlabel = ttk.Label(AboutUs, text="We are CSE Undergrads and Enthusiast Developers.",font=("bold", 10))
        rootlabel.configure(anchor="center") 
        rootlabel.grid()
        rootlabel = ttk.Label(AboutUs, text="This Application is made by : \n -- Akshat Gandhi \n -- Rugved Bongale \n -- Tushar Bapecha \n\n", width=30,font=("bold", 10))
        rootlabel.configure(anchor="center") 
        rootlabel.grid()

    def FeedBack():
        print("Feedback here")
        FeedBack = ThemedTk(theme = "xpnative", themebg = True)
        FeedBack.title("Feedback")
        FeedBack.geometry('300x150')
        FeedBackLabel = ttk.Label(FeedBack, text="We are always open to feedback :)",width=30,font=("bold", 10))
        FeedBackLabel.configure(anchor="center")  
        FeedBackLabel.place(x = 30, y = 20)
        link1 = Label(FeedBack, text="Click here to give feedback",width=30,font=("bold", 10), fg="blue", cursor="hand2")
        link1.configure(anchor="center")
        link1.place(x = 30, y = 50)
        link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))

    def UserM():
        print("User Manual here")
        FeedBack = ThemedTk(theme = "xpnative", themebg = True)
        FeedBack.title("Help")
        FeedBack.geometry('300x150')
        FeedBackLabel = ttk.Label(FeedBack, text="To get help in using this Application \nrefer the following UserManual",width=30,font=("bold", 10))
        FeedBackLabel.configure(anchor="center")  
        FeedBackLabel.place(x = 30, y = 20,)
        link1 = Label(FeedBack, text="Click here",width=30,font=("bold", 10), fg="blue", cursor="hand2")
        link1.configure(anchor="center")
        link1.place(x = 30, y = 65)
        link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))


    othersmenu = Menu(menubar, tearoff = 0, activeborderwidth = 3, bd = 3)
    othersmenu.add_command(label = "Feedback!", command = FeedBack)
    othersmenu.add_command(label = "About us", command = AboutUs)
    othersmenu.add_command(label = "Help", command = UserM)

    menubar.add_cascade(label = "Others", menu = othersmenu)