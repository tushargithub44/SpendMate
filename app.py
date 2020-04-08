# import tkinter as tk



# class PyText:
#     def __init__(self,master):
#         master.title("Current Month")
#         master.geometry("1100x600")

#         self.master = master
#         font_specs = ("ubuntu",18)    
        
# if __name__ == "__main__":
#     master = tk.Tk()
#     pt = PyText(master)
#     master.mainloop()



# from tkinter import *
# root = Tk() 
# root.geometry("900x600")
# root.title("Current Month")
# font_specs = ("ubuntu",18)
# # mylabel = Label(root,text="I am a label widget")  
# # mybutton = Button(root,text="I am a button")       
# # mylabel.pack()
# # mybutton.pack()
# label_frame = LabelFrame(root, text = 'This is Label Frame') 
# # label_frame.pack(expand = 'yes', fill = 'both') 
# label_frame.grid(column = 0, row = 0,padx = 20, pady = 40)  

# # Buttons 
# btn1 = Button(label_frame, text = 'Button 1') 
# btn1.place(x = 30, y = 10) 
# btn2 = Button(label_frame, text = 'Button 2') 
# btn2.place(x = 130, y = 10) 
  
# # Checkbuttons 
# chkbtn1 = Checkbutton(label_frame, text = 'Checkbutton 1') 
# chkbtn1.place(x = 30, y = 50) 
# chkbtn2 = Checkbutton(label_frame, text = 'Checkbutton 2') 
# chkbtn2.place(x = 30, y = 80) 
  
# root.mainloop()


# import tkinter as Tkinter

# if __name__ == '__main__':
#     form = Tkinter.Tk()

#     getFld = Tkinter.IntVar()

#     form.wm_title('File Parser')

#     stepOne = Tkinter.LabelFrame(form, text=" 1. Enter File Details: ")
#     stepOne.grid(row=0,column = 0, columnspan=5, sticky='W', \
#                  padx=5, pady=5, ipadx=5, ipady=5)

#     helpLf = Tkinter.LabelFrame(form, text=" Quick Help ")
#     helpLf.grid(row=0, column=6, columnspan=2, rowspan=8, \
#                 sticky='NS', padx=5, pady=5)
#     helpLbl = Tkinter.Label(helpLf, text="Help will come - ask for it.")
#     helpLbl.grid(row=0)

#     stepTwo = Tkinter.LabelFrame(form, text=" 2. Enter Table Details: ")
#     stepTwo.grid(row=2, columnspan=7, sticky='W', \
#                  padx=5, pady=5, ipadx=5, ipady=5)

#     stepThree = Tkinter.LabelFrame(form, text=" 3. Configure: ")
#     stepThree.grid(row=3, columnspan=7, sticky='W', \
#                    padx=5, pady=5, ipadx=5, ipady=5)

#     inFileLbl = Tkinter.Label(stepOne, text="Select the File:")
#     inFileLbl.grid(row=0, column=0, sticky='E', padx=5, pady=2)

#     inFileTxt = Tkinter.Entry(stepOne)
#     inFileTxt.grid(row=0, column=1, columnspan=7, sticky="WE", pady=3)

#     inFileBtn = Tkinter.Button(stepOne, text="Browse ...")
#     inFileBtn.grid(row=0, column=8, sticky='W', padx=5, pady=2)

#     outFileLbl = Tkinter.Label(stepOne, text="Save File to:")
#     outFileLbl.grid(row=1, column=0, sticky='E', padx=5, pady=2)

#     outFileTxt = Tkinter.Entry(stepOne)
#     outFileTxt.grid(row=1, column=1, columnspan=7, sticky="WE", pady=2)

#     outFileBtn = Tkinter.Button(stepOne, text="Browse ...")
#     outFileBtn.grid(row=1, column=8, sticky='W', padx=5, pady=2)

#     inEncLbl = Tkinter.Label(stepOne, text="Input File Encoding:")
#     inEncLbl.grid(row=2, column=0, sticky='E', padx=5, pady=2)

#     inEncTxt = Tkinter.Entry(stepOne)
#     inEncTxt.grid(row=2, column=1, sticky='E', pady=2)

#     outEncLbl = Tkinter.Label(stepOne, text="Output File Encoding:")
#     outEncLbl.grid(row=2, column=5, padx=5, pady=2)

