import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Buttons and Variables')
window.geometry("600x400")

# label

label = ttk.Label(master = window, text = 'Buttons and Variables', font = 'Calibre 16')
label.pack(pady = 5)

# button
def button_function():
    print(radio_var.get())

button_string = tk.StringVar(value='defaulf')
button = ttk.Button(master = window, text = 'Button', command = button_function, textvariable = button_string)
button.pack()

# check button
check_var = tk.IntVar(value = 10) #ustawiajac value = 10 guzik na starcie jest klikniety, poniewaz onvalue tez wynosi 10
check = ttk.Checkbutton(
        window,
        text = 'checkbox 1',
        command = lambda: print(check_var.get()),
        variable= check_var,
        onvalue = 10,
        offvalue = 5)
check.pack()

# radio button
radio_var = tk.StringVar()
radio1 = ttk.Radiobutton(
    window, text = 'Radiobutton 1',
    value = 'radio 1',
    variable = radio_var,
    command = lambda: print(radio_var.get()))
radio1.pack()

radio2 = ttk.Radiobutton(
    window,
    text = 'Radiobutton 2',
    value = 2,
    variable = radio_var)
radio2.pack()



window.mainloop()