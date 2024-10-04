import tkinter as tk
import random

words = ["python", "hangman", "programming", "tkinter", "challenge"]
chosen_word = random.choice(words)
guessed_letters = []
attempts = 10

def update_display():
    display_word = ''.join([letter if letter in guessed_letters else '_' for letter in chosen_word])
    word_label.config(text=' '.join(display_word))
    attempts_label.config(text=f"Attempts left: {attempts}")

def guess_letter():
    global attempts
    letter = guess_entry.get().lower()
    guess_entry.delete(0, tk.END)
    
    if len(letter) == 1 and letter.isalpha() and letter not in guessed_letters:
        guessed_letters.append(letter)
        if letter not in chosen_word:
            attempts -= 1
            
        update_display()
        
        if attempts == 0:
            result_label.config(text=f"You lost! The word was: {chosen_word}")
        elif all(letter in guessed_letters for letter in chosen_word):
            result_label.config(text="Congratulations! You guessed the word!")
    else:
        result_label.config(text="Please enter a valid letter.")

def reset_game():
    global chosen_word, guessed_letters, attempts
    chosen_word = random.choice(words)
    guessed_letters = []
    attempts = 10
    update_display()
    result_label.config(text="")

root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x300")
root.configure(bg='lightblue')

word_label = tk.Label(root, text='', font=('Helvetica', 24), bg='lightblue')
word_label.pack(pady=20)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", bg='lightblue')
attempts_label.pack(pady=10)

guess_entry = tk.Entry(root, width=10)
guess_entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.pack(pady=5)

result_label = tk.Label(root, text="", bg='lightblue')
result_label.pack(pady=10)

reset_game()
root.mainloop()
