# Telur Ceplok ASCII berkedip di terminal
# Dibuat oleh Jefanniel Nathan
# Terinspirasi dari teknik ASCII Donut (Andy Sloane)
import os
import time

# Warna ANSI
putih_telur = "\033[47m \033[0m" 
kuning1 = "\033[43m \033[0m"
kuning2 = "\033[103m \033[0m"

bingkai = [
    "       *****       ",
    "    ***********    ",
    "  ***************  ",
    " ***************** ",
    "*******************",
    "*****       *******",
    "****         ******",
    "***           *****",
    "**             ****",
    "*               ***",
]

def tampilkanTelur(kuning_aktif):
    os.system('cls' if os.name == 'nt' else 'clear')

    for y, baris in enumerate(bingkai):
        barisOutput = ""
        for x, karakter in enumerate(baris):
            if 7 <= x <= 11 and 2 <= y <= 6:
                barisOutput += kuning_aktif
            elif karakter == "*":
                barisOutput += putih_telur
            else:
                barisOutput += " "
        print(barisOutput)

# Animasi
while True:
    tampilkanTelur(kuning1)
    time.sleep(0.5)
    tampilkanTelur(kuning2)
    time.sleep(0.5)
