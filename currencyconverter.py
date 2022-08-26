from tkinter import simpledialog
import tkinter as tk
CURRENCY_USD = {"USD": 1.00, "YEN":135.28, "EUR":0.98, "MXN":20.15, "CNY": 6.87, "CAD":1.3}

class CurrencyConverter():

    def to_usd(currency, user_amount):
        usd = user_amount/CURRENCY_USD[currency]
        return usd

    def to_desired_currency(amount, currency):
        converted_currency = amount * CURRENCY_USD[currency]
        return converted_currency

    def convert_to_usd(currency):
        amount = simpledialog.askfloat("Amount", f"Enter {currency} amount: ")
        amount = float(amount)
        usd_amount = CurrencyConverter.to_usd(amount, currency)
        return usd_amount


