import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from fungsi_umum import daftar_produk
from fungsi_bos import hapus_rating, daftar_akun, laporan

def menu_boss():
    while True:
        jud_utama()
        jud_sub("Selamat Datang Bos!")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Daftar Akun",
                    "2. Daftar Produk",
                    "3. Hapus Rating",
                    "4. Laporan Penjualan",
                    "5. Logout"])]
        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Daftar Akun":
            jud_utama()
            jud_sub("Daftar Akun")
            daftar_akun()
        elif answer == "2. Daftar Produk":
            jud_utama()
            jud_sub("Daftar Produk")
            daftar_produk()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif answer == "3. Hapus Rating":
            jud_utama()
            jud_sub("Hapus Rating")
            hapus_rating()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif answer == "4. Laporan Penjualan":
            jud_utama()
            jud_sub("Laporan Penjualan")
            laporan()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif answer == "5. Logout":
            pesan_berhasil("Logout Berhasil!")
            break