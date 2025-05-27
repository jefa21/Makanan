# Pizza ASCII berputar di terminal
# Dibuat oleh Jefanniel Nathan
# Terinspirasi dari teknik ASCII Donut (Andy Sloane)
import os
import time
import math
import random

lebar = 40
tinggi = 20
topping = ['*', '@', 'o', ' ']
slicePizza = ['\\', '|', '/', '-', '\\', '|', '/', '-']

def bersih():
    os.system("cls" if os.name == "nt" else "clear")

def gambarPizza(rotasi):
    bersih()
    for y in range(-tinggi, tinggi):
        baris = ""
        for x in range(-lebar, lebar):
            # Koreksi bentuk elips karena terminal tidak square
            jarak = math.sqrt((x / 2)**2 + y**2)
            if 18 < jarak < 20:
                baris += "#"
            elif jarak <= 18:
                sudut = math.atan2(y, x)
                indeks = int(((sudut + math.pi) / (2 * math.pi)) * len(slicePizza))
                indeks = (indeks + rotasi) % len(slicePizza)
                # Random topping dengan slice di atasnya
                if random.random() < 0.05:
                    baris += random.choice(topping)
                else:
                    baris += slicePizza[indeks]
            else:
                baris += " "
        print(baris)

# Animasi berputar
rotasi = 0
while True:
    gambarPizza(rotasi)
    rotasi = (rotasi + 1) % len(slicePizza)
    time.sleep(0.25)
