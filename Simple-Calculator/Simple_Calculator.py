import tkinter as tk
import math

# Function to evaluate the expression
def evaluate_expression():
    try:
        expression = entry.get().replace('^', '**')
        result = eval(expression)
        
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to update the input field
def button_click(value):
    entry.insert(tk.END, value)

# Function to calculate square root
def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)

        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate sine
def sin():
    try:
        value = float(entry.get())
        result = math.sin(math.radians(value))

        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate cosine
def cos():
    try:
        value = float(entry.get())
        result = math.cos(math.radians(value))
        
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to calculate tangent
def tan():
    try:
        value = float(entry.get())
        result = math.tan(math.radians(value))
        
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Function to handle power calculations
def power():
    current_input = entry.get().strip()
    if current_input:
        entry.insert(tk.END, "^")

# Function to insert pi (π)
def insert_pi():
    entry.insert(tk.END, str(math.pi))

# Function to clear the input field
def clear_entry():
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font=("Arial", 20), bd=5, insertwidth=4, width=14, borderwidth=4)
entry.grid(row=0, column=0, columnspan=4)

# Button definitions
buttons = [
    'AC', '√',  '/','*',
    '7', '8', '9', '-',
    '4', '5', '6', '+',
    '1', '2', '3', '^',
    '0', '.','π','=',
    'cos','tan','sin'
    
]

row_val = 1
col_val = 0

for button in buttons:
    if button == "=":
        cmd = evaluate_expression
    elif button == "AC":
        cmd = clear_entry
    elif button == "√":
        cmd = sqrt
    elif button == "sin":
        cmd = sin
    elif button == "cos":
        cmd = cos
    elif button == "tan":
        cmd = tan
    elif button == "^":
        cmd = power
    elif button == "π":
        cmd = insert_pi
    else:
        cmd = lambda x=button: button_click(x)

    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 18), command=cmd).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
