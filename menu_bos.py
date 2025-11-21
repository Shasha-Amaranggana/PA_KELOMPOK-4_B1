import inquirer
import re
from prettytable import PrettyTable
from datetime import datetime
from data import akun, produk_list, save_akun_to_csv
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_no

def tamp_bos(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ DAFTAR AKUN'.center(30), '2 │ DAFTAR PRODUK'.center(32), '3 │ LAPORAN PENJUALAN'.center(35),  '4 │ LOGOUT'.center(23)],
        "2.1" : ['1 │ MENU AKUN SELLER'.center(33), '2 │ MENU AKUN KONSUMEN'.center(35), '3 │ KEMBALI'.center(25)],
        "3.1" : ['1 │ DAFTAR AKUN SELLER'.center(35), '2 │ BUAT AKUN SELLER'.center(33), '3 │ UBAH STATUS AKUN SELLER'.center(41), '4 │ KEMBALI'.center(25)],
        "3.2" : ['1 │ DAFTAR AKUN KONSUMEN'.center(37), '2 │ UBAH STATUS AKUN KONSUMEN'.center(43), '3 │ KEMBALI'.center(25)],
        "4.1" : ['1 │ Aktifkan Akun'.center(32), '2 │ Nonaktifkan Akun'.center(35), '3 │ Hapus Akun'.center(29)]}
    choices = daftar_menu[jenis] 
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan 

# FUNGSI BOS 1
# ════════════════════════════════════════════════════
def menu_boss():
    while True:
        jud_utama()
        jud_sub("Selamat Datang Bos!")
        pilih = tamp_bos("1")
        if pilih == "1 │ DAFTAR AKUN":
            jud_utama()
            jud_sub("Daftar Akun")
            daftar_akun()
        elif pilih == "2 │ DAFTAR PRODUK":
            jud_utama()
            jud_sub("Daftar Produk")
            daftar_produk()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "3 │ LAPORAN PENJUALAN":
            jud_utama()
            jud_sub("Laporan Penjualan")
            laporan()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "4 │ LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break

# FUNGSI BOS 2
# ════════════════════════════════════════════════════
def daftar_akun():
    while True:
        jud_utama()
        jud_sub("Daftar Akun")
        pilih = tamp_bos("2.1")
        if pilih  == "1 │ MENU AKUN SELLER":
            menu_akun_seller()
        elif pilih == "2 │ MENU AKUN KONSUMEN":
            menu_akun_konsumen()
        elif pilih == "3 │ KEMBALI":
            break

def daftar_produk():
    global produk_list
    if len(produk_list) == 0:
        print("Daftar produk belum ada.")
        return
    table = PrettyTable()
    table.field_names = ["NO", " ID ", "  VARIAN  ", "UKURAN", "HARGA", " STATUS ", "RATE"]
    for idx, p in enumerate(produk_list, start=1):
        table.add_row([
            idx,
            p["id"],
            p["varian"],
            p["kemasan"],
            f"{p['harga']}",
            p["status"],
            p["rating"]])
    print(table)
    
def laporan():
    print("belum kepikiran")

# FUNGSI BOS 3
# ════════════════════════════════════════════════════
def menu_akun_seller():
    while True:
        jud_utama()
        jud_sub("Menu Akun Seller")
        pilih = tamp_bos("3.1")
        if pilih == "1 │ DAFTAR AKUN SELLER":
            jud_utama()
            jud_sub("Daftar Akun Seller")
            daftar_seller()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "2 │ BUAT AKUN SELLER":
            jud_utama()
            jud_sub("Buat Akun Seller")
            regist_seller()
        elif pilih == "3 │ UBAH STATUS AKUN SELLER":
            stat_seller()
        elif pilih == "4 │ KEMBALI":
            break

def menu_akun_konsumen():
    while True:
        jud_utama()
        jud_sub("Menu Akun Konsumen")
        pilih = tamp_bos("3.2")
        if pilih == "1 │ DAFTAR AKUN KONSUMEN":
            jud_utama()
            jud_sub("Daftar Akun Konsumen")
            daftar_konsumen()
            print("")
            print("═"*60)
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "2 │ UBAH STATUS AKUN KONSUMEN":
            stat_konsumen()
        elif pilih == "3 │ KEMBALI":
            break

