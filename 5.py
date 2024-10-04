import tkinter as tk
import random

secret_number = random.randint(1, 50)
attempts = 5

def check_guess():
    global attempts
    guess = guess_entry.get()
    try:
        guess = int(guess)
        if attempts > 1:
            attempts -= 1
            if guess < secret_number:
                result_label.config(text="Too low. Attempts left: " + str(attempts))
            elif guess > secret_number:
                result_label.config(text="Too high. Attempts left: " + str(attempts))
            else:
                result_label.config(text="bravo! You guessed it!")
                attempts = 0
        else:
            result_label.config(text="No more attempts! Please reset")
    except ValueError:
        result_label.config(text="enter valid number")

def reset_game():
    global secret_number, attempts
    secret_number = random.randint(1, 50)
    attempts = 5
    result_label.config(text="Game reset! Guess the new number.")
    guess_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")  
root.configure(bg='lightblue') 

guess_entry = tk.Entry(root, width=40)
guess_entry.pack(pady=10)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

guess_button = tk.Button(button_frame, text="Guess", command=check_guess)
guess_button.pack(side=tk.LEFT, padx=5)

reset_button = tk.Button(button_frame, text="Reset Game", command=reset_game)
reset_button.pack(side=tk.LEFT, padx=5)

result_label = tk.Label(root, text="Guess a number between 1 and 50. You have 5 attempts.", bg='lightblue')
result_label.pack(pady=10)

root.mainloop()
