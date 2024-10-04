import tkinter as tk
from tkinter import messagebox
import sqlite3

def setup_backend():
    conn = sqlite3.connect('backend.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            price REAL,
            quantity INTEGER
        )
    ''')
    conn.commit()
    conn.close()

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("مدیریت فروشگاه")
        self.root.geometry("400x450")
        self.root.config(bg="red")

        self.setup_ui()
        self.load_products()

    def setup_ui(self):
        input_frame = tk.Frame(self.root, bg="red")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="نام محصول:", bg="white").grid(row=0, column=0)
        self.name_entry = tk.Entry(input_frame, bg="white")
        self.name_entry.grid(row=0, column=1)

        tk.Label(input_frame, text="قیمت:", bg="white").grid(row=1, column=0)
        self.price_entry = tk.Entry(input_frame, bg="white")
        self.price_entry.grid(row=1, column=1)

        tk.Label(input_frame, text="مقدار:", bg="white").grid(row=2, column=0)
        self.quantity_entry = tk.Entry(input_frame, bg="white")
        self.quantity_entry.grid(row=2, column=1)

        tk.Button(input_frame, text="اضافه کردن", command=self.add_product, bg="white").grid(row=3, column=0)
        tk.Button(input_frame, text="جستجو", command=self.search_product, bg="white").grid(row=3, column=1)
        tk.Button(input_frame, text="ویرایش", command=self.edit_product, bg="white").grid(row=4, column=0)
        tk.Button(input_frame, text="حذف", command=self.delete_product, bg="white").grid(row=4, column=1)

        tk.Button(input_frame, text="بستن", command=self.root.quit, bg="white").grid(row=5, column=0, columnspan=2, pady=10)

        self.product_list = tk.Listbox(self.root, bg="white")
        self.product_list.pack(pady=10, fill=tk.BOTH, expand=True)
        self.product_list.bind('<<ListboxSelect>>', self.on_product_select)

        scrollbar = tk.Scrollbar(self.root, command=self.product_list.yview)
        self.product_list.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def load_products(self):
        self.product_list.delete(0, tk.END)
        conn = sqlite3.connect('backend.db')
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM products")
        for product in cursor.fetchall():
            self.product_list.insert(tk.END, product[0])
        conn.close()

    def on_product_select(self, event):
        try:
            selected_product = self.product_list.get(self.product_list.curselection())
        except tk.TclError:
            return
        conn = sqlite3.connect('backend.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name=?", (selected_product,))
        product = cursor.fetchone()
        conn.close()

        if product:
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, product[1])
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, product[2])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, product[3])

    def add_product(self):
        name = self.name_entry.get()
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("خطا", "لطفاً قیمت و مقدار را به درستی وارد کنید.")
            return

        if not name:
            messagebox.showerror("خطا", "لطفاً نام محصول را وارد کنید.")
            return

        conn = sqlite3.connect('backend.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)", (name, price, quantity))
        conn.commit()
        conn.close()

        self.load_products()
        messagebox.showinfo("موفقیت", "محصول با موفقیت اضافه شد!")

    def search_product(self):
        name = self.name_entry.get()

        conn = sqlite3.connect('backend.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM products WHERE name=?", (name,))
        product = cursor.fetchone()
        conn.close()

        if product:
            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, product[2])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, product[3])
            messagebox.showinfo("پیدا شد", "محصول پیدا شد!")
        else:
            messagebox.showwarning("یافت نشد", "محصول یافت نشد!")

    def edit_product(self):
        try:
            selected_product = self.product_list.get(self.product_list.curselection())
        except tk.TclError:
            messagebox.showwarning("خطا", "لطفاً یک محصول را از لیست انتخاب کنید.")
            return

        name = self.name_entry.get()
        try:
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())
        except ValueError:
            messagebox.showerror("خطا", "لطفاً قیمت و مقدار را به درستی وارد کنید.")
            return

        if not name:
            messagebox.showerror("خطا", "لطفاً نام محصول را وارد کنید.")
            return

        conn = sqlite3.connect('supermarket.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE products SET name=?, price=?, quantity=? WHERE name=?", (name, price, quantity, selected_product))
        conn.commit()
        conn.close()

        self.load_products()
        messagebox.showinfo("موفقیت", "محصول با موفقیت ویرایش شد!")

    def delete_product(self):
        try:
            selected_product = self.product_list.get(self.product_list.curselection())
        except tk.TclError:
            messagebox.showwarning("خطا", "لطفاً یک محصول را از لیست انتخاب کنید.")
            return

        conn = sqlite3.connect('backend.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM products WHERE name=?", (selected_product,))
        conn.commit()
        conn.close()

        self.load_products()
        messagebox.showinfo("موفقیت", "محصول با موفقیت حذف شد!")

setup_backend()
root = tk.Tk()
app = StoreApp(root)
root.mainloop()
