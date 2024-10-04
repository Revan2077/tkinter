import tkinter as tk

balance = 1000
card_number = "1234567812345678"
password = "1234"
is_logged_in = False
dynamic_pw_enabled = False
fixed_pw_enabled = False

def log_in(event=None):
    """Checks if the card and password are correct and logs in the user."""
    global is_logged_in
    entered_card = card_entry.get()
    entered_password = password_entry.get()
    if entered_card.isdigit() and len(entered_card) == 16 and entered_password.isdigit() and len(entered_password) == 4:
        is_logged_in = True
        login_frame.pack_forget()
        main_frame.pack(pady=10)
        result_label.config(text="")
    else:
        result_label.config(text="Invalid card or password.")

def show_balance():
    """Displays the current balance."""
    result_label.config(text=f"Your balance: ${balance:.2f}")

def add_money():
    """Deposits the specified amount into the balance."""
    global balance
    try:
        amount = float(amount_entry.get())
        if amount > 0:
            balance += amount
            result_label.config(text=f"Deposited: ${amount:.2f}")
        else:
            result_label.config(text="Enter a positive amount.")
    except ValueError:
        result_label.config(text="Invalid amount.")

def take_money():
    """Withdraws the specified amount from the balance."""
    global balance
    try:
        amount = float(amount_entry.get())
        if 0 < amount <= balance:
            balance -= amount
            result_label.config(text=f"Withdrew: ${amount:.2f}")
        else:
            result_label.config(text="Invalid withdrawal amount.")
    except ValueError:
        result_label.config(text="Invalid input.")

def return_to_login():
    """Returns to the login screen."""
    main_frame.pack_forget()
    login_frame.pack(pady=10)
    card_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    result_label.config(text="")

def toggle_dynamic_pw():
    """Enables or disables dynamic password."""
    global dynamic_pw_enabled
    dynamic_pw_enabled = dynamic_pw_var.get()
    if dynamic_pw_enabled:
        dynamic_pw_status_label.config(text="Dynamic Password is enabled.")
    else:
        dynamic_pw_status_label.config(text="Dynamic Password is disabled.")

def toggle_fixed_pw():
    """Enables or disables fixed second password."""
    global fixed_pw_enabled
    fixed_pw_enabled = fixed_pw_var.get()
    if fixed_pw_enabled:
        fixed_pw_status_label.config(text="Fixed Second Password is enabled.")
    else:
        fixed_pw_status_label.config(text="Fixed Second Password is disabled.")

def update_first_password():
    """Changes the first password to a new one."""
    global password
    new_password = new_password_entry.get()
    if new_password.isdigit() and len(new_password) == 4:
        password = new_password
        result_label.config(text="Password changed successfully.")
    else:
        result_label.config(text="Invalid password. Must be 4 digits.")

def show_change_password():
    """Shows the change password frame."""
    change_password_frame.pack(pady=10)
    main_frame.pack_forget()

def hide_change_password():
    """Hides the change password frame and returns to main menu."""
    change_password_frame.pack_forget()
    main_frame.pack(pady=10)

def show_dynamic_pw_settings():
    """Shows the dynamic password settings frame."""
    dynamic_pw_settings_frame.pack(pady=10)
    main_frame.pack_forget()

def show_fixed_pw_settings():
    """Shows the fixed second password settings frame."""
    fixed_pw_settings_frame.pack(pady=10)
    main_frame.pack_forget()

def hide_dynamic_pw_settings():
    """Hides the dynamic password settings frame and returns to main menu."""
    dynamic_pw_settings_frame.pack_forget()
    main_frame.pack(pady=10)

def hide_fixed_pw_settings():
    """Hides the fixed second password settings frame and returns to main menu."""
    fixed_pw_settings_frame.pack_forget()
    main_frame.pack(pady=10)

# Main application setup
root = tk.Tk()
root.title("REZA BANKING EXE :)")
root.geometry("400x500")
root.configure(bg='darkgreen')

header_label = tk.Label(root, text="Reza Banking 💵", font=("Arial", 20), bg='darkgreen', fg='white')
header_label.pack(pady=10)

login_frame = tk.Frame(root, bg='darkgreen')
login_frame.pack(pady=10)

card_label = tk.Label(login_frame, text="Enter 16-digit Card Number:", bg='darkgreen', fg='white')
card_label.pack(pady=5)

card_entry = tk.Entry(login_frame, width=20)
card_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Enter 4-digit Password:", bg='darkgreen', fg='white')
password_label.pack(pady=5)

