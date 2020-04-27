from tkinter import *  
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import messagebox
import matplotlib.pyplot as plt


def callbalance(root):
    labelframe1 = LabelFrame(root, text="Balance Comments")  
    labelframe1.grid(row=1,column = 0,columnspan=2, sticky='WE', \
                padx=20, pady=20, ipadx=30, ipady=30)  
    
    rootlabel = Label(labelframe1, text="Your Current Balance is : ")  
    rootlabel.grid(pady = 10)  