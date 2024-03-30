import tkinter as tk
from tkinter import ttk

def button_function():
    print('A button was pressed')

def buttonPractice():
    print('hello')

# create a window
window = tk.Tk()
window.title("Widgets Test App")
window.geometry('800x500') # 'WIDTHxHEIGHT'

# ttk label
label = ttk.Label(master = window, text = 'This is a test label')
label.pack()

#tk.text
textbox = tk.Text(master = window) #text input
textbox.pack() # puts widget on screen

# ttk entry
entry = ttk.Entry(master = window) # single line of text
entry.pack() 

# practice label
label2 = ttk.Label(master = window, text = 'my label')
label2.pack()

# ttk button
button = ttk.Button(master = window, text = 'A button', command = button_function) # command runs a function
button.pack()

# practice button
button2 = ttk.Button(master = window, text = 'Press me', command = buttonPractice)
button2.pack()

#another practice button
button3 = ttk.Button(master = window, text = "Another one", command = lambda: print('Practice!'))
button3.pack()


# run
window.mainloop()
print('The program has finished') # runs after the app is closed