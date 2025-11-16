import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan

def menu_boss():
    jud_utama()
    jud_sub("Selamat Datang Bos!")
    while True:
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Akun",
                    "2. Daftar Produk",
                    "3. Logout"])]
        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Akun":
            print("Akun")
        elif answer == "2. Daftar Produk":
            print("Daftar Produk")
        elif answer == "3. Logout":
            pesan_berhasil("Logout Berhasil!")
            break