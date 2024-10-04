import tkinter as tk

def convert_money():
    try:
        if conversion_type.get() == "Tomans to Dollars":
            tomans = float(money_entry.get())
            dollars = tomans / 60000
            result_label.config(text=f"{tomans} Tomans = {dollars:.2f} Dollars")
        else:
            dollars = float(money_entry.get())
            tomans = dollars * 60000
            result_label.config(text=f"{dollars} Dollars = {tomans:.2f} Tomans")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

def reset_conversion():
    money_entry.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Money Converter")
root.geometry("300x200")
root.configure(bg='lightblue')

conversion_type = tk.StringVar(value="Tomans to Dollars")

conversion_frame = tk.Frame(root, bg='lightblue')
conversion_frame.pack(pady=10)

tomans_to_dollars_button = tk.Radiobutton(conversion_frame, text="Tomans to Dollars", variable=conversion_type, value="Tomans to Dollars", bg='lightblue')
tomans_to_dollars_button.pack(side=tk.LEFT)

dollars_to_tomans_button = tk.Radiobutton(conversion_frame, text="Dollars to Tomans", variable=conversion_type, value="Dollars to Tomans", bg='lightblue')
dollars_to_tomans_button.pack(side=tk.LEFT)

money_entry = tk.Entry(root, width=10)
money_entry.pack(pady=10)

convert_button = tk.Button(root, text="Convert", command=convert_money)
convert_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset", command=reset_conversion)
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", bg='lightblue')
result_label.pack(pady=10)

root.mainloop()
