import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Weak Password", "Length must be at least 4 for security.")
            return

        # Character sets
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = string.punctuation

        # Ensure password has at least one from each category
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]

        # Fill the rest with random characters
        all_chars = lowercase + uppercase + digits + symbols
        password += random.choices(all_chars, k=length - 4)
        random.shuffle(password)

        result.set("".join(password))
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#2c3e50")

# Title label
title_label = tk.Label(root, text="Secure Password Generator", font=("Arial", 16, "bold"), fg="white", bg="#2c3e50")
title_label.pack(pady=10)

# Input field
length_label = tk.Label(root, text="Enter Password Length:", font=("Arial", 12), bg="#2c3e50", fg="white")
length_label.pack()
length_entry = tk.Entry(root, font=("Arial", 12), width=10)
length_entry.pack(pady=5)

# Generate button
generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#3498db", fg="white", command=generate_password)
generate_btn.pack(pady=10)

# Result field
result = tk.StringVar()
result_entry = tk.Entry(root, textvariable=result, font=("Arial", 12), width=30, justify="center")
result_entry.pack(pady=5)

# Run GUI
root.mainloop()
