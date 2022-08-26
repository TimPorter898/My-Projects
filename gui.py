from tkinter import Label, StringVar, OptionMenu, Button,Toplevel, Entry, messagebox
from currencyconverter import CURRENCY_USD, CurrencyConverter
import tkinter as tk

def drop_down(col_placement, selection):
    drop = OptionMenu(root, selection, *options).grid(column=col_placement, row=2)

def show():
    initial_currency = selection.get()
    final_currency = selection_2.get()
    user_amount = float(amount.get())
    usd = CurrencyConverter.to_usd(initial_currency,user_amount)
    final_amount = CurrencyConverter.to_desired_currency(usd, final_currency)
    final_amount = round(final_amount,3)
    message(final_currency, final_amount)


def message(final_currency, final_amount):
    toplevel = Toplevel(root)
    toplevel.grid()
    toplevel.geometry("310x100")
    toplevel.title("Conversion complete")
    Label(toplevel, text= "Your amount in "+final_currency+ ": " +str(final_amount)).grid(column=2,row=2)
    Button(toplevel, text="Close", command=lambda: toplevel.destroy()).grid(column=2,row=3)


root = tk.Tk()
root.geometry("750x150")
root.title("Currency Exchanger")
root.grid()
#------------------------Drop Down-------------------------

options = [key for key in CURRENCY_USD]

selection = StringVar()
selection.set('USD')
initial_denomination = drop_down(1, selection)

selection_2 = StringVar()
selection_2.set('USD')
requested_denomination = drop_down(3, selection_2)

#----------------------------Labels---------------
Label(root,text="Select your current currency below").grid(columnspan=1, column=1, row=1)

Label(root,text="Select your desired currency below").grid(columnspan=1, column=3, row=1)


# ---------------Buttons---------------------------------
convert = Button(root, text="Convert", command=show, width=30).grid(column=2, row=3)

quit = Button(root, text="Exit", command=lambda:root.destroy(), width=10).grid(column=3, row=4,sticky="e")



#------------------------Entry Box---------------------------
amount = StringVar()
amount.set('10')
amount_entry = Entry(root, textvariable=amount, bd=5).grid(column=2, row=2)


root.mainloop()