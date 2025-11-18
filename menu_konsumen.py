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
                    "1. Lihat Akun",
                    "2. Lihat Produk",
                    "3. Keranjang Belanja",
                    "4. Pesanan Anda",
                    "5. Riwayat",
                    "6. Rating",
                    "7. Saldo",
                    "8. Logout"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Lihat Akun":
            jud_utama()
            jud_sub("Akun Saya")
            lihat_akun(username)

        elif answer == "2. Lihat Produk":
            jud_utama()
            jud_sub("Daftar Produk")
            lihat_produk()

        elif answer == "3. Keranjang Belanja":
            jud_utama()
            jud_sub("Keranjang Belanja")
            keranjang_belanja(username)

        elif answer == "4. Pesanan Anda":
            jud_utama()
            jud_sub("Pesanan Anda")
            pesanan_anda(username)

        elif answer == "5. Riwayat":
            jud_utama()
            jud_sub("Riwayat Belanja")
            riwayat(username)

        elif answer == "6. Rating":
            jud_utama()
            jud_sub("Rating Produk")
            rating(username)

        elif answer == "7. Saldo":
            jud_utama()
            jud_sub("Saldo")
            saldo(username)

        elif answer == "8. Logout":
            pesan_berhasil("Logout Berhasil!")
            break
