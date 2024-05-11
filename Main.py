import tkinter as tk
import time
import pyautogui
from tkinter import *
from PIL import ImageTk, Image

pencere = tk.Tk()
pencere.geometry("410x500")
pencere.title("Clickpro auto-clicker")
pencere.configure(bg="lightblue")

resim = ImageTk.PhotoImage(Image.open("images/upgrade.jpg"))
label = Label(image=resim)
label.grid(row=1, columnspan=2)

def sonsuz_auto_click_işlevi():
    while True:
        time.sleep(0.1)
        pyautogui.leftClick()

def double_click():
    while True:
        time.sleep(0.1)
        pyautogui.doubleClick()


bilgi = tk.Label(text="""Başlat butonuna tıkladıktan sonra
3 saniye içinde tıklamasını istediğiniz
konuma farenizi yerleştirin""", font="Courier 13 bold", fg="black", bg="lightblue")

double_butonu = tk.Button(text="start doubleclick", font="Courier 15 bold", command=double_click)
sınırsız_butonu = tk.Button(text="start click", font="Courier 17 bold", command=sonsuz_auto_click_işlevi)


# Konumlar
double_butonu.grid(row=0, column=0)
sınırsız_butonu.grid(row=0, column=1)
bilgi.grid(row=1, column=0, columnspan=2)


pencere.mainloop()
