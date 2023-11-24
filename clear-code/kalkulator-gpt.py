import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

# Configure grid row and column weights
for i in range(6):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i, weight=1)

# Entry widget to display the calculation
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(row=0, column=0, columnspan=4, pady=10, sticky="nsew")

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '(', ')', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    button_widget = tk.Canvas(root, width=50, height=50, highlightthickness=0)
    button_widget.create_oval(5, 5, 45, 45, outline='black', width=2)
    button_widget.create_text(25, 25, text=button, font=("Arial", 14), tags="text")
    button_widget.grid(row=row_val, column=col_val, padx=5, pady=5)
    button_widget.bind("<Button-1>", lambda event, b=button: add_to_calculation(b))

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear and Equals buttons
clear_button = tk.Canvas(root, width=110, height=50, highlightthickness=0)
clear_button.create_oval(5, 5, 45, 45, outline='black', width=2)
clear_button.create_text(55, 25, text="Clear", font=("Arial", 14), tags="text")
clear_button.grid(row=5, column=0, columnspan=2, pady=5)
clear_button.bind("<Button-1>", lambda event: clear_field())

equals_button = tk.Canvas(root, width=110, height=50, highlightthickness=0)
equals_button.create_oval(5, 5, 45, 45, outline='black', width=2)
equals_button.create_text(55, 25, text="=", font=("Arial", 14), tags="text")
equals_button.grid(row=5, column=2, columnspan=2, pady=5)
equals_button.bind("<Button-1>", lambda event: evaluate_calculation())

# Adjust weight for the last row to make the Clear and Equals buttons expandable
root.grid_rowconfigure(5, weight=1)

# Run the application
root.mainloop()
