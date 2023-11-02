import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_input = entry.get()
    try:
        mile_input = float(mile_input)
        km_output = float(km_output)
        km_output = mile_input * 1.61
        output_string.set(km_output)
        output_label.config(foreground='black')
    except ValueError:
        output_string.set("Musisz podać liczbe!")
        output_label.config(foreground='red')

# window
window = ttk.Window(themename = 'flatly')
window.title('Miles to kilometers')
window.geometry("300x150")


# title
title_label = ttk.Label(master = window, text = "Miles to kilometers", font = 'Calibri 24')
title_label.pack()

# input
input_frame = ttk.Frame(master=window)
entry = ttk.Entry(master=input_frame)
button = ttk.Button(master=input_frame, text='Convert', command=convert)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master = window, 
    text = 'Output', 
    font = 'Calibri 22 ',
    textvariable = output_string)

output_label.pack(pady = 5)


# run
window.mainloop()