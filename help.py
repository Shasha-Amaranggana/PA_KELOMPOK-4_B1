import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def jud_utama(): 
    clear()
    print("═"*60)
    print("WEBSITE PENJUALAN PRODUK POPCORN".center(60))
    print("═"*60)

def jud_sub(judul):
    print(("═"*40).center(60))
    print(judul.center(60))
    print(("═"*40).center(60))
    print("")

def inp_menu():
    print("")
    print(("═"*50).center(60))
    menu = input("╰┈➤  Pilih menu: ")
    return menu

def inp_nochar():
    print("")
    print(("═"*50).center(60))
    menu = input("╰┈➤  Masukkan nomor karakter yang ingin diupdate: ")
    print("")
    return menu

def pesan_berhasil(pesan):
    print("")
    print(("═"*20).center(60))
    print(pesan.center(60))
    print(("═"*20).center(60))
    print("")

def pesan_peringatan(pesan, jumlah):
    print("")
    print("──" * jumlah)
    print(pesan)
    print("──" * jumlah)
    print("")