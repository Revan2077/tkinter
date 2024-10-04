import tkinter as tk

def add_task():
    task = task_entry.get()  
    if task:  
        tasks_listbox.insert(tk.END, task)  
        task_entry.delete(0, tk.END)  


def delete_task():
    selected_task_index = tasks_listbox.curselection()  
    if selected_task_index:  
        tasks_listbox.delete(selected_task_index)  


root = tk.Tk()
root.title("To-Do List")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)


tasks_listbox = tk.Listbox(root, width=50, height=10)
tasks_listbox.pack(pady=10)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)


root.mainloop()
