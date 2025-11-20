import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan

def lihat_akun():
    while True:
        jud_utama()
        jud_sub("Akun Anda")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Lihat Akun (data diri)",
                    "2. Edit data diri",
                    "3. Kembali"])]
        
        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Lihat Akun (data diri)":
            lihat_data_diri()
        elif answer == "2. Edit data diri":
            edit_data_diri()
        elif answer == "3. Kembali":
            break
def lihat_produk():
    while True:
        jud_utama()
        jud_sub("Daftar Produk")
        daftar_produk()  

        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Belanja",
                    "2. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Belanja":
            pilih_produk()
        elif answer == "2. Kembali":
            break
