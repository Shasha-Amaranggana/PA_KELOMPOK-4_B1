import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from data_konsumen import keranjang
from menu import daftar_produk
from prettytable import PrettyTable

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
            belanja()
        elif answer == "2. Kembali":
            break
def keranjang_belanja():

    while True:
        jud_utama()
        jud_sub("Keranjang Belanja")

        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Lihat Keranjang Belanja",
                    "2. Edit Keranjang Belanja",
                    "3. Pesan Sekarang",
                    "4. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Lihat Keranjang Belanja":
            lihat_keranjang()

        elif answer == "2. Edit Keranjang Belanja":
            edit_keranjang()

        elif answer == "3. Pesan Sekarang":
            pesan_sekarang()

        elif answer == "4. Kembali":
            break

def belanja():

    while True:
        jud_utama()
        jud_sub("Pesan")
        daftar_produk()  
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Tambah ke Keranjang",
                    "2. Beli Sekarang",
                    "3. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Tambah ke Keranjang":
            tambah_keranjang()

        elif answer == "2. Beli Sekarang":
            beli_sekarang()

        elif answer == "3. Kembali":
            break

def pesanan_anda():
    while True:
        jud_utama()
        jud_sub("Riwayat")

        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Riwayat pemesanan",
                    "2. Edit pemesanan(Cancel)",
                    "3. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Riwayat pemesanan":
            riwayat_pemesanan()

        elif answer == "2. Edit pemesanan(Cancel)":
            edit_pemesanan()

        elif answer == "3. Kembali":
            break

def saldo():
    while True:
        jud_utama()
        jud_sub("Saldo")

        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Saldo Anda",
                    "2. Top Up",
                    "3. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Saldo Anda":
            cek_saldo()

        elif answer == "2. Top Up":
            top_up()

        elif answer == "3. Kembali":
            break
