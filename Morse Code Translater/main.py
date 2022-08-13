from tkinter import *
import tkinter as tk
from tkinter import simpledialog
from copylabel import CopyLabel
from translater import Translater
from tkinter import messagebox

def morse_code():
    try:
        answer = simpledialog.askstring("Translater", "Text for conversion:")
        answer = Translater.to_morse_code(answer)
        CopyLabel(answer)
    except:
        messagebox.showerror("Error", "An error has occurred.")

def english():
    try:
        answer = simpledialog.askstring("Translater", "Text for conversion:")
        answer = Translater.to_english(answer)
        CopyLabel(answer)
    except:
        messagebox.showerror("Error", "An error has occurred.")

root = Tk()
frm = tk.Frame(root)
root.title('Morse Code Translater for Encryption')
root.geometry('880x400')
frm.grid()

greeting_statement = Label(root, text="Welcome to the morse code enryption program.\n" \
                     "Choose to turn your message into morse code or morse code to english.\n" \
                     "let us handle everything else.",font=("Aerial", 20)).grid(columnspan=4, column=3, row=0)

to_english_button = tk.Button(root, text="To English", width=30, height=2, command=(lambda: (english()))).grid(columnspan=1,column=4, row=3)
to_morse_code_button = tk.Button(root, text="To Morse Code", width=30,height=2, command=(lambda: (morse_code()))).grid(columnspan=1, column=5, row=3)


root.mainloop()


