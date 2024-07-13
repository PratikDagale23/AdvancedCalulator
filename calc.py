import tkinter as tk
from tkinter import messagebox
import math

def click(event):
    global expression
    expression += event.widget.cget("text")
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set(expression)

def evaluate():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

def switch_to_advanced():
    for button in advanced_buttons:
        button.grid()

def advanced_click(event):
    global expression
    text = event.widget.cget("text")
    if text == 'sin':
        expression += "math.sin("
    elif text == 'cos':
        expression += "math.cos("
    elif text == 'tan':
        expression += "math.tan("
    elif text == 'log':
        expression += "math.log("
    equation.set(expression)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x700")

expression = ""
equation = tk.StringVar()

# Display
display = tk.Entry(root, textvariable=equation, font=("Arial", 30), bd=10, insertwidth=4, width=18, borderwidth=4)
display.grid(row=0, column=0, columnspan=4)

# Buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row = 1
col = 0
for button in buttons:
    b = tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), relief="solid", borderwidth=1)
    b.grid(row=row, column=col, sticky="nsew")
    b.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

# Clear button
clear_button = tk.Button(root, text='C', padx=20, pady=20, font=("Arial", 18), relief="solid", borderwidth=1, command=clear)
clear_button.grid(row=row, column=col, columnspan=2, sticky="nsew")

# Equal button
equal_button = tk.Button(root, text='=', padx=20, pady=20, font=("Arial", 18), relief="solid", borderwidth=1, command=evaluate)
equal_button.grid(row=row+1, column=0, columnspan=4, sticky="nsew")

# Advanced calculator button
advanced_button = tk.Button(root, text='Advanced', padx=20, pady=20, font=("Arial", 18), relief="solid", borderwidth=1, command=switch_to_advanced)
advanced_button.grid(row=row, column=2, columnspan=2, sticky="nsew")

# Advanced buttons
advanced_buttons = []
advanced_operations = ['sin', 'cos', 'tan', 'log']
for i, operation in enumerate(advanced_operations):
    b = tk.Button(root, text=operation, padx=20, pady=20, font=("Arial", 18), relief="solid", borderwidth=1)
    b.grid(row=row+2, column=i, sticky="nsew")
    b.bind("<Button-1>", advanced_click)
    advanced_buttons.append(b)
    b.grid_remove()  # Initially hide advanced buttons

# Configure grid
for i in range(7):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
