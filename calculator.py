import tkinter as tk

# setting calculation (screen) to 0 at the beginning of the function

calculation = ""
result = ""
light = True

# functions for calculator

# function 1: codes for addition of button values to screen
def add_to_calc(symbol):
    global calculation
    global result
    result = ""
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# function 2: codes for solving of mathematical equation when '=' button is pressed
def eval_calc():
    global calculation
    global result
    try:
        result = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, result)
        history_func()
    except:
        clear()
        text_result.insert(1.0, "Error")

# function 3: codes for addition of completed calculations to the history screen
def history_func():
    global calculation
    history.insert(1.0, result + '\n')
    history.insert(1.0, calculation + '=')
    calculation = ""


# function 4: codes for clearing of the calculation screen when 'Clear' button is pressed
def clear():
    global calculation
    global result
    calculation = ""
    result = ""
    text_result.delete(1.0, "end")

# function 5: codes for clearing of the history screen when 'CH' button is pressed
def clear_his():
    global result
    result = ""
    history.delete(1.0, "end")

# calculator window settings

calc_win = tk.Tk()
calc_win.geometry('587x380')
calc_win.title('Calculator')

# code for the button dimensions and function

container = tk.Frame()
container.pack()

text_result = tk.Text(container, height=3, width=21, font=('Arial', 24))
text_result.grid(columnspan=15, sticky=tk.W)


history = tk.Text(container, height=17, width=18, font=('Arial', 14))
history.grid(row=0, rowspan=8, column=15, columnspan=14, sticky=tk.W)

button1 = tk.Button(container, width=7, font=('Arial', 16), text="1", command=lambda: add_to_calc(1), bg='Grey')
button1.grid(row=2, column=1)

button2 = tk.Button(container, width=7, font=('Arial', 16), text="2", command=lambda: add_to_calc(2), bg='Grey')
button2.grid(row=2, column=2)

button3 = tk.Button(container, width=7, font=('Arial', 16), text="3", command=lambda: add_to_calc(3), bg='Grey')
button3.grid(row=2, column=3)

button4 = tk.Button(container, width=7, font=('Arial', 16), text="4", command=lambda: add_to_calc(4), bg='Grey')
button4.grid(row=3, column=1)

button5 = tk.Button(container, width=7, font=('Arial', 16), text="5", command=lambda: add_to_calc(5), bg='Grey')
button5.grid(row=3, column=2)

button6 = tk.Button(container, width=7, font=('Arial', 16), text="6", command=lambda: add_to_calc(6), bg='Grey')
button6.grid(row=3, column=3)

button7 = tk.Button(container, width=7, font=('Arial', 16), text="7", command=lambda: add_to_calc(7), bg='Grey')
button7.grid(row=4, column=1)

button8 = tk.Button(container, width=7, font=('Arial', 16), text="8", command=lambda: add_to_calc(8), bg='Grey')
button8.grid(row=4, column=2)

button9 = tk.Button(container, width=7, font=('Arial', 16), text="9", command=lambda: add_to_calc(9), bg='Grey')
button9.grid(row=4, column=3)

button0 = tk.Button(container, width=7, font=('Arial', 16), text="0", command=lambda: add_to_calc(0), bg='Grey')
button0.grid(row=5, column=2)

button_plus = tk.Button(container, width=7, font=('Arial', 16), text="+", command=lambda: add_to_calc('+'), bg='Orange')
button_plus.grid(row=2, column=4)

button_minus = tk.Button(container, width=7, font=('Arial', 16), text="-", command=lambda: add_to_calc('-'), bg='Orange')
button_minus.grid(row=3, column=4)

button_div = tk.Button(container, width=7, font=('Arial', 16), text="/", command=lambda: add_to_calc('/'), bg='Orange')
button_div.grid(row=4, column=4)

button_mul = tk.Button(container, width=7, font=('Arial', 16), text="*", command=lambda: add_to_calc('*'), bg='Orange')
button_mul.grid(row=5, column=4)


button_decpoint = tk.Button(container, width=7, font=('Arial', 16), text=".", command=lambda: add_to_calc('.'))
button_decpoint.grid(row=5, column=1)

button_exponent = tk.Button(container, width=7, font=('Arial', 16), text="x²", command=lambda: add_to_calc('**2'))
button_exponent.grid(row=5, column=3)

button_open_bracket = tk.Button(container, width=7, font=('Arial', 16), text="(", command=lambda: add_to_calc('('))
button_open_bracket.grid(row=6, column=1)

button_close_bracket = tk.Button(container, width=7, font=('Arial', 16), text=")", command=lambda: add_to_calc(')'))
button_close_bracket.grid(row=6, column=2)

button_clear = tk.Button(container, width=7, font=('Arial', 16), text="Clear", command=clear)
button_clear.grid(row=7, column=1)

button_clear_his = tk.Button(container, width=7, font=('Arial', 16), text="CH", command=clear_his)
button_clear_his.grid(row=7, column=2)

button_square_root = tk.Button(container, width=7, font=('Arial', 16), text="√x", command=lambda: add_to_calc('**0.5'))
button_square_root.grid(row=6, column=3)

button_pi = tk.Button(container, width=7, font=('Arial', 16), text="π", command=lambda: add_to_calc('3.14159265'))
button_pi.grid(row=6, column=4)

button_equals = tk.Button(container, width=15, font=('Arial', 16), text="=", command=eval_calc)
button_equals.grid(row=7, column=3, columnspan=2)

# code to cause GUI to be projected

calc_win.mainloop()