import tkinter as tk

window = tk.Tk()

window.title("Calculator")

window.geometry("400x200")

entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

lbl = tk.Label(window, text="RESULT  : ")
lbl.pack()

def addition():
    number_1 =int(entry1.get())
    number_2 = int(entry2.get())
    result = number_1 + number_2

    lbl.config(text=str(result))

boutton_addition = tk.Button(window, text="Add", command=addition)
boutton_addition.pack()

def substract():
    number_1 = int(entry1.get())
    number_2 = int(entry2.get())
    result = number_1 - number_2
    lbl.config(text=str(result))

button_substract = tk.Button(window, text="Substraction", command=substract)
button_substract.pack()

def multiply():
    number_1 = int(entry1.get())
    number_2 = int(entry2.get())
    result = number_1 * number_2
    lbl.config(text=str(result))

boutton_multiplication = tk.Button(window, text="Multiply", command=multiply)
boutton_multiplication.pack()

def divide():
    number_1 = int(entry1.get())
    number_2 = int(entry2.get())
    result = number_1 / number_2
    lbl.config(text=str(result))

button_divide = tk.Button(window, text="Divide", command=divide)
button_divide.pack()

def clear():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    lbl.config(text="")

button_clear = tk.Button(window, text="Clear", command=clear)
button_clear.pack()

window.mainloop()   