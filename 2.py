import tkinter as tk
import random

def play_game():
    user_choice = user_var.get()
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


user_var = tk.StringVar(value="Rock")


tk.Radiobutton(root, text="Rock", variable=user_var, value="Rock").pack(anchor=tk.W)
tk.Radiobutton(root, text="Paper", variable=user_var, value="Paper").pack(anchor=tk.W)
tk.Radiobutton(root, text="Scissors", variable=user_var, value="Scissors").pack(anchor=tk.W)
tk.Button(root, text="Play", command=play_game).pack(pady=10)

result_label = tk.Label(root)
result_label.pack(pady=10)


root.mainloop()
