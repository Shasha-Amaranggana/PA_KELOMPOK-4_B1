import os
import inquirer
from prettytable import PrettyTable
from colorama import Fore, Style
from colorama import Fore, Style, init


current_seller = {
    "username": "seller1",
    "nama": "Khanza",
    "email": "seller1@gmail.com",
    "no_hp": "08123456789"
}

# daftar produk popcorn
produk_list = [
    {"id": 1, "varian": "Caramel", "kemasan": "Small", "harga": 5000, "status": "Tersedia"},
    {"id" : 2, "varian": "Matcha", "kemasan" : "Medium", "harga" : 10000, "status": "Tersedia"},
    {"id" : 3, "varian": "Choco", "kemasan" : "Large", "harga" : 15000, "status": "Habis"}
]

# daftar pesanan (dari user)
pesanan_list = [
    {
    "id_pesanan": 1,
    "nama_user": "Ghina",
    "produk": "CarNMamel - Medium",
    "jumlah": 2,
    "total_harga": 20000,
    "status_pesanan": ""
    }
]

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')