password_entry = tk.Entry(login_frame, width=10, show='*')
password_entry.pack(pady=5)
password_entry.bind("<Return>", log_in)

enter_button = tk.Button(login_frame, text="Enter", command=log_in)
enter_button.pack(pady=5)

main_frame = tk.Frame(root, bg='darkgreen')

amount_entry = tk.Entry(main_frame, width=10)
amount_entry.pack(pady=10)

check_balance_button = tk.Button(main_frame, text="Check Balance", command=show_balance)
check_balance_button.pack(pady=5)

deposit_button = tk.Button(main_frame, text="Deposit", command=add_money)
deposit_button.pack(pady=5)

withdraw_button = tk.Button(main_frame, text="Withdraw", command=take_money)
withdraw_button.pack(pady=5)

dynamic_pw_button = tk.Button(main_frame, text="Dynamic Password", command=show_dynamic_pw_settings)
dynamic_pw_button.pack(pady=5)

fixed_pw_button = tk.Button(main_frame, text="Fixed Second Password", command=show_fixed_pw_settings)
fixed_pw_button.pack(pady=5)

change_password_button = tk.Button(main_frame, text="Change First Password", command=show_change_password)
change_password_button.pack(pady=5)

exit_button = tk.Button(main_frame, text="Exit", command=return_to_login)
exit_button.pack(pady=5)

result_label = tk.Label(root, text="", bg='darkgreen', fg='white')
result_label.pack(pady=10)

# Dynamic Password Settings Frame
dynamic_pw_settings_frame = tk.Frame(root, bg='darkgreen')

dynamic_pw_var = tk.BooleanVar(value=dynamic_pw_enabled)
dynamic_pw_enabled_radio = tk.Radiobutton(dynamic_pw_settings_frame, text="Enable Dynamic Password", variable=dynamic_pw_var, value=True, command=toggle_dynamic_pw, bg='darkgreen', fg='white')
dynamic_pw_disabled_radio = tk.Radiobutton(dynamic_pw_settings_frame, text="Disable Dynamic Password", variable=dynamic_pw_var, value=False, command=toggle_dynamic_pw, bg='darkgreen', fg='white')

dynamic_pw_enabled_radio.pack(pady=5)
dynamic_pw_disabled_radio.pack(pady=5)

dynamic_pw_status_label = tk.Label(dynamic_pw_settings_frame, text="", bg='darkgreen', fg='white')
dynamic_pw_status_label.pack(pady=5)

back_button_dynamic = tk.Button(dynamic_pw_settings_frame, text="Back", command=hide_dynamic_pw_settings)
back_button_dynamic.pack(pady=5)

# Fixed Second Password Settings Frame
fixed_pw_settings_frame = tk.Frame(root, bg='darkgreen')

fixed_pw_var = tk.BooleanVar(value=fixed_pw_enabled)
fixed_pw_enabled_radio = tk.Radiobutton(fixed_pw_settings_frame, text="Enable Fixed Second Password", variable=fixed_pw_var, value=True, command=toggle_fixed_pw, bg='darkgreen', fg='white')
fixed_pw_disabled_radio = tk.Radiobutton(fixed_pw_settings_frame, text="Disable Fixed Second Password", variable=fixed_pw_var, value=False, command=toggle_fixed_pw, bg='darkgreen', fg='white')

fixed_pw_enabled_radio.pack(pady=5)
fixed_pw_disabled_radio.pack(pady=5)

fixed_pw_status_label = tk.Label(fixed_pw_settings_frame, text="", bg='darkgreen', fg='white')
fixed_pw_status_label.pack(pady=5)

back_button_fixed = tk.Button(fixed_pw_settings_frame, text="Back", command=hide_fixed_pw_settings)
back_button_fixed.pack(pady=5)

# Change Password Frame
change_password_frame = tk.Frame(root, bg='darkgreen')

new_password_label = tk.Label(change_password_frame, text="Enter New 4-digit Password:", bg='darkgreen', fg='white')
new_password_label.pack(pady=5)

new_password_entry = tk.Entry(change_password_frame, width=10)
new_password_entry.pack(pady=5)

change_password_confirm_button = tk.Button(change_password_frame, text="Change Password", command=update_first_password)
change_password_confirm_button.pack(pady=5)

back_button_change = tk.Button(change_password_frame, text="Back", command=hide_change_password)
back_button_change.pack(pady=5)

root.mainloop()
