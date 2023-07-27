import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_pwd(length, complexity):
    characters = string.ascii_letters + string.digits
    if complexity == "high":
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_pwd1():
    name = name_entry.get().strip()
    length = int(length_entry.get())
    complexity = complexity_var.get()

    if name == "":
        messagebox.showerror("Error", "Please enter your name ")
        return

    password = generate_pwd(length, complexity)
    result_label.config(text=f"Your password is: {password}")
    

window = tk.Tk()
window.title("Password Generator")
window.config(bg="#FAF3F0")

heading_label = tk.Label(window, text="Password Generator", font=("Arial", 18, "bold"),bg="#FAF3F0")
heading_label.grid(pady=10, column=1, columnspan=10)
    
name_label = tk.Label(window, text="Name:", font=("Arial", 12),bg="#FAF3F0")
name_label.grid(row=1, column=1, padx=10, pady=15)

name_entry = tk.Entry(window, width=30)
name_entry.grid(row=1, column=2, padx=10, pady=15)

length_label = tk.Label(window, text="Password Length:", font=("Arial", 12),bg="#FAF3F0")
length_label.grid(row=2, column=1, padx=10, pady=15)

length_entry = tk.Entry(window, width=30)
length_entry.grid(row=2, column=2, padx=10, pady=15)

complexity_label = tk.Label(window, text="Complexity Level:", font=("Arial", 12),bg="#FAF3F0")
complexity_label.grid(row=3, column=1, padx=10, pady=15)

complexity_var = tk.StringVar()
complexity_var.set("low")

complexity_radio_low = tk.Radiobutton(window, text="Low", variable=complexity_var, value="low",bg="#FAF3F0")
complexity_radio_low.grid(row=3, column=2, padx=10, pady=15)

complexity_radio_high = tk.Radiobutton(window, text="High", variable=complexity_var, value="high",bg="#FAF3F0")
complexity_radio_high.grid(row=4, column=2, padx=10, pady=15)

generate_password_button = tk.Button(window, text="Generate Password", command=generate_pwd1, font=("Arial", 12), bg="#FAF3F0" )
generate_password_button.grid(row=5, column=1, columnspan=19, padx=10, pady=10)

result_label = tk.Label(window, text="", wraplength=400, bg="#FAF3F0", font=("Arial", 12))
result_label.grid(row=6, column=1, columnspan=2, padx=10, pady=15)

window.mainloop()

