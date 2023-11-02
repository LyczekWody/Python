from cgi import test
import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print("A button was pressed")

def button_func1():
    print("Hello")

# window
window = ttk.Window(themename = 'journal')
window.title('Window and widgets')
window.geometry("800x550")


# ttk widgets
label = ttk.Label(master = window, text = 'Test')
label.pack()

#tk.text
text = tk.Text(master = window)
text.pack()

# ttk entry
entry = ttk.Entry(master = window)
entry.pack()

# exercise label
label2 = ttk.Label(master = window, text = 'My label')
label2.pack()

# ttk button
button = ttk.Button(master = window, text = 'Button', command = button_func)
button.pack()

# hello button
# hello_button = ttk.Button(master = window, text = 'Hello button', command = button_func1)
hello_button = ttk.Button(master = window, text = 'Hello button', command = lambda: print('hello'))

hello_button.pack(pady = 5)

# run
window.mainloop()