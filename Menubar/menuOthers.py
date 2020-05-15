from tkinter import *  
from tkinter import ttk
import tkinter as tk
from tkcalendar import Calendar, DateEntry
from ttkthemes import ThemedTk
from tkinter import messagebox
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import PIL.Image
import webbrowser
from Main_Window.theme import ttk_theme

def callback(url):
    webbrowser.open_new(url)


def callmenuOther(menubar):
    def AboutUs():
        AboutUs = ThemedTk(theme = ttk_theme, themebg = True)
        labelframe2 = ttk.LabelFrame(AboutUs, text="About us")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)

        AboutUs.title('About Us')
        rootlabel = ttk.Label(labelframe2, text="We are CSE Undergrads and Enthusiast Developers.",font=("bold", 10))
        rootlabel.configure(anchor="center") 
        rootlabel.grid()
        rootlabel = ttk.Label(labelframe2, text="This Application is made by : \n -- Akshat Gandhi \n -- Rugved Bongale \n -- Tushar Bapecha \n\n", width=30,font=("bold", 10))
        rootlabel.configure(anchor="center") 
        rootlabel.grid()

    def FeedBack():
        print("Feedback here")
        FeedBack = ThemedTk(theme = ttk_theme, themebg = True)
        labelframe2 = ttk.LabelFrame(FeedBack, text="About us")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)
        FeedBack.title("Feedback")
        FeedBackLabel = ttk.Label(labelframe2, text="We are always open to feedback :)",width=30,font=("bold", 10))
        FeedBackLabel.configure(anchor="center")  
        FeedBackLabel.grid()
        link1 = Label(labelframe2, text="Click here to give feedback",width=30,font=("bold", 10), fg="blue", cursor="hand2")
        link1.configure(anchor="center")
        link1.grid()
        link1.bind("<Button-1>", lambda e: callback("https://docs.google.com/forms/d/e/1FAIpQLSd4UH2BXl-jRCnLFsDGS0OVK6u5liSXEED30cRuv4_bZJBB_Q/viewform?usp=sf_link"))

    def UserM():
        print("User Manual here")
        FeedBack = ThemedTk(theme = ttk_theme, themebg = True)
        FeedBack.title("Help")
        labelframe2 = ttk.LabelFrame(FeedBack, text="About us")  
        labelframe2.grid(row=1,column = 2, rowspan = 6, columnspan=4, sticky='WE', \
                padx=30, pady=30, ipadx=30, ipady=30)
        FeedBackLabel = ttk.Label(labelframe2, text="To get help in using this Application \nrefer the following UserManual",width=30,font=("bold", 10))
        FeedBackLabel.configure(anchor="center")  
        FeedBackLabel.grid()
        link1 = Label(labelframe2, text="Click here",width=30,font=("bold", 10), fg="blue", cursor="hand2")
        link1.configure(anchor="center")
        link1.grid()
        link1.bind("<Button-1>", lambda e: callback("http://www.google.com"))


    othersmenu = Menu(menubar, tearoff = 0, activeborderwidth = 3, bd = 3)
    othersmenu.add_command(label = "Feedback!", command = FeedBack)
    othersmenu.add_command(label = "About us", command = AboutUs)
    othersmenu.add_command(label = "Help", command = UserM)

    menubar.add_cascade(label = "Others", menu = othersmenu)