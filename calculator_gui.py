import tkinter as tk
from tkinter import messagebox

from functions import (
    substraction, division, modulus,
    find_factorial, fibonacci_sequence, fibonacci_at_nth,
    sin_angle, cos_angle, tan_angle, compute_log,
    rad_to_deg, deg_to_rad
)

root = tk.Tk()
root.title("Simple Scientific Calculator")
root.geometry("380x520")
root.resizable(False, False)

# Display
display = tk.Entry(root, font=("Arial", 24), bd=5, relief="sunken", justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")


# Expression Insert
def add_input(value):
    display.insert(tk.END, value)


# Evaluate Basic Expression
def evaluate():
    try:
        expr = display.get().replace("×", "*").replace("÷", "/")
        result = eval(expr)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except:
        messagebox.showerror("Error", "Invalid Expression")


# Clear
def clear():
    display.delete(0, tk.END)


# Delete last char
def delete():
    text = display.get()
    display.delete(0, tk.END)
    display.insert(0, text[:-1])


# Scientific popups
def sci(func, title):
    win = tk.Toplevel(root)
    win.title(title)
    win.geometry("250x120")

    tk.Label(win, text=title).pack(pady=5)
    entry = tk.Entry(win, font=("Arial", 14))
    entry.pack(pady=5)

    def calc():
        try:
            val = float(entry.get())
            result = func(val)
            display.delete(0, tk.END)
            display.insert(0, str(result))
            win.destroy()
        except:
            messagebox.showerror("Error", "Invalid Input")

    tk.Button(win, text="Calculate", command=calc).pack(pady=5)


# Buttons Layout
buttons = [
    ("7", lambda: add_input("7")), ("8", lambda: add_input("8")), ("9", lambda: add_input("9")), ("÷", lambda: add_input("÷")),
    ("4", lambda: add_input("4")), ("5", lambda: add_input("5")), ("6", lambda: add_input("6")), ("×", lambda: add_input("×")),
    ("1", lambda: add_input("1")), ("2", lambda: add_input("2")), ("3", lambda: add_input("3")), ("-", lambda: add_input("-")),
    ("0", lambda: add_input("0")), (".", lambda: add_input(".")), ("(", lambda: add_input("(")), (")", lambda: add_input(")")),
]

row = 1
col = 0
for (text, cmd) in buttons:
    tk.Button(root, text=text, width=6, height=2, command=cmd).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col == 4:
        col = 0
        row += 1

# Special row
tk.Button(root, text="C", width=6, height=2, command=clear).grid(row=row, column=0)
tk.Button(root, text="DEL", width=6, height=2, command=delete).grid(row=row, column=1)
tk.Button(root, text="Ans", width=6, height=2, command=lambda: add_input(display.get())).grid(row=row, column=2)
tk.Button(root, text="=", width=6, height=2, command=evaluate).grid(row=row, column=3)

row += 1

# Scientific row 1
tk.Button(root, text="sin", width=6, height=2, command=lambda: sci(sin_angle, "sin")).grid(row=row, column=0)
tk.Button(root, text="cos", width=6, height=2, command=lambda: sci(cos_angle, "cos")).grid(row=row, column=1)
tk.Button(root, text="tan", width=6, height=2, command=lambda: sci(tan_angle, "tan")).grid(row=row, column=2)
tk.Button(root, text="log", width=6, height=2, command=lambda: sci(compute_log, "log")).grid(row=row, column=3)

row += 1

# Scientific row 2
tk.Button(root, text="x!", width=6, height=2, command=lambda: sci(lambda x: find_factorial(int(x)), "factorial")).grid(row=row, column=0)
tk.Button(root, text="Fib", width=6, height=2, command=lambda: sci(lambda x: fibonacci_at_nth(int(x)), "Fibonacci")).grid(row=row, column=1)
tk.Button(root, text="Rad→Deg", width=6, height=2, command=lambda: sci(rad_to_deg, "Rad → Deg")).grid(row=row, column=2)
tk.Button(root, text="Deg→Rad", width=6, height=2, command=lambda: sci(deg_to_rad, "Deg → Rad")).grid(row=row, column=3)

root.mainloop()
