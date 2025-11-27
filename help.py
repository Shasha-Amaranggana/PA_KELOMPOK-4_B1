import os
from colorama import Fore, Style, init
init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def jud_utama(): 
    clear()
    print(("═"*70))
    print("WEBSITE PENJUALAN PRODUK POPCORN".center(70))
    print(("═"*70))

def jud_sub(judul):
    print(("═"*50).center(70))
    print(judul.center(70))
    print(("═"*50).center(70))
    print("")

def inp_no():
    print("")
    print(("═"*50).center(70))
    menu = input("╰┈➤  Masukkan nomor yang ingin dipilih (ketik 'kembali' untuk kembali): ").strip().lower()
    print("")
    return menu

def pesan_berhasil(pesan):
    print("")
    print(Style.RESET_ALL + Fore.GREEN + ("═" * 20).center(70))
    print(Fore.GREEN + Style.BRIGHT + pesan.center(70))
    print(Fore.GREEN + ("═" * 20).center(70) + Style.RESET_ALL)
    print("")

def pesan_peringatan(pesan, warna, jumlah):
    print("")
    print(Style.RESET_ALL + warna + ("──" * jumlah).center(70))
    print(warna + Style.BRIGHT + pesan.center(70))
    print(warna + ("──" * jumlah).center(70) + Style.RESET_ALL)
    print("")

def inp_enter():
    print(("═"*70))
    input("→ 「Enter untuk kembali」")