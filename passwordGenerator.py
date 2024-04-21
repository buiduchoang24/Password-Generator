from tkinter import *
from tkinter import IntVar
import random
import string
import os
import time

root = Tk()
p1 = PhotoImage(file = 'lock.png')
root.iconphoto(False, p1)
root.title('My Password Generator')
root.geometry("500x800")

named_tuple = time.localtime()
time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)

# Function to generate password
def generate_password():
    # define variables
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    numbers = False
    special_characters = False

    # Check if user wants to add numbers, special characters
    if var1.get() == 1:
        numbers = True
    if var2.get() == 1:
        special_characters = True

    # If Checkbox is clicked, assign characters
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    # Clear content of Password Box
    pw_entry.delete(0, END)

    # Get the length
    pw_length = int(my_entry.get())

    # variable that contains password
    psw = ''
    for x in range(pw_length):
       new_char = random.choice(characters)
       psw += new_char

    pw_entry.insert(0, psw)
   
# Fuction to copy
def copy_func():
    # Clear clipboard
    root.clipboard_clear()
    # Copy to clipboard
    root.clipboard_append(pw_entry.get())

# Function to save
def save_file():
    psfile = 'urStrongPass'
    filename = psfile + '.txt'

    if os.path.exists(filename):
        mode = 'a'
    else:
        mode = 'w'
    # Save to file
    with open(filename, mode) as f:
        f.write(str(time_string) + ', Password: ' + str(pw_entry.get()) + '\n')
        f.close()

# Label
lb = LabelFrame(root, text="How many characters do you want?")
lb.pack(pady=20)

# Entry Box
my_entry = Entry(lb, font=("Montserrat", 24))
my_entry.pack(pady=20, padx=20)

# Entry Box Password
pw_entry = Entry(root, text='', font=("Montserrat", 24))
pw_entry.pack(pady=20)

# Frame for Buttons
frame = Frame(root)
frame.pack(pady=20)

# Checkbox Numbers
var1 = IntVar()
checkNum = Checkbutton(frame, variable=var1, text="Numbers")
checkNum.grid(row=1, column=0)

# Checkbox Special Character
var2 = IntVar()
checkSpec = Checkbutton(frame, variable=var2, text="Special Characters")
checkSpec.grid(row=2, column=0)

# Buttons
my_btn = Button(frame, text="Generate Strong Password", command=generate_password)
my_btn.grid(row=4, column=0, padx=10)

copy_button = Button(frame, text="Copy To Clipboard", command=copy_func)
copy_button.grid(row=4, column=1, padx=10)

save_button = Button(frame, text="Save To File", command=save_file)
save_button.grid(row=2, column=1)

root.mainloop()
