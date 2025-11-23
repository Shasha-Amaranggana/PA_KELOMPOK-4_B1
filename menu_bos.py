import inquirer
import re
from prettytable import PrettyTable
from datetime import datetime
from data import akun, produk_list, save_akun_to_csv
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_no, inp_enter
from colorama import Fore, Style, init
init(autoreset=True)

def tamp_bos(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ DAFTAR AKUN'.center(33), '2 │ DAFTAR PRODUK'.center(36), '3 │ LAPORAN PENJUALAN'.center(40),  '4 │ LOGOUT'.center(28)],
        "2.1" : ['1 │ MENU AKUN SELLER'.center(37), '2 │ MENU AKUN KONSUMEN'.center(39), '3 │ KEMBALI'.center(29)],
        "3.1" : ['1 │ DAFTAR AKUN SELLER'.center(39), '2 │ BUAT AKUN SELLER'.center(37), '3 │ UBAH STATUS AKUN SELLER'.center(45), '4 │ KEMBALI'.center(29)],
        "3.2" : ['1 │ DAFTAR AKUN KONSUMEN'.center(41), '2 │ UBAH STATUS AKUN KONSUMEN'.center(47), '3 │ KEMBALI'.center(29)],
        "4.1" : ['1 │ Aktifkan Akun'.center(35), '2 │ Nonaktifkan Akun'.center(37), '3 │ Hapus Akun'.center(32)]}
    choices = daftar_menu[jenis] 
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan 

# MENU BOS UTAMA
# ════════════════════════════════════════════════════
def menu_boss():
    while True:
        jud_utama()
        jud_sub("Selamat Datang Bos!")
        pilih = tamp_bos("1")
        if pilih == "1 │ DAFTAR AKUN":
            daftar_akun()
        elif pilih == "2 │ DAFTAR PRODUK":
            jud_utama()
            jud_sub("Daftar Produk")
            daftar_produk()
            print("")
            inp_enter()
        elif pilih == "3 │ LAPORAN PENJUALAN":
            jud_utama()
            jud_sub("Laporan Penjualan")
            laporan()
            print("")
            inp_enter()
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
        pesan_peringatan("Daftar produk masih kosong.", Fore.YELLOW, 12)
        return
    table = PrettyTable()
    table.field_names = ["NO", " ID ", "  VARIAN  ", "UKURAN", "HARGA", " STOK "]
    for idx, p in enumerate(produk_list, start=1):
        table.add_row([
            idx,
            p["id"],
            p["varian"],
            p["kemasan"],
            f"{p['harga']}",
            p["stok"]])
    table.align["NO", " ID ", "  VARIAN  ", "UKURAN", "HARGA", " STOK "] ="l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))
    
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
            inp_enter()
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
            inp_enter()
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
    table.align["NO", " ID ", "  USERNAME  ", " ROLE ", " STATUS ", "TERDAFTAR"] ="l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

