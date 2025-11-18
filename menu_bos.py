import inquirer
import re
from data import akun
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from fungsi_umum import daftar_produk

# FUNGSI BOS 1
# ════════════════════════════════════════════════════
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

# FUNGSI BOS 2
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
        break

def daftar_produk():
    global produk
    if len(produk) == 0:
        pesan_berhasil("Daftar produk belum ada.")
    else:
        print("ID     NAMA       UKURAN     HARGA      STOK       RATE")
        print("──" * 30)
        no = 1
        for nomor, k in produk.items():
            print(no,"| ", k["nm"], " "*(14 - len(k["nm"])), k["sz"], " "*(9 - len(k["sz"])), k["pz"], " "*(11 - len(k["pz"])), k["stk"], " "*(9 - len(k["stk"])), k["rt"])
            no = no + 1

def laporan():
    print("belum kepikiran")

# FUNGSI BOS 3
# ════════════════════════════════════════════════════
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
            jud_utama()
            jud_sub("Daftar Produk")
            daftar_seller()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif answer == "2. Buat Akun Seller":
            jud_utama()
            jud_sub("Daftar Produk")
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
            jud_utama()
            jud_sub("Daftar Produk")
            daftar_konsumen()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif answer == "2. Ubah Status Akun Konsumen":
            status_konsumen()
        elif answer == "3. Aktivitas Akun Konsumen":
            akt_konsumen()
        elif answer == "4. Kembali":
            break

# FUNGSI BOS 4
# ════════════════════════════════════════════════════
def daftar_seller():
    global akun
    seller_list = {}
    for nomor, k in akun.items():
        if k["role"] == "seller":
            seller_list[nomor] = k
    if len(seller_list) == 0:
        pesan_berhasil("Daftar akun seller belum ada.")
    else:
        print("ID     USERNAME       ROLE     STATUS      TERDAFTAR PADA TANGGAL")
        print("──" * 30)
        no = 1
        for nomor, k in seller_list.items():
            print(
                no, "| ",
                k["us"], " " * (14 - len(k["us"])),
                k["role"], " " * (9 - len(k["role"])),
                k["status"], " " * (11 - len(k["status"])),
                k["tgl"])
            no += 1

def regist_seller():
    jud_utama()
    jud_sub("Silakan Registrasi")
    print("   > Username min 5 karakter, mengandung huruf/angka,")
    print("     tidak mengandung karakter spesial!")
    print("   > Password min 8 karakter, mengandung huruf besar & kecil & angka,")
    print("     tidak mengandung karakter spesial!")
    print("")
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if username == "" or password == "":
            pesan_peringatan("Semua kolom harus diisi!", 12)
            raise ValueError
        elif not re.search(r"^[a-zA-Z0-9]{4,}$", username):
            pesan_peringatan("Sesuaikan dengan syarat yang tersedia", 12)
            raise ValueError
        else:
            pola_pw = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
            if not re.search(pola_pw, password):
                pesan_peringatan("Sesuaikan dengan syarat yang tersedia", 12)
                raise ValueError
            else:
                for nomor, user in akun.items():
                    if user["us"] == username:
                        pesan_peringatan("User telah tersedia", 12)
                        raise ValueError
                akun.update({
                    str(len(akun)+1): {
                        "us": username,
                        "pw": password,
                        "role": "seller",
                        "status" : "Aktif",
                        "tgl" : ""}})
                pesan_berhasil("Akun seller berhasil dibuat!") 
                input("→ 「 Enter untuk kembali 」")
                return True
    except ValueError:
        input("→ 「 Enter untuk kembali 」")
        return None

def stat_seller():
    while True:
        jud_utama()
        jud_sub("Status Seller")
        daftar_seller()
        global akun
        print("\nKetik 'kembali' untuk keluar.")
        no_char = input("Pilih nomor akun seller: ").strip()
        if no_char == "kembali":
            return None
        if not no_char.isdigit():
            pesan_peringatan("Input harus berupa angka!", 15)
            continue
        no_char = int(no_char)
        daftar_seller_ids = list({nomor: k for nomor, k in akun.items() if k["role"] == "seller"}.keys())
        if not (1 <= no_char <= len(daftar_seller_ids)):
            pesan_peringatan("Nomor akun seller tidak ditemukan!", 15)
            continue
        akun_id = daftar_seller_ids[no_char - 1]
        data_seller = akun[akun_id]
        print("\nPKonfirmasi status akun:")
        print("1. Aktifkan akun")
        print("2. Nonaktifkan akun")
        print("3. Hapus akun")
        tindakan = input("Masukkan pilihan: ").strip()
        if tindakan == "1":
            akun[akun_id]["status"] = "Aktif"
            pesan_berhasil("Akun berhasil diaktifkan!")
        elif tindakan == "2":
            akun[akun_id]["status"] = "Nonaktif"
            pesan_berhasil("Akun berhasil dinonaktifkan!")
        elif tindakan == "3":
            del akun[akun_id]
            pesan_berhasil("Akun berhasil dihapus!")
        else:
            pesan_peringatan("Pilihan tindakan tidak valid!", 15)
            continue

def daftar_konsumen():
    jud_utama()
    jud_sub("Daftar Konsumen")
    global akun
    konsumen_list = {}
    for nomor, k in akun.items():
        if k["role"] == "seller":
            konsumen_list[nomor] = k
    if len(konsumen_list) == 0:
        pesan_berhasil("Daftar akun konsumen belum ada.")
    else:
        print("ID     USERNAME       ROLE     STATUS      TERDAFTAR PADA TANGGAL")
        print("──" * 30)
        no = 1
        for nomor, k in konsumen_list.items():
            print(
                no, "| ",
                k["us"], " " * (14 - len(k["us"])),
                k["role"], " " * (9 - len(k["role"])),
                k["status"], " " * (11 - len(k["status"])),
                k["tgl"])
            no += 1
