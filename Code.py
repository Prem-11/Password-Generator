import tkinter as tk
import tkinter.font as font
from tkinter import *
from tkinter.ttk import *
import pyperclip
import random
import string
from tkinter import Button

master = tk.Tk()
master.geometry("700x500")
master.configure(bg="#856ff8")
master.title("Password Generator")

def generate_password():
    length = int(length_entry.get())
    complexity = complexity_var.get()
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation.replace(" ", "")
    
    if complexity == 1:  # Low complexity
        chars = uppercase + lowercase
    elif complexity == 2:  # Medium complexity
        chars = uppercase + lowercase + digits
    else:  # High complexity
        chars = uppercase + lowercase + digits + punctuation

    password = random.choice(uppercase)  # Ensure at least one uppercase letter
    password += ''.join(random.choice(chars) for _ in range(length - 1))
    
    password = shuffle(password)
    password_label.config(text="Your Generated password is: " + password)

def copy_password():
    pyperclip.copy(password_label.cget("text").replace("Your Generated password is: ", ""))
    copied_label.config(text="Your password has been copied to Clipboard!")

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# UI elements
title_label = Label(master, text="Password Generator", font=("Arial", 20))
title_label.pack(pady=20)

length_label = Label(master, text="Enter the length of password:"    )
length_label.pack()

length_entry = Entry(master     )
length_entry.pack(pady=10)

complexity_label = Label(master, text="Select the complexity:" )
complexity_label.pack()

complexity_var = IntVar()
low_complexity_radio = Radiobutton(master, text="Low", variable=complexity_var, value=1  )
low_complexity_radio.pack()

medium_complexity_radio = Radiobutton(master, text="Medium", variable=complexity_var, value=2 )
medium_complexity_radio.pack()

high_complexity_radio = Radiobutton(master, text="High", variable=complexity_var, value=3  )
high_complexity_radio.pack()

generate_button = Button(master, text="Generate Password", padx=50, pady=20, command=generate_password )
generate_button.pack(pady=20)

password_label = Label(master )
password_label.pack()

copy_button = Button(master, text="Copy Password", padx=20, pady=10  , command=copy_password)
copy_button.pack(pady=10)

copied_label = Label(master  )
copied_label.pack()

# Set the default complexity to Low
complexity_var.set(1)

# Configure styles
style = Style()
style.configure("My.TButton"   , foreground="White", background="Black")

# Start the GUI
master.mainloop()