#     outEncTxt = Tkinter.Entry(stepOne)
#     outEncTxt.grid(row=2, column=7, pady=2)

#     outTblLbl = Tkinter.Label(stepTwo, \
#           text="Enter the name of the table to be used in the statements:")
#     outTblLbl.grid(row=3, column=0, sticky='W', padx=5, pady=2)

#     outTblTxt = Tkinter.Entry(stepTwo)
#     outTblTxt.grid(row=3, column=1, columnspan=3, pady=2, sticky='WE')

#     fldLbl = Tkinter.Label(stepTwo, \
#                            text="Enter the field (column) names of the table:")
#     fldLbl.grid(row=4, column=0, padx=5, pady=2, sticky='W')

#     getFldChk = Tkinter.Checkbutton(stepTwo, \
#                            text="Get fields automatically from input file",\
#                            onvalue=1, offvalue=0)
#     getFldChk.grid(row=4, column=1, columnspan=3, pady=2, sticky='WE')

#     fldRowTxt = Tkinter.Entry(stepTwo)
#     fldRowTxt.grid(row=5, columnspan=5, padx=5, pady=2, sticky='WE')

#     transChk = Tkinter.Checkbutton(stepThree, \
#                text="Enable Transaction", onvalue=1, offvalue=0)
#     transChk.grid(row=6, sticky='W', padx=5, pady=2)

#     transRwLbl = Tkinter.Label(stepThree, \
#                  text=" => Specify number of rows per transaction:")
#     transRwLbl.grid(row=6, column=2, columnspan=2, \
#                     sticky='W', padx=5, pady=2)

#     transRwTxt = Tkinter.Entry(stepThree)
#     transRwTxt.grid(row=6, column=4, sticky='WE')

#     form.mainloop()


from tkinter import *  
  
top = Tk()  
top.geometry("900x600")  
  

tlabel = Label(top, text="Welcome to SpendMate")  
tlabel.grid(columnspan = 12,pady = 2)  
tlabel.config(font=("ubuntu", 25))

def hello():  
    print("hello!")

menubar = Menu(top)  
menubar.add_command(label="Hello!", command=hello)  
menubar.add_command(label="Quit!", command=top.quit)  

top.config(menu=menubar)  

labelframe1 = LabelFrame(top, text="Balance Comments")  
labelframe1.grid(row=1,column = 0,columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
toplabel = Label(labelframe1, text="Place to put the positive comments")  
toplabel.grid(pady = 10)  

# btn1 = Button(labelframe1, text = 'Button 1') 
# btn1.grid(padx=10, pady=10)


labelframe1 = LabelFrame(top, text="Income Comments")  
labelframe1.grid(row=1,column = 3, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
toplabel = Label(labelframe1, text="Place to put the positive comments")  
toplabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()


labelframe1 = LabelFrame(top, text="Expense Comments")  
labelframe1.grid(row=1,column = 6, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
toplabel = Label(labelframe1, text="Place to put the positive comments")  
toplabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()


labelframe1 = LabelFrame(top, text="Positive Comments")  
labelframe1.grid(row=3,column = 0, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
toplabel = Label(labelframe1, text="Place to put the positive comments")  
toplabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()



labelframe1 = LabelFrame(top, text="Positive Comments")  
labelframe1.grid(row=3,column = 3, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
toplabel = Label(labelframe1, text="Place to put the positive comments")  
toplabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()



labelframe1 = LabelFrame(top, text="Positive Comments")  
labelframe1.grid(row=3,column = 6, columnspan=2, sticky='WE', \
             padx=20, pady=20, ipadx=30, ipady=30)  
  
toplabel = Label(labelframe1, text="Place to put the positive comments")  
toplabel.grid()  

btn1 = Button(labelframe1, text = 'Button 1') 
btn1.grid()




# btn3 = Button(top, text = 'Button 1') 
# btn3.grid(row = 0, column = 3)


 
# labelframe2 = LabelFrame(top, text = "Negative Comments")  
# labelframe2.pack(fill="both", expand = "yes")  
  
# bottomlabel = Label(labelframe2,text = "Place to put the negative comments")  
# bottomlabel.pack()  
  

# top.rowconfigure(1, weight=1)
# top.columnconfigure(2, weight=1)

top.mainloop()