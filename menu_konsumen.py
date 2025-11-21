import inquirer
from help import jud_utama, jud_sub, pesan_berhasil
from fungsi_konsumen import lihat_akun, lihat_produk


def menu_konsumen(username):
    while True:
        jud_utama()
        jud_sub(f"Selamat Datang, {username}!")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1 | LIHAT AKUN",
                    "2 | LIHAT PRODUK",
                    "3 | KERANJANG BELANJA",
                    "4 | PESANAN ANDA",
                    "5 | RIWAYAT",
                    "6 | SALDO",
                    "7 | LOGOUT"])]
        answer = inquirer.prompt(questions)["menu"]

        if answer == "1 | LIHAT AKUN":
            jud_utama()
            jud_sub("Akun Saya")
            lihat_akun(username)
        elif answer == "2 | LIHAT PRODUK":
            jud_utama()
            jud_sub("Daftar Produk")
            lihat_produk()
        elif answer == "3 | KERANJANG BELANJA":
            jud_utama()
            jud_sub("Keranjang Belanja")
            keranjang_belanja(username)
        elif answer == "4 | PESANAN ANDA":
            jud_utama()
            jud_sub("Pesanan Anda")
            pesanan_anda(username)
        elif answer == "5 | RIWAYAT":
            jud_utama()
            jud_sub("Riwayat Belanja")
            riwayat(username)
        elif answer == "6 | SALDO":
            jud_utama()
            jud_sub("Saldo")
            saldo(username)
        elif answer == "7 | LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break