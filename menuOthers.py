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


    othersmenu = Menu(menubar, tearoff = 0)
    othersmenu.add_command(label = "Feedback!", command = FeedBack)
    othersmenu.add_command(label = "About us", command = AboutUs)

    menubar.add_cascade(label = "Others", menu = othersmenu)