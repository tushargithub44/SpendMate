import tkinter as tk
from tkhtmlview import HTMLLabel

root = tk.Tk()
html_label=HTMLLabel(root, html='<a href="http://www.google.com"> Google Hyperlink </a>')
html_label.pack()
root.mainloop()