# FUNGSI BOS 4
# ════════════════════════════════════════════════════
def daftar_seller():
    global akun
    seller_list = {}
    for id_key, data in akun.items():
        if data["role"] == "Seller":
            seller_list[id_key] = data
    if len(seller_list) == 0:
        pesan_berhasil("Daftar akun seller belum ada.")
        return
    table = PrettyTable()
    table.field_names = ["NO", " ID ", "  USERNAME  ", " ROLE ", " STATUS ", "TERDAFTAR"]
    for idx, (id_key, user) in enumerate(seller_list.items(), start=1):
        table.add_row([
            idx,
            id_key,
            user["us"],
            user["role"],
            user["status"],
            user["tgl"]])
    print(table)

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
        elif not re.search(r"^[a-zA-Z0-9]{5,}$", username):
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
                    str(len(akun)+1):{
                        "us": username,
                        "pw": password,
                        "role": "Seller",
                        "status" : "Aktif",
                        "tgl" : datetime.now().strftime("%Y-%m-%d")}})
                save_akun_to_csv(akun)
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
        no_char = inp_no()
        if no_char == "kembali":
            return None
        if not no_char.isdigit():
            pesan_peringatan("Input harus berupa angka!", 15)
            continue
        no_char = int(no_char)
        seller_list = list({nomor: k for nomor, k in akun.items() if k["role"] == "Seller"}.keys())
        if not (1 <= no_char <= len(seller_list)):
            pesan_peringatan("Nomor akun seller tidak ditemukan!", 15)
            continue
        akun_id = seller_list[no_char - 1]
        questions = [
            inquirer.List(
                "menu",
                message="Pilih tindakan:",
                choices=[
                    "1 | Aktifkan Akun",
                    "2 | Nonaktifkan Akun",
                    "3 | Hapus Akun"])]
        pilih = inquirer.prompt(questions)["menu"]
        if pilih == "1 | Aktifkan Akun":
            akun[akun_id]["status"] = "Aktif"
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil diaktifkan!")
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "2 | Nonaktifkan Akun":
            akun[akun_id]["status"] = "Nonaktif"
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dinonaktifkan!")
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "3 | Hapus Akun":
            del akun[akun_id]
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dihapus!")
            input("→ 「 Enter untuk kembali 」")

def daftar_konsumen():
    jud_utama()
    jud_sub("Daftar Konsumen")
    global akun
    konsumen_list = {}
    for id_key, data in akun.items():
        if data["role"] == "Konsumen":
            konsumen_list[id_key] = data
    if len(konsumen_list) == 0:
        pesan_berhasil("Daftar akun konsumen belum ada.")
        return
    table = PrettyTable()
    table.field_names = ["NO", " ID ", "  USERNAME  ", " ROLE ", " STATUS ", "TERDAFTAR"]
    for idx, (id_key, user) in enumerate(konsumen_list.items(), start=1):
        table.add_row([
            idx,
            id_key,
            user["us"],
            user["role"],
            user["status"],
            user["tgl"]])
    print(table)

def stat_konsumen():
    while True:
        jud_utama()
        jud_sub("Status Konsumen")
        daftar_konsumen()
        global akun
        no_char = inp_no()
        if no_char == "kembali":
            return None
        if not no_char.isdigit():
            pesan_peringatan("Input harus berupa angka!", 15)
            continue
        no_char = int(no_char)
        konsumen_list = list({nomor: k for nomor, k in akun.items() if k["role"] == "Konsumen"}.keys())
        if not (1 <= no_char <= len(konsumen_list)):
            pesan_peringatan("Nomor akun seller tidak ditemukan!", 15)
            continue
        akun_id = konsumen_list[no_char - 1]
        questions = [
            inquirer.List(
                "menu",
                message="Pilih tindakan:",
                choices=[
                    "1 | Aktifkan Akun",
                    "2 | Nonaktifkan Akun",
                    "3 | Hapus Akun"])]
        pilih = inquirer.prompt(questions)["menu"]
        if pilih == "1 | Aktifkan Akun":
            akun[akun_id]["status"] = "Aktif"
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil diaktifkan!")
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "2 | Nonaktifkan Akun":
            akun[akun_id]["status"] = "Nonaktif"
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dinonaktifkan!")
            input("→ 「 Enter untuk kembali 」")
        elif pilih == "3 | Hapus Akun":
            del akun[akun_id]
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dihapus!")
            input("→ 「 Enter untuk kembali 」")