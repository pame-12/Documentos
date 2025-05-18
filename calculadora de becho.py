import tkinter as tk

# Función para actualizar el campo de entrada
def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

# Función para evaluar la expresión
def evaluate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except:
        input_text.set("Error")
        expression = ""

# Función para limpiar el campo de entrada
def clear():
    global expression
    expression = ""
    input_text.set("")

# Configuración de la ventana principal
root = tk.Tk() #crea la ventana principal
root.title("Calculadora")#crea el titulo de la calculadora

expression = ""
input_text = tk.StringVar()

# Campo de entrada
input_frame = tk.Frame(root)
input_frame.pack()

input_field = tk.Entry(input_frame, textvariable=input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

# Frame para los botones
btns_frame = tk.Frame(root)
btns_frame.pack()

# Primera fila
tk.Button(btns_frame, text='7', command=lambda: click_button(7), height=3, width=9).grid(row=1, column=0)
tk.Button(btns_frame, text='8', command=lambda: click_button(8), height=3, width=9).grid(row=1, column=1)
tk.Button(btns_frame, text='9', command=lambda: click_button(9), height=3, width=9).grid(row=1, column=2)
tk.Button(btns_frame, text='/', command=lambda: click_button('/'), height=3, width=9).grid(row=1, column=3)

# Segunda fila
tk.Button(btns_frame, text='4', command=lambda: click_button(4), height=3, width=9).grid(row=2, column=0)
tk.Button(btns_frame, text='5', command=lambda: click_button(5), height=3, width=9).grid(row=2, column=1)
tk.Button(btns_frame, text='6', command=lambda: click_button(6), height=3, width=9).grid(row=2, column=2)
tk.Button(btns_frame, text='*', command=lambda: click_button('*'), height=3, width=9).grid(row=2, column=3)

# Tercera fila
tk.Button(btns_frame, text='1', command=lambda: click_button(1), height=3, width=9).grid(row=3, column=0)
tk.Button(btns_frame, text='2', command=lambda: click_button(2), height=3, width=9).grid(row=3, column=1)
tk.Button(btns_frame, text='3', command=lambda: click_button(3), height=3, width=9).grid(row=3, column=2)
tk.Button(btns_frame, text='-', command=lambda: click_button('-'), height=3, width=9).grid(row=3, column=3)

# Cuarta fila
tk.Button(btns_frame, text='C', command=clear, height=3, width=9).grid(row=4, column=0)
tk.Button(btns_frame, text='0', command=lambda: click_button(0), height=3, width=9).grid(row=4, column=1)
tk.Button(btns_frame, text='=', command=evaluate, height=3, width=9).grid(row=4, column=2)
tk.Button(btns_frame, text='+', command=lambda: click_button('+'), height=3, width=9).grid(row=4, column=3)

root.mainloop()

