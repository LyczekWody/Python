import tkinter as tk
from tkinter import ttk


def button_func():
    # get the content of the entry
    entry_text = entry.get()
    #  update the Label
    # label.configure(text = entry_text)
    label['text'] = entry_text
    entry ['state'] = 'disabled'

def button_func1():
    label ['text'] = "Some text"
    entry ['state'] = 'enable'

#window
window = tk.Tk()
window.title('Getting and setttig widgets')
window.geometry('500x350')

# widget
label = ttk.Label(master=window, text = "Getting and setttig widgets")
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'A Button', command = button_func)
button.pack()

# exercise
button1 = ttk.Button(master = window, text = 'Exercise button', command = button_func1)
button1.pack()


window.mainloop()