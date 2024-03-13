import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)


# Calculate Button
def button_calculate():
    miles = float(input_miles.get())
    kilometers = miles * 1.609344
    print(f"Miles: {miles}\nKilometers: {kilometers}")
    label_conversion.config(text=round(kilometers))


# Button-Calculate
button = tk.Button(text="Calculate", command=button_calculate)
button.grid(row=3, column=2)

# Text - is equal to
label_convert = tk.Label(text="is equal to")
label_convert.grid(row=2, column=1)
# Text - Miles
label_miles = tk.Label(text="Miles")
label_miles.grid(row=1, column=3)
# Text - Answer
label_conversion = tk.Label()
label_conversion.grid(row=2, column=2)
# Text - Km
label_kilometers = tk.Label(text="Km")
label_kilometers.grid(row=2, column=3)

# Entry-Box
input_miles = tk.Entry(width=10)
input_miles.grid(row=1, column=2)

window.mainloop()
