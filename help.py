import os
import inquirer

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def jud_utama(): 
    clear()
    print("═"*70)
    print("WEBSITE PENJUALAN PRODUK POPCORN".center(70))
    print("═"*70)

def jud_sub(judul):
    print(("═"*40).center(70))
    print(judul.center(70))
    print(("═"*40).center(70))
    print("")

def inp_menu():
    print("")
    print(("═"*50).center(70))
    menu = input("╰┈➤  Pilih menu: ")
    return menu

def inp_no():
    print("")
    print(("═"*50).center(70))
    menu = input("╰┈➤  Masukkan nomor yang ingin dipilih (jika ingin kembali, ketik 'kembali'): ").strip().lower()
    print("")
    return menu

def pesan_berhasil(pesan):
    print("")
    print(("═"*20).center(70))
    print(pesan.center(70))
    print(("═"*20).center(70))
    print("")

def pesan_peringatan(pesan, jumlah):
    print("")
    print("──" * jumlah)
    print(pesan)
    print("──" * jumlah)
    print("")

