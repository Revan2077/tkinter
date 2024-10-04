import tkinter as tk
import time
from tkinter import messagebox

class SimpleAlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm App")
        self.root.geometry("400x300")

        self.time_label = tk.Label(self.root, text="Set Alarm Time (HH:MM):", font=("Arial", 14))
        self.time_label.pack(pady=10)

        self.time_entry = tk.Entry(self.root, font=("Arial", 14))
        self.time_entry.pack(pady=5)

        self.set_button = tk.Button(self.root, text="Set Alarm", font=("Arial", 14), command=self.set_alarm)
        self.set_button.pack(pady=20)

        self.message = tk.Label(self.root, text="", font=("Arial", 14), fg="green")
        self.message.pack(pady=10)

        self.alarm_time = None

    def set_alarm(self):
        alarm_time = self.time_entry.get()
        self.alarm_time = alarm_time
        self.message.config(text=f"Alarm set for {alarm_time}")
        self.check_alarm()

    def check_alarm(self):
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == self.alarm_time:
                messagebox.showinfo("Alarm", "Time to wake up!")
                break
            time.sleep(1)

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleAlarmApp(root)
    root.mainloop()
