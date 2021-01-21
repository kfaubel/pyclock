#!/usr/bin/env python3
from tkinter import *
import os
from os import *
from time import *

clock = Tk()                          # Create the main widget
width, height = clock.winfo_screenwidth(), clock.winfo_screenheight()
clock.overrideredirect(1)
clock.geometry("%dx%d+0+0" % (width, height))
textSize = 200

clock.focus_set() 
clock.bind("<space>", lambda root: root.widget.quit())

def updateTime():
    time = strftime("%X")
    text.delete('1.0', END)                          # Clear the old time
    # TODO: Figure out why updated time is not centered
    text.tag_configure("center", justify='center')
    text.tag_add("center", "1.0", "end")
    text.insert(INSERT, strftime("%X"))               # Insert the new time
    clock.after(1000, updateTime)                     # Call again in 1 second

time = strftime("%X")

text = Text(clock)
text.configure(font=("Arial", textSize, "bold"))
text.configure(background='#B0B0B0')
text.configure(foreground='#4D4DFF')
text.tag_configure("center", justify='center')
text.insert(INSERT, strftime("%X"))
text.tag_add("center", "1.0", "end")
text.pack(expand=True, fill='both')

clock.after(1000, updateTime)         # Start the periodic update cycle
clock.mainloop()