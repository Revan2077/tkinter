import tkinter as tk
from tkinter import filedialog

class MyNotepadApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Notepad")
        self.window.geometry("800x600")

        self.text_box = tk.Text(self.window, wrap="word", undo=True)
        self.text_box.pack(expand=1, fill="both")

        self.menu_bar = tk.Menu(self.window)
        self.window.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_existing_file)
        self.file_menu.add_command(label="Save", command=self.save_current_file)

        self.current_file = None

    def open_existing_file(self):
        file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.current_file = file
            with open(file, "r") as f:
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, f.read())

    def save_current_file(self):
        if self.current_file:
            with open(self.current_file, "w") as f:
                f.write(self.text_box.get(1.0, tk.END))
        else:
            self.save_as_new_file()

    def save_as_new_file(self):
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file:
            self.current_file = file
            with open(file, "w") as f:
                f.write(self.text_box.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = MyNotepadApp(root)
    root.mainloop()
