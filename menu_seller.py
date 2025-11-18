import os
import inquirer
from prettytable import PrettyTable
from colorama import Fore, Style
from colorama import Fore, Style, init
init(autoreset=True)


current_seller = {
    "username": "seller1",
    "nama": "khanza",
    "email": "seller1@gmail.com",
    "no_hp": "08123456789"
}

## daftar produk popcorn
produk_list = [
    # popcorn rasa caramel
    {"id": "C1", "varian": "Caramel",  "kemasan": "Small",  "harga": 5000,  "status": "Tersedia"},
    {"id": "C2", "varian": "Caramel",  "kemasan": "Medium", "harga": 10000, "status": "Tersedia"},
    {"id": "C3", "varian": "Caramel",  "kemasan": "Large",  "harga": 18000, "status": "Tersedia"},

    # popcorn rasa blueberry
    {"id": "B1", "varian": "Blueberry","kemasan": "Small",  "harga": 5000,  "status": "Tersedia"},
    {"id": "B2", "varian": "Blueberry","kemasan": "Medium", "harga": 10000, "status": "Tersedia"},
    {"id": "B3", "varian": "Blueberry","kemasan": "Large",  "harga": 18000, "status": "Tersedia"},

    # popcorn rasa matcha
    {"id": "M1", "varian": "Matcha",   "kemasan": "Small",  "harga": 5000,  "status": "Tersedia"},
    {"id": "M2", "varian": "Matcha",   "kemasan": "Medium", "harga": 10000, "status": "Tersedia"},
    {"id": "M3", "varian": "Matcha",   "kemasan": "Large",  "harga": 18000, "status": "Tersedia"},
]

# kosong karena perlu input dari user
pesanan_list = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# MENU SELLER UTAMA
def menu_seller():
    while True:
        clear()
        print("=== MENU SELLER POPCORN ===")
        pertanyaan_menu = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "Akun",
                    "Penjualan",
                    "Pembelian",
                    "Pemesanan",
                    "Status Pemesanan",
                    "Logout"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan_menu)
        if jawaban is None:
            break

        menu = jawaban["menu"]

        if menu == "Akun":
            menu_akun()
        elif menu == "Penjualan":
            menu_penjualan()
        elif menu == "Pembelian":
            menu_pembelian()
        elif menu == "Pemesanan":
            menu_pemesanan()
        elif menu == "Status Pemesanan":
            menu_status_pemesanan()
        elif menu == "Logout":
            break