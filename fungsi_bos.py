from data import akun, produk
import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_no
from fungsi_umum import daftar_produk

# FUNGSI BOS 1
# ════════════════════════════════════════════════════
def daftar_akun():
    while True:
        jud_utama()
        jud_sub("Daftar Akun")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Menu Akun Seller",
                    "2. Menu Akun Konsumen",
                    "3. Kembali"])]
        answer = inquirer.prompt(questions)["menu"]
        if answer == "1. Menu Akun Seller":
            menu_akun_seller()
        elif answer == "2. Menu Akun Konsumen":
            menu_akun_konsumen()
        elif answer == "3. Kembali":
            break

def hapus_rating():
    while True:
        jud_utama()
        jud_sub("Hapus Rating")
        daftar_produk()
        no_char = input("Masukkan nomor produk (atau ketik 'kembali' untuk keluar): ").strip().lower()
        if no_char == "kembali":
            return None
        if not no_char.isdigit():
            pesan_peringatan("Input harus berupa angka!", 15)
            continue
        no_char = int(no_char)
        if not (1 <= no_char <= len(daftar_produk)):
            pesan_peringatan("Nomor produk tidak ditemukan!", 15)
        nomor = list(daftar_produk.keys())[no_char - 1]
        if nomor == "update":
            pesan_peringatan("Produk ini tidak bisa dihapus!", 15)
            continue
        pesan_berhasil("Rating berhasil dihapus!")
        break   # keluar setelah sukses

def laporan():
    while True:
        jud_utama()
        jud_sub("Menu Akun Seller")

def menu_akun_seller():
    while True:
        jud_utama()
        jud_sub("Menu Akun Seller")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Daftar Akun Seller",
                    "2. Buat Akun Seller",
                    "3. Ubah Status Akun Seller",
                    "4. Aktivitas Akun Seller",
                    "5. Kembali"])]
        answer = inquirer.prompt(questions)["menu"]
        if answer == "1. Daftar Akun Seller":
            daftar_seller()
        elif answer == "2. Buat Akun Seller":
            regist_seller()
        elif answer == "3. Ubah Status Akun Seller":
            status_seller()
        elif answer == "4. Aktivitas Akun Seller":
            akt_seller()
        elif answer == "5. Kembali":
            break

def menu_akun_konsumen():
    while True:
        jud_utama()
        jud_sub("Menu Akun Konsumen")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Daftar Akun Konsumen",
                    "2. Ubah Status Akun Konsumen",
                    "3. Aktivitas Akun Konsumen",
                    "4. Kembali"])]
        answer = inquirer.prompt(questions)["menu"]
        if answer == "1. Daftar Akun Konsumen":
            daftar_konsumen()
        elif answer == "2. Ubah Status Akun Konsumen":
            status_konsumen()
        elif answer == "3. Aktivitas Akun Konsumen":
            akt_konsumen()
        elif answer == "4. Kembali":
            break
