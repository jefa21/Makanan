import os
import time
import math

lapisan = [
    "   _______   ",  # Roti atas
    "  /       \\  ",
    " |  ROTI   | ",
    " |  SELADA | ",
    " |  TOMAT  | ",
    " |  KEJU   | ",
    " |  DAGING | ",
    " \\_______/  ",  # Roti bawah
]

warna = [
    "\033[93m",  # kuning muda (roti)
    "\033[92m",  # hijau (selada)
    "\033[91m",  # merah (tomat)
    "\033[93m",  # kuning (keju)
    "\033[95m",  # ungu (daging)
]

RESET = "\033[0m"

def bersihkan():
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilinBurger(berapaLapisan):
    bersihkan()
    for i in range(berapaLapisan):
        baris = lapisan[i]
        # Tambahkan warna sesuai urutan lapisan
        if "ROTI" in baris:
            warnaTeks = warna[0]
        elif "SELADA" in baris:
            warnaTeks = warna[1]
        elif "TOMAT" in baris:
            warnaTeks = warna[2]
        elif "KEJU" in baris:
            warnaTeks = warna[3]
        elif "DAGING" in baris:
            warnaTeks = warna[4]
        else:
            warnaTeks = RESET
        print(warnaTeks + baris + RESET)
    print()

def putarBurger():
    bersihkan()
    sudut = 0
    for _ in range(50):
        bersihkan()
        print("BURGER BERPUTAR!\n")
        for i in range(len(lapisan)):
            geser = int(10 * math.sin(sudut + i))
            spasi = " " * (10 + geser)
            baris = lapisan[i]
            print(spasi + baris)
        time.sleep(0.05)
        sudut += 0.3

def burgerMeledak():
    bersihkan()
    for i in range(len(lapisan)):
        geser = " " * (i * 3)
        print(f"{geser}{lapisan[i]}")
        time.sleep(0.1)

# Animasi utama
def main():
    for i in range(1, len(lapisan) + 1):
        tampilinBurger(i)
        time.sleep(0.3)

    putarBurger()

    burgerMeledak()

if __name__ == "__main__":
    main()
