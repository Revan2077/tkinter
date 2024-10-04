import tkinter as tk

def convert_temperature():
    try:
        if conversion_type.get() == "Celsius to Fahrenheit":
            celsius = float(temperature_entry.get())
            fahrenheit = (celsius * 9/5) + 32
            result_label.config(text=f"{celsius}°C = {fahrenheit:.2f}°F")
        else:
            fahrenheit = float(temperature_entry.get())
            celsius = (fahrenheit - 32) * 5/9
            result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def reset_conversion():
    temperature_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Temperature Converter")
root.geometry("300x200")
root.configure(bg='lightblue')

conversion_type = tk.StringVar(value="Celsius to Fahrenheit")

conversion_frame = tk.Frame(root, bg='lightblue')
conversion_frame.pack(pady=10)

c_to_f_button = tk.Radiobutton(conversion_frame, text="Celsius to Fahrenheit", variable=conversion_type, value="Celsius to Fahrenheit", bg='lightblue')
c_to_f_button.pack(side=tk.LEFT)

f_to_c_button = tk.Radiobutton(conversion_frame, text="Fahrenheit to Celsius", variable=conversion_type, value="Fahrenheit to Celsius", bg='lightblue')
f_to_c_button.pack(side=tk.LEFT)

temperature_entry = tk.Entry(root, width=10)
temperature_entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_conversion)
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", bg='lightblue')
result_label.pack(pady=10)

root.mainloop()
