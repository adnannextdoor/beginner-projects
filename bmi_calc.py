import tkinter as tk

metric = True
def update_gui():
    clear_container()
    if metric:
        show_metric_units()
    else:
        show_imp_units()

def met_or_imp():
    global metric
    metric = not metric
    update_gui()


def metric_calc():
    try:
        weight_val = int(kg_entry.get())
        height_val = float(metcmet_entry.get())
        bmi_result = weight_val / (height_val ** 2)

        result_screen.delete(1.0, "end")
        result_screen.insert(1.0, str(bmi_result))
    except:
        result_screen.delete(1.0, "end")
        result_screen.insert(1.0, "Error")

def imp_calc():
    try:
        lbs_weight_val = float(lbs_entry.get())
        feet_height_val = float(feet_entry.get())
        inch_height_val = float(inches_entry.get())
        kg_val = lbs_weight_val / 2.204623
        feet_height_val *= 30.48
        inch_height_val *= 2.54
        metric_height_val = (feet_height_val + inch_height_val) / 100

        bmi_result = kg_val / (metric_height_val ** 2)

        result_screen.delete(1.0, "end")
        result_screen.insert(1.0, str(bmi_result))
    except:
        result_screen.delete(1.0, "end")
        result_screen.insert(1.0, "Error")

def clear_container():
    for widget in container.winfo_children():
        widget.destroy()
def show_metric_units():
    instruction1 = tk.Label(container, height=2, font=("Helvetica", 24), text="Enter weight in kg below")
    instruction1.pack()

    bmi_entry = tk.Entry(container, font=("Helvetica", 30), textvariable=kg_entry)
    bmi_entry.pack(pady=2)

    instruction2 = tk.Label(container, height=2, font=("Helvetica", 24), text="Enter height in metres below")
    instruction2.pack()

    bmi_entry = tk.Entry(container, font=("Helvetica", 30),  textvariable=metcmet_entry)
    bmi_entry.pack(pady=2)

    button = tk.Button(container, text="Calculate", command=metric_calc)
    button.pack(pady=10)

def show_imp_units():
    instruction1 = tk.Label(container, height=2, font=("Helvetica", 24), text="Enter weight in lbs below")
    instruction1.pack()

    bmi_entry = tk.Entry(container, font=("Helvetica", 30), textvariable=lbs_entry)
    bmi_entry.pack(pady=2)

    instruction2 = tk.Label(container, height=2, font=("Helvetica", 24), text="Enter height in feet and inches below")
    instruction2.pack()

    instruction3 = tk.Label(container, height=1, font=("Helvetica", 24), text="Feet")
    instruction3.pack()

    bmi_entry = tk.Entry(container, font=("Helvetica", 30), textvariable=feet_entry)
    bmi_entry.pack(pady=2)

    instruction4 = tk.Label(container, height=1, font=("Helvetica", 24), text="Inches")
    instruction4.pack()

    bmi_entry = tk.Entry(container, font=("Helvetica", 30), textvariable=inches_entry)
    bmi_entry.pack(pady=2)

    button = tk.Button(container, text="Calculate", command=imp_calc)
    button.pack(pady=10)


window = tk.Tk()
window.geometry("700x700")
window.title("BMI calculator")

kg_entry = tk.StringVar()
metre_entry = tk.StringVar()
lbs_entry = tk.StringVar()
feet_entry = tk.StringVar()
inches_entry = tk.StringVar()
metcmet_entry = tk.StringVar()


result_label = tk.Label(window, height=2, font=("Helvetica", 24), text="Your BMI is")
result_label.pack(pady=2)

result_screen = tk.Text(window, height=1, width=15, font=("Helvetica", 24))
result_screen.pack(pady=2)

change_dis = tk.Button(window, text="Change", font="Helvetica", command=lambda: met_or_imp())
change_dis.pack()

container = tk.Frame(window)
container.pack()

update_gui()
window.mainloop()


