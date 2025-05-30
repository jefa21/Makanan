import os
import time
import math

# Lapisan burger tanpa teks (hanya bentuk visual)
lapisan = [
    "   ███████   ",  # Roti atas
    "  █████████  ",
    " ███████████ ",  # Selada
    " ███████████ ",  # Tomat
    " ███████████ ",  # Keju
    " ███████████ ",  # Daging
    "  █████████  ",
    "   ███████   ",  # Roti bawah
]

# Warna ANSI untuk masing-masing lapisan
warna = [
    "\033[93m",  # Roti atas
    "\033[93m",  # Roti atas bawah
    "\033[92m",  # Selada
    "\033[91m",  # Tomat
    "\033[93m",  # Keju
    "\033[95m",  # Daging
    "\033[93m",  # Roti bawah
    "\033[93m",  # Roti bawah
]

RESET = "\033[0m"

def bersihkan():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilinBurger(berapaLapisan):
    bersihkan()
    for i in range(berapaLapisan):
        warnaTeks = warna[i] if i < len(warna) else RESET
        print(warnaTeks + lapisan[i] + RESET)
    print()

def putarBurger():
    sudut = 0
    for _ in range(60):
        bersihkan()
        print("🍔 BURGER MUTER DULU!\n")
        for i in range(len(lapisan)):
            offset = int(10 * math.sin(sudut + i))
            spasi = " " * (10 + offset)
            print(spasi + warna[i] + lapisan[i] + RESET)
        time.sleep(0.04)
        sudut += 0.3

def burgerSleketew():
    bersihkan()
    for i in range(len(lapisan)):
        spasi = " " * (i * 3)
        print(spasi + warna[i] + lapisan[i] + RESET)
        time.sleep(0.1)

# Animasi utama
def main():
    for i in range(1, len(lapisan) + 1):
        tampilinBurger(i)
        time.sleep(0.3)
    putarBurger()
    burgerSleketew()

if __name__ == "__main__":
    main()