def regist_seller():
    jud_utama()
    jud_sub("Silakan Daftarkan Seller Baru")
    print(Fore.BLUE + "  > Username min 5 karakter, mengandung huruf/angka," + Style.RESET_ALL)
    print(Fore.BLUE + "    tidak mengandung karakter spesial!" + Style.RESET_ALL)
    print(Fore.BLUE + "  > Password min 8 karakter, mengandung huruf besar & kecil & angka," + Style.RESET_ALL)
    print(Fore.BLUE + "    tidak mengandung karakter spesial!" + Style.RESET_ALL)
    print(Fore.BLUE + "  > Email harus valid dan berakhiran '@gmail.com'" + Style.RESET_ALL)
    print(Fore.BLUE + "  > No. HP harus valid dan berawalan '08'" + Style.RESET_ALL)
    print("")
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    email = input("Email: ".center(40))
    no_hp = input("No HP: ".center(40))
    alamat = input("Alamat: ".center(40))
    try:
        if username == "" or password == "" or email == "" or no_hp == "" or alamat == "":
            pesan_peringatan("Semua kolom harus diisi!", Fore.YELLOW, 12)
            inp_enter()
            return None
        if not re.search(r"^[a-zA-Z0-9]{5,}$", username):
            raise ValueError
        if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
            raise ValueError
        if not no_hp.startswith("08"):
            raise ValueError
        if not email.endswith("@gmail.com"):
            raise ValueError
        for user in akun.values():
            if user["us"] == username or user["email"] == email:
                pesan_peringatan("User atau email telah tersedia", Fore.RED, 12)
                raise ValueError
        existing_ids = [k for k in akun.keys() if k.startswith("U_S")]
        last_num = max([int(k.replace("U_S", "")) for k in existing_ids], default=0)
        new_id = f"U_S{last_num + 1}"
        akun.update({
            new_id: {
                "id": new_id,
                "us": username,
                "pw": password,
                "role": "Seller",
                "status": "Aktif",
                "tgl": datetime.now().strftime("%Y-%m-%d"),
                "email": email,
                "no_hp": no_hp,
                "alamat": alamat,
                "saldo": 0}})
        save_akun_to_csv(akun)
        pesan_berhasil(f"Akun seller berhasil dibuat! ID: {new_id}")
        inp_enter()
        return True
    except ValueError:
        pesan_peringatan("Pastikan data yang diinput sesuai syarat!", Fore.YELLOW, 12)       
        inp_enter()
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
            pesan_peringatan("Input harus berupa angka!", Fore.YELLOW, 15)
            inp_enter()
            continue
        no_char = int(no_char)
        seller_list = list({nomor: k for nomor, k in akun.items() if k["role"] == "Seller"}.keys())
        if not (1 <= no_char <= len(seller_list)):
            pesan_peringatan("Nomor akun seller tidak ditemukan!", Fore.YELLOW, 15)
            inp_enter()
            continue
        akun_id = seller_list[no_char - 1]
        pilih = tamp_bos("4.1")
        if pilih == "1 │ Aktifkan Akun":
            if akun[akun_id]["status"] == "Aktif":
                pesan_peringatan("Akun sudah dalam status Aktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status"] = "Aktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil diaktifkan!")
                inp_enter()
        elif pilih == "2 │ Nonaktifkan Akun":
            if akun[akun_id]["status"] == "Nonaktif":
                pesan_peringatan("Akun sudah dalam status Nonaktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status"] = "Nonaktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil dinonaktifkan!")
                inp_enter()
        elif pilih == "3 | Hapus Akun":
            del akun[akun_id]
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dihapus!")
            inp_enter()

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
    table.align["NO", " ID ", "  USERNAME  ", " ROLE ", " STATUS ", "TERDAFTAR"] ="l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

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
            pesan_peringatan("Input harus berupa angka!", Fore.YELLOW, 15)
            inp_enter()
            continue
        no_char = int(no_char)
        konsumen_list = list({nomor: k for nomor, k in akun.items() if k["role"] == "Konsumen"}.keys())
        if not (1 <= no_char <= len(konsumen_list)):
            pesan_peringatan("Nomor akun seller tidak ditemukan!", Fore.YELLOW, 15)
            inp_enter()
            continue
        akun_id = konsumen_list[no_char - 1]
        pilih = tamp_bos("4.1")
        if pilih == "1 │ Aktifkan Akun":
            if akun[akun_id]["status"] == "Aktif":
                pesan_peringatan("Akun sudah dalam status Aktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status"] = "Aktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil diaktifkan!")
                inp_enter()
        elif pilih == "2 │ Nonaktifkan Akun":
            if akun[akun_id]["status"] == "Nonaktif":
                pesan_peringatan("Akun sudah dalam status Nonaktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status"] = "Nonaktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil dinonaktifkan!")
                inp_enter()
        elif pilih == "3 | Hapus Akun":
            del akun[akun_id]
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dihapus!")
            inp_enter()