import tkinter as tk
from tkinter import ttk
import random


def play_game():
    user_choice = combo.get()
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])

    if user_choice == computer_choice:
        result = "mosavi!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "bordi!"
    else:
        result = "computer bord!"
    result_label.config(text=f"You: {user_choice} | Computer: {computer_choice}\n{result}")


root = tk.Tk()
root.title("Rock Paper Scissors")


combo = ttk.Combobox(root, values=['Rock', 'Paper', 'Scissors'], state="readonly")
combo.current(0)
combo.pack(pady=10)


tk.Button(root, text="Play", command=play_game).pack(pady=10)


result_label = tk.Label(root)
result_label.pack(pady=10)

root.mainloop()
