import tkinter as tk

def calculate_bmi():
    weight = float(weight_entry.get())
    height = float(height_entry.get()) / 100

    bmi = weight / (height ** 2)

    result_label.config(text="Your BMI is {:.2f}".format(bmi))

    if bmi < 18.5:
        status_label.config(text="You are underweight")
    elif 18.5 <= bmi < 25:
        status_label.config(text="You have a normal weight")
    else:
        status_label.config(text="You are overweight")

# Creating tkinter window
window = tk.Tk()
window.title("BMI Calculator")

# Weight input
weight_label = tk.Label(window, text="Enter your weight in kg:")
weight_label.grid(row=0, column=0)
weight_entry = tk.Entry(window)
weight_entry.grid(row=0, column=1)

# Height input
height_label = tk.Label(window, text="Enter your height in cm:")
height_label.grid(row=1, column=0)
height_entry = tk.Entry(window)
height_entry.grid(row=1, column=1)

# Button to calculate BMI
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

# Result display
result_label = tk.Label(window, text="")
result_label.grid(row=3, columnspan=2)

# BMI status display
status_label = tk.Label(window, text="")
status_label.grid(row=4, columnspan=2)

window.mainloop()
