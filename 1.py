import tkinter as tk

root = tk.Tk()
root.title("4 digit Calculator")

entry = tk.Entry(root)
entry.pack()

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + str(value))

def calculate():
    try:
        result = eval(entry.get()) 
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


buttons = [
    ('1', 1), ('2', 2), ('3', 3), ('+', 4),
    ('4', 5), ('5', 6), ('6', 7), ('-', 8),
    ('7', 9), ('8', 10), ('9', 11), ('*', 12),
    ('0', 13), ('=', 14), ('/', 15), ('C', 16),
]

for (text, index) in buttons:
    action = lambda x=text: button_click(x) if x != '=' else calculate()
    tk.Button(root, text=text, command=action).pack(side=tk.LEFT)

root.mainloop()
