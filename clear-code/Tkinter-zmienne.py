import tkinter as tk
from tkinter import ttk

def button_func():
     print(string_var.get())
     string_var.set('button pressed')

def button_func1():
    string_var1.set('')

#window
window = tk.Tk()
window.title('Tkinter Variables')
window.geometry('500x350')

# tkinter variables
string_var = tk.StringVar()
string_var1 = tk.StringVar(value = 'test')



# widget
label = ttk.Label(master = window, text = 'Label',font = 'Ariel 18', textvariable = string_var)
label.pack(pady = 5)

entry = ttk.Entry(master = window, textvariable = string_var) 
entry.pack(pady = 5)

button = ttk.Button(master = window, text = 'Button', command = button_func )
button.pack(pady = 5)

# exercise
entry1 = ttk.Entry(master = window, textvariable = string_var1) 
entry1.pack(pady = 5)

entry2 = ttk.Entry(master = window, textvariable = string_var1) 
entry2.pack(pady = 5)

label1 = ttk.Label(master = window, text = 'Label',font = 'Ariel 18', textvariable = string_var1)
label1.pack(pady = 5)

button1 = ttk.Button(master = window, text = ' Clear Button', command = button_func1 )
button1.pack(pady = 5)

# run
window.mainloop()