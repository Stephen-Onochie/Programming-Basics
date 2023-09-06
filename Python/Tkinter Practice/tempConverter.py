import tkinter as tk
import ttkbootstrap as ttk

# window
window = ttk.Window(themename='darkly')
window.title("Temperature Converter (C to F)")
window.geometry('300x150')

def convert():
    celInput = entry_Int.get()
    fOutput = int(celInput) * (9/5) + 32
    output_string.set(fOutput)

#title
title_label = ttk.Label(master = window, text = 'Celsius to Fahrenheit', font = 'Calibri 24')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_Int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_Int)
button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left')
button.pack(side = 'left', padx = 10)
input_frame.pack(pady = 10)

# output
output_string = tk.StringVar()

output_label = ttk.Label(
    master = window,
    text = 'Output',
    font = 'Calibri 24',
    textvariable = output_string
)

output_label.pack(pady = 5)


# run
window.mainloop()