import tkinter as tk

def click_button(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + button)

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Crear la ventana
root = tk.Tk()
root.title("Calculadora")

# Crear un banner que diga "Calculadora de ejemplo"
banner = tk.Label(root, text="Calculadora de ejemplo", font=("Arial", 16))
banner.grid(row=0, column=0, columnspan=4, pady=10)

# Crear la entrada
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Definir los botones
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', 'C', '+',
    '='
]

# Añadir los botones a la interfaz
row = 2
col = 0
for button in buttons:
    if button == "=":
        tk.Button(root, text=button, padx=30, pady=15, font=("Arial", 14), command=calculate).grid(row=row, column=col, padx=5, pady=5)
    elif button == "C":
        tk.Button(root, text=button, padx=27, pady=15, font=("Arial", 14), command=clear_entry).grid(row=row, column=col, padx=5, pady=5)
    else:
        tk.Button(root, text=button, padx=35, pady=15, font=("Arial", 14), command=lambda b=button: click_button(b)).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()
