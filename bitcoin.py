import requests
import tkinter as tk
from datetime import timedelta


def trackBitcoin():
    url = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,JPY,EUR'
    response = requests.get(url).json()
    price = response['USD']
    time = timedelta.now().strftime('%H:%M:%S')
    print(price)

    labelPrice.config(text=str(price) + ' $')
    labelTime.config(text='Updated at: ' + time)

    canvas.after(1000, trackBitcoin)


canvas = tk.Tk()
canvas.geometry('400x500')
canvas.title('Bitcoin Tracker')

f1 = ('popins', 24, 'bold')
f2 = ('popins', 22, 'bold')
f3 = ('popins', 18, 'normal')

label = tk.Label(canvas, text='Bitcoin Price', font=f1)
label.pack(pady=20)

labelPrice = tk.Label(canvas, font=f2)
label.pack(pady=20)

labelTime = tk.Label(canvas, font=f3)
labelTime.pack(pady=20)

trackBitcoin()

canvas.mainloop()
