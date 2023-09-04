#All Tkinter Apps use Widgets, Layouts, & Style
import tkinter as tk
from tkinter import ttk

#window
window = tk.Tk()
window.title("Demo Tkinter App")
window.geometry('300x150')

def convert():
    print(entryInt.get())


#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Calibri 24 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left')
button.pack(side = 'left', padx = 10)
input_frame.pack(pady = 10)

#output
output_string = tk.Str
output_label = ttk.Label(master = window, text = 'Output', font = 'Calibri 24')
output_label.pack(pady=5)

#run
window.mainloop()