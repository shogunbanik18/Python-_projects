
from tkinter import *
from tkinter .ttk import *

# importig time 
from time import strftime

# creating a ui for the time table box 
root =Tk()
root.title("Clock")
label = Label(root,font=("DS-Digital",80),background ="black",foreground = "cyan" )
label.pack(anchor='center')

# defining a function for time 
def time():
    # clock in 24 hour format 
    string = strftime('%H:%M:%S %p')
    # clock in 12 hour format 
    string = strftime('%I:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)

time()

mainloop()

