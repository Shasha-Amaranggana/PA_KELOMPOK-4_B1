import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from fungsi_umum import daftar_akun, daftar_produk

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
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif answer == "2. Daftar Produk":
            jud_utama()
            jud_sub("Daftar Produk")
            daftar_produk()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif answer == "3. Hapus Rating":
            print("d")
        elif answer == "4. Laporan Penjualan":
            print("Laporan Penjualan")
        elif answer == "5. Logout":
            pesan_berhasil("Logout Berhasil!")
            break