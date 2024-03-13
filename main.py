import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=200)


# Calculate Button
def button_calculate(miles=1.0):
    print(round(miles * 0.621371))


button = tk.Button(text="Calculate", command=button_calculate)
button.grid(row=3, column=2)

window.mainloop()
