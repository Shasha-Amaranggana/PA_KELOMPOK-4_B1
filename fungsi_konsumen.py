import inquirer
from data_konsumen import akun, produk, keranjang, pesanan, riwayat, rating, saldo
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from fungsi_umum import daftar_produk

def lihat_akun():
    while True:
        jud_utama()
        jud_sub("Akun Anda")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Lihat Akun",
                    "2. Edit data diri",
                    "3. Kembali"])]
        answer = inquirer.prompt(questions)["menu"]
        if answer == "1. Lihat Akun":
            lihat_akun()
        elif answer == "2. Menu Akun Konsumen":
            edit_data_diri()
        elif answer == "3. Kembali":
            break

def lihat_produk():
    while True:
        jud_utama()
        jud_sub("Akun Anda")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Lihat Produk",
                    "2. Kembali"])]
        answer = inquirer.prompt(questions)["menu"]
        if answer == "1. Lihat Produk":
            lihat_produk()
        elif answer == "2. Kembali":
            break