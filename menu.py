import re
import inquirer
from prettytable import PrettyTable
from datetime import datetime

from data import akun, produk_list, keranjang, pembelian, save_akun_to_csv, save_produk_to_csv, save_pembelian_to_csv, save_keranjang_to_csv
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_no, inp_enter

from colorama import Fore, Style, init
init(autoreset=True)



# TAMPILAN MENU
# ════════════════════════════════════════════════════
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

def tamp_sell(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ AKUN'.center(25), '2 │ PENJUALAN'.center(31), '3 │ PEMBELIAN'.center(31),  '4 │ PEMESANAN'.center(31), '5 │ LOGOUT'.center(27)],
        "2.1" : ['1 │ LIHAT DATA DIRI'.center(37), '2 │ EDIT DATA DIRI'.center(36), '3 │ KEMBALI'.center(29)],
        "2.2" : ['1 │ TAMBAH PRODUK'.center(35), '2 │ LIHAT PRODUK'.center(34), '3 │ EDIT PRODUK'.center(33), '4 │ HAPUS PRODUK'.center(34), '5 │ KEMBALI'.center(29)],
        "2.3" : ['1 │ LIHAT RINGKASAN PEMBELIAN'.center(47), '2 │ KEMBALI'.center(29)],
        "2.4" : ['1 │ LIHAT PEMESANAN'.center(37), '2 │ UBAH STATUS PESANAN'.center(42), '3 │ LIHAT STATUS PESANAN'.center(41), '4 │ KEMBALI'.center(29)]}
    choices = daftar_menu[jenis]
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan

def tamp_kons(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ AKUN'.center(25), '2 | LIHAT PRODUK'.center(33), '3 | KERANJANG BELANJA'.center(39),  '4 | PESANAN ANDA'.center(33), '5 | SALDO'.center(27), '6 | LOGOUT'.center(27)],
        "2.1" : ['1 │ LIHAT DATA DIRI'.center(37), '2 │ EDIT DATA DIRI'.center(36), '3 │ KEMBALI'.center(29)],
        "2.2" : ['1 │ TAMBAH KE KERANJANG'.center(41), '2 │ PESAN SEKARANG'.center(35), '3 │ KEMBALI'.center(29)],
        "2.3" : ['1 │ HAPUS PRODUK DARI KERANJANG'.center(50), '2 │ PESAN SEKARANG'.center(35), '3 │ KEMBALI'.center(29)],
        "2.4" : ['1 │ DIKEMAS'.center(29), '2 │ DIKIRIM'.center(29), '3 │ SELESAI'.center(29), '4 │ DIBATALKAN'.center(31), '5 │ KEMBALI'.center(29)],
        "3.2" : ['1 │ CANCEL PRODUK'.center(35), '2 │ KEMBALI'.center(29)],
        "3.3" : ['1 │ TERIMA PRODUK'.center(35), '2 │ KEMBALI'.center(29)],
        "3.1" : ['1 │ TAMBAH KE KERANJANG'.center(33), '2 │ PESAN SEKARANG'.center(33), '3 │ KEMBALI'.center(29)],
        "2.5" : ['1 │ TOP UP'.center(28), '2 │ KEMBALI'.center(29)]}
    choices = daftar_menu[jenis]
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    if not answer:
        return ""
    menu_val = answer.get('menu')
    if not menu_val:
        return ""
    return menu_val.strip()


# ════════════════════════════════════════════════════
#              MENU BOS DAN FITURNYA
# ════════════════════════════════════════════════════

# MENU BOS UTAMA
# ════════════════════════════════════════════════════
def menu_bos(current_user):
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
            laporan(current_user)
        elif pilih == "4 │ LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break

# MENU AKUN
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

def regist_seller():
    jud_utama()
    jud_sub("Daftarkan Akun Seller")
    print(Fore.BLUE + "  > Username min 5 karakter, mengandung huruf/angka," + Style.RESET_ALL)
    print(Fore.BLUE + "    tidak mengandung simbol/karakter spesial kecuali spasi/underscore" + Style.RESET_ALL)
    print(Fore.BLUE + "  > Password min 8 karakter, mengandung huruf besar & kecil & angka," + Style.RESET_ALL)
    print(Fore.BLUE + "    simbol diperbolehkan" + Style.RESET_ALL)
    print(Fore.BLUE + "  > Email harus valid dan berakhiran '@gmail.com'" + Style.RESET_ALL)
    print(Fore.BLUE + "  > No. HP harus valid, berawalan '08', min 10 angka" + Style.RESET_ALL)
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
        if not re.search(r"^[a-zA-Z0-9_ ]{5,}$", username):
            raise ValueError
        if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
            raise ValueError
        if not no_hp.startswith("08") or not re.search(r"^[0-9]{10,}$", no_hp):
            raise ValueError
        if not email.endswith("@gmail.com"):
            raise ValueError
        for user in akun.values():
            if user["us"] == username or user["email"] == email:
                pesan_peringatan("User atau email telah tersedia", Fore.RED, 12)
                raise ValueError
        existing_ids = [k for k in akun.keys() if k.startswith("U_K")]
        last_num = max([int(k.replace("U_K", "")) for k in existing_ids], default=0)
        new_id = f"U_K{last_num + 1}"
        akun.update({
            new_id: {
                "id_user": new_id,
                "us": username,
                "pw": password,
                "role": "Seller",
                "status_user": "Aktif",
                "tanggal_daftar": datetime.now().strftime("%Y-%m-%d"),
                "email": email,
                "no_hp": no_hp,
                "alamat": alamat,
                "saldo": 0}})
        save_akun_to_csv(akun)
        pesan_berhasil("Anda berhasil registrasi! Silakan login untuk melanjutkan.")
        inp_enter()
        return True
    except ValueError:
        pesan_peringatan("Pastikan data yang diinput sesuai syarat!", Fore.YELLOW, 12)       
        inp_enter()
        return None

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
            user["status_user"],
            user["tanggal_daftar"]])
    table.align["NO", " ID ", "  USERNAME  ", " ROLE ", " STATUS ", "TERDAFTAR"] ="l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

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
            if akun[akun_id]["status_user"] == "Aktif":
                pesan_peringatan("Akun sudah dalam status Aktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status_user"] = "Aktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil diaktifkan!")
                inp_enter()
        elif pilih == "2 │ Nonaktifkan Akun":
            if akun[akun_id]["status_user"] == "Nonaktif":
                pesan_peringatan("Akun sudah dalam status Nonaktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status_user"] = "Nonaktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil dinonaktifkan!")
                inp_enter()
        elif pilih == "3 | Hapus Akun":
            del akun[akun_id]
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dihapus!")
            inp_enter()


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
            user["status_user"],
            user["tanggal_daftar"]])
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
            if akun[akun_id]["status_user"] == "Aktif":
                pesan_peringatan("Akun sudah dalam status Aktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status_user"] = "Aktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil diaktifkan!")
                inp_enter()
        elif pilih == "2 │ Nonaktifkan Akun":
            if akun[akun_id]["status_user"] == "Nonaktif":
                pesan_peringatan("Akun sudah dalam status Nonaktif!", Fore.YELLOW, 15)
                inp_enter()
                continue
            else:
                akun[akun_id]["status_user"] = "Nonaktif"
                save_akun_to_csv(akun)
                pesan_berhasil("Akun berhasil dinonaktifkan!")
                inp_enter()
        elif pilih == "3 | Hapus Akun":
            del akun[akun_id]
            save_akun_to_csv(akun)
            pesan_berhasil("Akun berhasil dihapus!")
            inp_enter()

# MENU PRODUK
# ════════════════════════════════════════════════════
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
            p["id_produk"],
            p["varian"],
            p["kemasan"],
            f"{p['harga']}",
            p["stok"]])
    table.align["NO", " ID ", "  VARIAN  ", "UKURAN", "HARGA", " STOK "] ="l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

# MENU PRODUK
# ════════════════════════════════════════════════════
def laporan(current_user):
    jud_utama()
    jud_sub("Laporan Penjualan")
    hasil = transaksi_dan_omzet()
    total_transaksi = hasil[0]
    total_omzet = hasil[1]
    saldo_bos = int(current_user.get("saldo", 0))
    pesan_peringatan(f"Total Transaksi : {total_transaksi}".replace(",", "."), Fore.CYAN, 20)
    pesan_peringatan(f"Total Omzet : Rp{total_omzet}".replace(",", "."), Fore.CYAN, 20)
    pesan_peringatan(f"Saldo Anda: Rp{saldo_bos}".replace(",", "."), Fore.CYAN, 20)
    print("")
    inp_enter()

def transaksi_dan_omzet():
    semua_pesanan_selesai = []
    for id_user, daftar_pesanan in pembelian.items():
        for p in daftar_pesanan:
            p["id_user"] = id_user
        pesanan_selesai = [p for p in daftar_pesanan if p.get("status_order") == "Selesai"]
        semua_pesanan_selesai.extend(pesanan_selesai)
    total_transaksi = len(semua_pesanan_selesai)
    total_omzet = sum(p["total_harga"] for p in semua_pesanan_selesai)
    return total_transaksi, total_omzet, semua_pesanan_selesai

# ════════════════════════════════════════════════════
#              MENU SELLER DAN FITURNYA
# ════════════════════════════════════════════════════

# MENU SELLER UTAMA
# ════════════════════════════════════════════════════
def menu_seller(current_user):
    while True:
        jud_utama()
        jud_sub("Selamat Datang Seller!")
        pilih = tamp_sell("1")
        if pilih == "1 │ AKUN":
            menu_akun_s(current_user)
        elif pilih == "2 │ PENJUALAN":
            menu_penjualan()
        elif pilih == "3 │ PEMBELIAN":
            menu_pembelian()
        elif pilih == "4 │ PEMESANAN":
            menu_pemesanan()
        elif pilih == "5 │ LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break

# MENU AKUN
# ════════════════════════════════════════════════════
def menu_akun_s(current_user):
    while True:
        jud_utama()
        jud_sub("Menu Akun")
        pilih = tamp_sell("2.1")
        if pilih == "1 │ LIHAT DATA DIRI":
            jud_utama()
            jud_sub("Data Diri Anda")
            lihat_data_diri(current_user)
            print("")
            inp_enter()
        elif pilih == "2 │ EDIT DATA DIRI":
            jud_utama()
            jud_sub("Edit Data Diri Anda")
            edit_data_diri(current_user)
            inp_enter()
        elif pilih == "3 │ KEMBALI":
            break


def lihat_data_diri(current_user):
    table = PrettyTable()
    table.field_names = ["    NAMA    ", "         DATA         "]
    table.add_row(["Username", current_user.get("us")])
    table.add_row(["Password", current_user.get("pw")])
    table.add_row(["Email", current_user.get("email")])
    table.add_row(["No. HP", current_user.get("no_hp")])
    table.add_row(["Alamat", current_user.get("alamat")])
    table.align["    NAMA    "] = "l"
    table.align["         DATA         "] = "l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

def edit_data_diri(current_user):
    print(Fore.BLUE + "  > Lewati jika tidak ingin mengubah data.\n" + Style.RESET_ALL)
    pertanyaan = [
        inquirer.Text("nama", message="Username baru", default=current_user.get("us", "")),
        inquirer.Text("password", message="Password baru", default=current_user.get("pw", "")),
        inquirer.Text("email", message="Email baru", default=current_user.get("email", "")),
        inquirer.Text("no_hp", message="No. HP baru", default=current_user.get("no_hp", "")),
        inquirer.Text("alamat", message="Alamat baru", default=current_user.get("alamat", ""))]
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return

    us_val = (jawaban.get("nama") or current_user.get("us") or "").strip()
    pw_val = (jawaban.get("password") or current_user.get("pw") or "").strip()
    email_val = (jawaban.get("email") or current_user.get("email") or "").strip()
    no_hp_val = (jawaban.get("no_hp") or current_user.get("no_hp") or "").strip()
    alamat_val = (jawaban.get("alamat") or current_user.get("alamat") or "").strip()
    if not email_val.endswith("@gmail.com") or not no_hp_val.startswith("08") or not re.fullmatch(r"08\d{8,12}", no_hp_val) or not re.search(r"^[a-zA-Z0-9_ ]{5,}$", us_val) or not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", pw_val) or alamat_val == "":
        if not re.search(r"^[a-zA-Z0-9_ ]{5,}$", us_val):
            pesan_peringatan("Username min 5 char, ada huruf/angka, tidak ada char spesial!", Fore.YELLOW, 30)
        if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", pw_val):
            pesan_peringatan("Password min 8 char, ada huruf dan angka, tidak ada char spesial!", Fore.YELLOW, 30)
        if not email_val.endswith("@gmail.com"):
            pesan_peringatan("Email harus valid dan berakhiran '@gmail.com'!", Fore.YELLOW, 30)
        if not no_hp_val.startswith("08") or not re.fullmatch(r"08\d{8,12}", no_hp_val):
            pesan_peringatan("No. HP harus valid, berawalan '08', min 10 angka", Fore.YELLOW, 30)
        if alamat_val == "":
            pesan_peringatan("Alamat tidak boleh kosong!", Fore.YELLOW, 30)
        return

    current_user["us"] = jawaban["nama"] or current_user["us"]
    current_user["pw"] = jawaban["password"] or current_user["pw"]
    current_user["email"] = email_val
    current_user["no_hp"] = no_hp_val
    current_user["alamat"] = jawaban["alamat"] or current_user["alamat"]

    if "id_user" in current_user:
        akun[current_user["id_user"]] = current_user
        save_akun_to_csv(akun)
    pesan_berhasil("Data akun berhasil diubah!")

# MENU PENJUALAN (CRUD PRODUK)
# ════════════════════════════════════════════════════
def menu_penjualan():
    while True:
        jud_utama()
        jud_sub("Menu Penjualan (Produk Popcorn)")
        pilihan = tamp_sell("2.2")
        if pilihan == "1 │ TAMBAH PRODUK":
            jud_utama()
            jud_sub("Tambah Produk Popcorn")
            create_produk()
        elif pilihan == "2 │ LIHAT PRODUK":
            jud_utama()
            jud_sub("Daftar Produk")
            daftar_produk()
            print("")
            inp_enter()
        elif pilihan == "3 │ EDIT PRODUK":
            jud_utama()
            jud_sub("Edit Produk")
            update_produk()
        elif pilihan == "4 │ HAPUS PRODUK":
            jud_utama()
            jud_sub("Hapus Produk")
            delete_produk()
        elif pilihan == "5 │ KEMBALI":
            break


def create_produk():
    kemasan_map = {
        "          1 │ Small": "Small",
        "          2 │ Medium": "Medium",
        "          3 │ Large": "Large"}
    pertanyaan = [
        inquirer.Text("varian", message="Masukkan varian rasa baru"),
        inquirer.List(
            "kemasan",
            message="Masukkan ukuran kemasan",
            choices=list(kemasan_map.keys())),
        inquirer.Text("harga", message="Masukkan harga sesuai kemasan"),
        inquirer.Text("stok", message="Masukkan jumlah stok")]
    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return
    
    error_1 = []
    varian = jawaban["varian"].strip()
    if varian == "":
        error_1.append("Varian tidak boleh kosong!")
    try:
        harga = int(jawaban["harga"])
        stok = int(jawaban["stok"])
        if harga < 0:
            error_1.append("Harga tidak boleh negatif!")
        if stok < 0:
            error_1.append("Stok tidak boleh negatif!")
    except ValueError:
        error_1.append("Harga dan stok harus berupa angka!")
    if error_1:
        for err in error_1:
            pesan_peringatan(err, Fore.YELLOW, 12)
        inp_enter()
        return

    kode = varian[0].upper()
    existing_ids = [p["id_produk"] for p in produk_list if p["id_produk"].startswith(kode)]
    max_num = 0
    for pid in existing_ids:
        tail = pid[1:]
        if tail.isdigit():
            num = int(tail)
            if num > max_num:
                max_num = num
    new_id = f"{kode}{max_num + 1}"

    produk_baru = {
        "id_produk": new_id,
        "varian": varian,
        "kemasan": kemasan_map[jawaban["kemasan"]],
        "harga": harga,
        "stok": jawaban["stok"]}

    produk_list.append(produk_baru)
    save_produk_to_csv(produk_list)
    pesan_berhasil(f"Produk berhasil ditambahkan dengan ID {new_id}")
    inp_enter()

def update_produk():
    global produk_list
    if len(produk_list) == 0:
        pesan_peringatan("Daftar produk masih kosong.", Fore.YELLOW, 12)
        inp_enter()
        return
    pilihan_id = [
        inquirer.List(
            "produk",
            message="Pilih produk yang akan diubah",
            choices=[f"{p['id_produk']} │ {p['varian']} ({p['kemasan']})" for p in produk_list])]
    jawaban = inquirer.prompt(pilihan_id)
    if jawaban is None:
        return
    teks = jawaban["produk"]
    id_terpilih = teks.split(" │ ")[0].strip()
    produk = next((p for p in produk_list if p["id_produk"] == id_terpilih), None)

    if not produk:
        pesan_peringatan("Produk tidak ditemukan!", Fore.RED, 12)       
        inp_enter()
        return
    
    print(("═"*50).center(70))
    print("")
    table = PrettyTable()
    table.field_names = ["    NAMA    ", "         DATA         "]
    table.add_row(["ID", produk["id_produk"]])
    table.add_row(["Varian", produk["varian"]])
    table.add_row(["Kemasan", produk["kemasan"]])
    table.add_row(["Harga", f"Rp{produk['harga']}"])
    table.add_row(["stok", produk["stok"]])
    table.align["    NAMA    "] = "l"
    table.align["         DATA         "] = "l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))
    print("")
    print(("═"*50).center(70))

    print(Fore.BLUE + "  > Lewati jika tidak ingin mengubah data.\n" + Style.RESET_ALL)
    kemasan_map = {
        "          1 │ Small": "Small",
        "          2 │ Medium": "Medium",
        "          3 │ Large": "Large"}
    pertanyaan = [
        inquirer.Text("varian", message="Varian baru", default=produk["varian"]),
        inquirer.List("kemasan", message="Ukuran kemasan baru", choices=list(kemasan_map.keys()), default=produk["kemasan"]),
        inquirer.Text("harga", message="Harga baru", default=str(produk["harga"])),
        inquirer.Text("stok", message="Stok baru", default=str(produk["stok"]))]

    jawab_update = inquirer.prompt(pertanyaan)
    if jawab_update is None:
        return

    if jawab_update["harga"] or jawab_update["stok"]:
        try:
            produk["varian"] = jawab_update["varian"] or produk["varian"]
            produk["kemasan"] = kemasan_map[jawab_update["kemasan"]] or produk["kemasan"]
            if jawab_update["harga"]:
                harga_baru = int(jawab_update["harga"])
                if harga_baru < 0:
                    raise ValueError("Harga tidak boleh negatif")
                produk["harga"] = harga_baru
            if jawab_update["stok"]:
                stok_baru = int(jawab_update["stok"])
                if stok_baru < 0:
                    raise ValueError("Stok tidak boleh negatif")
                produk["stok"] = stok_baru
            save_produk_to_csv(produk_list)
            pesan_berhasil("Data produk berhasil diubah!")
        except ValueError:
            pesan_peringatan("Harga dan stok baru tidak valid! Harga dan stok lama dipertahankan.", Fore.YELLOW, 30)       
    inp_enter()

def delete_produk():
    global produk_list
    if len(produk_list) == 0:
        pesan_peringatan("Daftar produk masih kosong.", Fore.YELLOW, 12)
        input("→ 「 Enter untuk kembali 」")
        return
    pilihan_id = [
        inquirer.List(
            "produk",
            message="Pilih produk yang akan dihapus",
            choices=[f"{p['id_produk']} │ {p['varian']} ({p['kemasan']})" for p in produk_list])]
    jawaban = inquirer.prompt(pilihan_id)
    if jawaban is None:
        return
    teks = jawaban["produk"]
    id_terpilih = teks.split(" │ ")[0].strip()
    produk = next((p for p in produk_list if p["id_produk"] == id_terpilih), None)

    if not produk:
        pesan_peringatan("Produk tidak ditemukan!", Fore.RED, 12)       
        input("→「 Enter untuk kembali 」")
        return
    print("")
    print(("═"*50).center(70))
    print("")
    konfirmasi = [
        inquirer.List(
            "konfirm",
            message=f"Konfirmasi ingin menghapus produk {produk['varian']} ({produk['kemasan']})",
            choices=["            1 │ Ya", "            2 │ Tidak"])]
    jawab_konfirmasi = inquirer.prompt(konfirmasi)
    if jawab_konfirmasi and jawab_konfirmasi["konfirm"] == "            1 │ Ya":
        produk_list.remove(produk)
        save_produk_to_csv(produk_list)
        pesan_berhasil("Produk berhasil dihapus!")
    else:
        pesan_peringatan("Produk batal dihapus!", Fore.RED, 12)
    inp_enter()

# MENU PEMBELIAN
# ════════════════════════════════════════════════════
def menu_pembelian():
    jud_utama()
    jud_sub("Ringkasan Pembelian")
    semua_pesanan_selesai = []
    for id_user, daftar_pesanan in pembelian.items():
        for p in daftar_pesanan:
            p["id_user"] = id_user
        pesanan_selesai = [p for p in daftar_pesanan if p.get("status_order") == "Selesai"]
        semua_pesanan_selesai.extend(pesanan_selesai)

    if not semua_pesanan_selesai:
        pesan_peringatan("Daftar pembelian masih kosong.", Fore.YELLOW, 12)
        print("")
        inp_enter()
        return None

    hasil = transaksi_dan_omzet()
    total_transaksi = hasil[0]
    total_omzet = hasil[1]
    semua_pesanan_selesai = hasil[2]
    if total_transaksi == 0:
        pesan_peringatan("Daftar pembelian masih kosong.", Fore.YELLOW, 12)
        print("")
        inp_enter()
        return None
    print(f"Total Transaksi : {total_transaksi}")
    print(f"Total Omzet     : Rp{total_omzet}")
    print("-" * 30)

    table = PrettyTable()
    table.field_names = ["ID USER", "ID ORDER", "VARIAN", "KEMASAN", "JUMLAH", "TOTAL HARGA", "TANGGAL"]
    for item in semua_pesanan_selesai:
        table.add_row([
            item.get("id_user"),
            item.get("id_order"),
            item.get("varian"),
            item.get("kemasan"),
            item.get("jumlah"),
            f"Rp{int(item.get('total_harga', 0)):,}",
            item.get("tanggal_pesan")])
        table.align["ID"] = "c"
        table.align["Nama User"] = "l"
        table.align["Total Harga"] = "r"
        table.align["Status"] = "c"

        table_str = table.get_string()
        for line in table_str.split("\n"):
            print(line.center(70))
    print("")
    inp_enter()

# MENU PEMESANAN
# ════════════════════════════════════════════════════
def menu_pemesanan():
    while True:
        jud_utama()
        jud_sub("Menu Pemesanan")
        pilihan = tamp_sell("2.4")
        if pilihan == "1 │ LIHAT PEMESANAN":
            jud_utama()
            jud_sub("Daftar Pesanan Baru")
            lihat_pemesanan()
            print("")
            inp_enter()
        elif pilihan == "2 │ UBAH STATUS PESANAN":
            jud_utama()
            jud_sub("Ubah Status Pesanan")
            ubah_status_pesanan()
        elif pilihan == "3 │ LIHAT STATUS PESANAN":
            jud_utama()
            jud_sub("Lihat Status Pemesanan Terkini")
            lihat_status_pesanan()
            print("")
            inp_enter()
        elif pilihan == "4 │ KEMBALI":
            break


def lihat_pemesanan():
    pesanan_dipesan = []
    for id_user, daftar_pesanan in pembelian.items():
        for p in daftar_pesanan:
            if p.get("status_order") == "Dipesan":
                p["id_user"] = id_user
                pesanan_dipesan.append(p)

    if not pesanan_dipesan:
        pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
        return None
    
    table = PrettyTable()
    table.field_names = ["ID", "ID U", "ID P", "VARIAN", "KEMASAN", "JML", "TOTAL HARGA", "TGL PESAN"]
    for p in pesanan_dipesan:
        table.add_row([
            p.get("id_order"),
            p["id_user"],
            p.get("id_produk"),
            p.get("varian"),
            p.get("kemasan"),
            p.get("jumlah"),
            f"Rp{p.get('total_harga')}",
            p.get("tanggal_pesan")])

    for field in table.field_names:
        table.align[field] = "l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

    return True 

def ubah_status_pesanan():
    while True:
        jud_utama()
        jud_sub("Ubah Status Pesanan")

        pesanan_awal = []
        for id_user, daftar_pesanan in pembelian.items():
            for p in daftar_pesanan:
                if p.get("status_order") == "Dipesan":
                    p["id_user"] = id_user
                    pesanan_awal.append(p)

        if not pesanan_awal:
            pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
            print("")
            inp_enter()
            return None
        
        pilihan_id = [
            inquirer.List(
                "pesanan",
                message="Pilih pesanan yang mau statusnya diubah",
                choices=[f"{p['id_order']} │ {p['varian']} ({p['kemasan']}) │ {p['id_user']}" for p in pesanan_awal])]
        jawaban = inquirer.prompt(pilihan_id)
        if jawaban is None:
            return
        teks = jawaban["pesanan"]
        id_terpilih = teks.split(" │ ")[0].strip()

        produk = next((p for p in pesanan_awal if p["id_order"] == id_terpilih), None)
        if not produk:
            pesan_peringatan("Pesanan tidak ditemukan!", Fore.RED, 12)       
            inp_enter()
            return

        print(("═"*50).center(70))
        print("")
        table = PrettyTable()
        table.field_names = ["    NAMA    ", "         DATA         "]
        table.add_row(["ID Order", produk["id_order"]])
        table.add_row(["ID User", produk["id_user"]])
        table.add_row(["ID Produk", produk["id_produk"]])
        table.add_row(["Varian", produk["varian"]])
        table.add_row(["Kemasan", produk["kemasan"]])
        table.add_row(["Tanggal Dipesan", produk["tanggal_pesan"]])
        table.add_row(["Jumlah", produk["jumlah"]])
        table.add_row(["Total Harga", f"Rp{produk['total_harga']}"])
        table.align["    NAMA    "] = "l"
        table.align["         DATA         "] = "l"
        table_str = table.get_string()
        for line in table_str.split("\n"):
            print(line.center(70))
        print("")
        print(("═"*50).center(70))

        aksi = [
            inquirer.List(
                "aksi",
                message=f"Ingin melakukan apa pada {produk['id_order']} ini?",
                choices=["            1 │ Kirim Produk", "            2 │ Cancel Pesanan", "            3 │ Kembali"])]
        jawaban_aksi = inquirer.prompt(aksi)
        if not jawaban_aksi:
            return

        if jawaban_aksi["aksi"] == "            1 │ Kirim Produk" or jawaban_aksi["aksi"] == "            2 │ Cancel Pesanan":
            konfirmasi = [
                inquirer.List(
                    "konfirm",
                    message=f"Konfirmasi ingin melakukan hal tersebut?",
                    choices=["            1 │ Ya", "            2 │ Tidak"])]
            jawab_konfirmasi = inquirer.prompt(konfirmasi)
            if not jawab_konfirmasi:
                return
        
            if jawab_konfirmasi["konfirm"] == "            1 │ Ya":

                if jawaban_aksi["aksi"] == "            1 │ Kirim Produk":
                    produk["status_order"] = "Dikirim"
                    produk["tanggal_dikirim"] = datetime.now().strftime("%Y-%m-%d")
                    save_pembelian_to_csv(pembelian)
                    pesan_berhasil("Pesanan berhasil dikirim!")
                    inp_enter()
                    return
                elif jawaban_aksi["aksi"] == "            2 │ Cancel Pesanan":
                    alasan = input("╰┈➤ Masukkan alasan pembatalan: ").strip()
                    produk["status_order"] = "Dibatalkan"
                    produk["alasan"] = alasan
                    produk["batal_oleh"] = "Seller"
                    master = next((p for p in produk_list if p["id_produk"] == produk["id_produk"]), None)
                    if master:
                        master["stok"] = int(master["stok"]) + int(produk["jumlah"])
                        save_produk_to_csv(produk_list)
                    
                    kembalikan_saldo = True
                    if kembalikan_saldo:
                        saldo_back = int(produk["total_harga"] * 75/100)
                        id_user_pesan = produk["id_user"]
                        user_yang_pesan = akun.get(id_user_pesan)
                        if user_yang_pesan:
                            user_yang_pesan["saldo"] = int(user_yang_pesan.get("saldo", 0)) + saldo_back
                        user_bos = None
                        for id_user, user in akun.items():
                            if user.get("role") == "Bos":
                                user_bos = id_user
                                break
                        if user_bos:
                            akun[user_bos]["saldo"] = max(0, int(akun[user_bos].get("saldo", 0)) - saldo_back)
                            save_akun_to_csv(akun)
                            pesan_berhasil(f"Saldo pembelian sebesar Rp{saldo_back:,} telah dikembalikan ke akun yang bersangkutan!")
                        save_pembelian_to_csv(pembelian)
                    pesan_berhasil("Produk berhasil dibatalkan!")
                    inp_enter()
                    return
            elif jawab_konfirmasi["konfirm"] == "            2 │ Tidak":
                pesan_peringatan("Produk batal untuk diubah statusnya!", Fore.RED, 12)
                inp_enter()
                return
        else:
            return

def lihat_status_pesanan():
    global pesanan_NoDipesan
    pesanan_NoDipesan = []

    for id_user, daftar_pesanan in pembelian.items():
        for p in daftar_pesanan:
            if p.get("status_order") == "Dikirim" or p.get("status_order") == "Dibatalkan":
                p["id_user"] = id_user
                pesanan_NoDipesan.append(p)

    if not pesanan_NoDipesan:
        pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
        return None
    
    table = PrettyTable()
    table.field_names = ["ID", "ID U", "ID P", "VARIAN", "KEMASAN", "JML", "TOTAL HARGA", "STATUS", "TGL PESAN"]
    for p in pesanan_NoDipesan:
        table.add_row([
            p.get("id_order"),
            p["id_user"],
            p.get("id_produk"),
            p.get("varian"),
            p.get("kemasan"),
            p.get("jumlah"),
            f"Rp{p.get('total_harga')}",
            p.get("status_order"),
            p.get("tanggal_pesan")])

    for field in table.field_names:
        table.align[field] = "l"
    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

    return True 



# ════════════════════════════════════════════════════
#              MENU KONSUMEN DAN FITURNYA
# ════════════════════════════════════════════════════

# MENU KONSUMEN UTAMA
# ════════════════════════════════════════════════════
def menu_konsumen(current_user):
    while True:
        jud_utama()
        jud_sub(f"Selamat Datang!")
        pilih = tamp_kons("1")
        if pilih == "1 │ AKUN":
            menu_akun_k(current_user)
        elif pilih == "2 | LIHAT PRODUK":
            jud_utama()
            jud_sub("Daftar Produk")
            lihat_produk(current_user)
        elif pilih == "3 | KERANJANG BELANJA":
            jud_utama()
            jud_sub("Keranjang Belanja")
            keranjang_belanja(current_user)
        elif pilih == "4 | PESANAN ANDA":
            jud_utama()
            jud_sub("Pesanan Anda")
            pesanan_anda(current_user)
        elif pilih == "5 | SALDO":
            saldo(current_user)
        elif pilih == "6 | LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break

# MENU AKUN
# ════════════════════════════════════════════════════
def menu_akun_k(current_user):
    while True:
        jud_utama()
        jud_sub("Menu Akun")
        pilih = tamp_kons("2.1")
        if pilih == "1 │ LIHAT DATA DIRI":
            jud_utama()
            jud_sub("Data Diri Konsumen")
            lihat_data_diri(current_user)
            print("")
            inp_enter()
        elif pilih == "2 │ EDIT DATA DIRI":
            jud_utama()
            jud_sub("Edit Data Diri Konsumen")
            edit_data_diri(current_user)
            inp_enter()
        elif pilih == "3 │ KEMBALI":
            break

# MENU LIHAT PRODUK
# ════════════════════════════════════════════════════
def lihat_produk(current_user):
    while True:
        jud_utama()
        jud_sub("Daftar Produk")
        daftar_produk()  
        print("")
        print(("═"*50).center(70))
        pilih = tamp_kons("2.2")
        if pilih == "1 │ TAMBAH KE KERANJANG":
            tambah_keranjang(current_user)
        elif pilih == "2 │ PESAN SEKARANG":
            pesan(current_user)
        elif pilih == "3 │ KEMBALI":
            break

def tambah_keranjang(current_user):
    id_user = current_user.get("id_user", "")
    user_items = keranjang.get(id_user, [])
    if not id_user:
        pesan_peringatan("Akun tidak valid (tidak memiliki ID). Silakan login ulang.", Fore.YELLOW, 20)
        return
    while True:
        jud_utama()
        jud_sub("Tambah ke Keranjang")
        pilihan_id = [
            inquirer.List(
                "produk",
                message="Pilih produk yang akan ditambahkan",
                choices=[f"{p['id_produk']} │ {p['varian']} ({p['kemasan']}) │ Rp{p['harga']}" for p in produk_list])]
        jawaban = inquirer.prompt(pilihan_id)
        if jawaban is None:
            return
        teks = jawaban["produk"]
        id_terpilih = teks.split(" │ ")[0].strip()

        produk = next((p for p in produk_list if p["id_produk"] == id_terpilih), None)
        if not produk:
            pesan_peringatan("Produk tidak ditemukan!", Fore.RED, 12)       
            inp_enter()
            return
        if int(produk["stok"]) <= 0:
            pesan_peringatan("Stok produk telah habis! Tidak dapat dimasukkan ke keranjang.", Fore.RED, 12)
            inp_enter()
            return

        print(("═"*50).center(70))
        print("")
        table = PrettyTable()
        table.field_names = ["    NAMA    ", "         DATA         "]
        table.add_row(["ID", produk["id_produk"]])
        table.add_row(["Varian", produk["varian"]])
        table.add_row(["Kemasan", produk["kemasan"]])
        table.add_row(["Harga", f"Rp{produk['harga']}"])
        table.add_row(["Stok", produk["stok"]])
        table.align["    NAMA    "] = "l"
        table.align["         DATA         "] = "l"
        table_str = table.get_string()
        for line in table_str.split("\n"):
            print(line.center(70))
        print("")
        print(("═"*50).center(70))

        konfirmasi = [
            inquirer.List(
                "konfirm",
                message=f"Konfirmasi ingin memasukkan {produk['varian']} ({produk['kemasan']}) ke keranjang?",
                choices=["            1 │ Ya", "            2 │ Tidak"])]
        jawab_konfirmasi = inquirer.prompt(konfirmasi)
        if not jawab_konfirmasi:
            return
        if jawab_konfirmasi["konfirm"] == "            1 │ Ya":
            existing = next((item for item in user_items if item["id_produk"] == id_terpilih), None)
            if existing:
                pesan_peringatan("Produk sudah ada di keranjang anda!", Fore.YELLOW, 12)
                inp_enter()
                return

            user_items.append({
                "id_user":id_user,
                "id_produk": produk["id_produk"],
                "varian": produk["varian"],
                "kemasan": produk["kemasan"],
                "harga": int(produk["harga"])})

            keranjang[id_user] = user_items
            save_keranjang_to_csv(keranjang)
            pesan_berhasil("Produk berhasil ditambahkan ke keranjang anda!")
            inp_enter()
            return

        else:
            pesan_peringatan("Produk batal dimasukkan!", Fore.RED, 12)
            inp_enter()
            return

def pesan(current_user, source_list=None):
    id_user = current_user.get("id_user", "")
    saldo_user = int(current_user.get("saldo", 0))

    if source_list is None:
        source_list = produk_list

    while True:
        jud_utama()
        jud_sub("Pesan Produk")
        pilihan_id = [
            inquirer.List(
                "produk",
                message="Pilih produk yang akan dipesan",
                choices=[f"{p['id_produk']} │ {p['varian']} ({p['kemasan']}) │ Rp{p['harga']}" for p in source_list])]
        jawaban = inquirer.prompt(pilihan_id)
        if not jawaban:
            return

        teks = jawaban["produk"]
        id_terpilih = teks.split(" │ ")[0].strip()
        produk = next((p for p in source_list if p["id_produk"] == id_terpilih), None)
        if not produk:
            pesan_peringatan("Produk tidak ditemukan!", Fore.RED, 12)
            inp_enter()
            return
        master = next((p for p in produk_list if (p.get("id_produk") == id_terpilih or p.get("id") == id_terpilih)), None)
        stok_master = int(master.get("stok", 0))
        harga_master = int(master.get("harga", 0))
        varian = produk.get("varian", master.get("varian", ""))
        kemasan = produk.get("kemasan", master.get("kemasan", ""))

        if stok_master <= 0:
            pesan_peringatan("Stok produk telah habis! Tidak dapat dipesan", Fore.RED, 12)
            inp_enter()
            return

        print(("═"*50).center(70))
        print("")
        table = PrettyTable()
        table.field_names = ["    NAMA    ", "         DATA         "]
        table.add_row(["ID", produk["id_produk"]])
        table.add_row(["Varian", varian])
        table.add_row(["Kemasan", kemasan])
        table.add_row(["Harga", f"Rp{harga_master}"])
        table.add_row(["Stok", stok_master])
        table.align["    NAMA    "] = "l"
        table.align["         DATA         "] = "l"
        table_str = table.get_string()
        for line in table_str.split("\n"):
            print(line.center(70))
        print("")
        print(("═"*50).center(70))

        konfirmasi = [
            inquirer.List(
                "konfirm",
                message=f"Konfirmasi ingin memesan {produk['varian']} ({produk['kemasan']})?",
                choices=["            1 │ Ya", "            2 │ Tidak"])]
        jawab_konfirmasi = inquirer.prompt(konfirmasi)
        if not jawab_konfirmasi:
            return
        if jawab_konfirmasi["konfirm"] == "            1 │ Ya":
            inp = input("Masukkan jumlah produk yang ingin dipesan (ketik 'kembali' untuk kembali): ").strip()
            if inp == "kembali":
                return None
            try:
                jumlah = int(inp)
                if jumlah == 0 or jumlah < 0:
                    pesan_peringatan("Jumlah produk tidak boleh nol atau negatif!", Fore.YELLOW, 20)
                    inp_enter()
                    continue
                elif jumlah > stok_master:
                    pesan_peringatan("Jumlah produk melebihi stok yang tersedia!", Fore.YELLOW, 30)
                    inp_enter()
                    continue
                else:
                    total_harga = harga_master * jumlah
                    if saldo_user < total_harga:
                        pesan_peringatan("Saldo anda tidak mencukupi untuk membeli produk ini!", Fore.RED, 12)
                        inp_enter()
                        return
            except ValueError:
                pesan_peringatan("Input tidak valid! Silakan masukkan angka.", Fore.YELLOW, 30)
                inp_enter()
                continue

            produk_ids = []
            for daftar in pembelian.values():
                for order in daftar:
                    produk_ids.append(order.get("id_order", ""))
            last_num = max([int(k.replace("O", "")) for k in produk_ids if k.startswith("O")], default=0)
            id_order = f"O{last_num + 1}"

            if id_user not in pembelian:
                pembelian[id_user] = []

            pembelian[id_user].append({
                "id_order": id_order,
                "id_produk": produk["id_produk"],
                "varian": varian,
                "kemasan": kemasan,
                "harga": harga_master,
                "id_user": id_user,
                "tanggal_pesan": datetime.now().strftime("%Y-%m-%d"),
                "tanggal_dikirim": "",
                "tanggal_sampai": "",
                "jumlah": jumlah,
                "total_harga": total_harga,
                "status_order": "Dipesan",
                "batal_oleh": "",
                "alasan": ""})

            current_user["saldo"] = saldo_user - total_harga
            for user_data in akun.values():
                if user_data.get("role") == "Bos":
                    user_data["saldo"] = int(user_data.get("saldo", 0)) + total_harga
                    break
            master["stok"] = stok_master - jumlah
            if master["stok"] < 0:
                master["stok"] = 0

            if source_list is not produk_list:
                if id_user in keranjang and produk in keranjang[id_user]:
                    keranjang[id_user].remove(produk)
                    if not keranjang[id_user]:
                        del keranjang[id_user]
                    save_keranjang_to_csv(keranjang)
            save_akun_to_csv(akun)
            save_pembelian_to_csv(pembelian)
            save_produk_to_csv(produk_list)
            pesan_berhasil("Produk berhasil dipesan!")
            inp_enter()
            return

        else:
            pesan_peringatan("Produk batal dipesan!", Fore.RED, 12)
            inp_enter()
            return


# MENU KERANJANG BELANJA
# ════════════════════════════════════════════════════
def keranjang_belanja(current_user):
    while True:
        jud_utama()
        jud_sub("Keranjang Belanja")
        if daftar_keranjang(current_user) is None:
            inp_enter()
            return
        else:
            print("")
            print(("═"*50).center(70))
            pilih = tamp_kons("2.3")
            if pilih == "1 │ HAPUS PRODUK DARI KERANJANG":
                hapus_keranjang(current_user)
            elif pilih == "2 │ PESAN SEKARANG":
                id_user = current_user.get("id_user", "")
                user_keranjang = keranjang.get(id_user, [])
                if user_keranjang:
                    pesan(current_user, user_keranjang)
            elif pilih == "3 │ KEMBALI":
                break

def daftar_keranjang(current_user):
    id_user = current_user.get("id_user", "")
    user_items = keranjang.get(id_user, [])

    if not user_items:
        pesan_peringatan("Daftar keranjang masih kosong.", Fore.YELLOW, 12)
        print("")
        return None
    
    table = PrettyTable()
    table.field_names = ["NO", "ID", "VARIAN", "UKURAN", "HARGA"]
    for idx, item in enumerate(user_items, start=1):
        harga = int(item.get("harga", 0))
        table.add_row([
            idx,
            item.get("id_produk"),
            item.get("varian"),
            item.get("kemasan"),
            f"Rp{harga:,}"])

    table.align["NO"] = "l"
    table.align["ID"] = "l"
    table.align["VARIAN"] = "l"
    table.align["UKURAN"] = "l"
    table.align["HARGA"] = "r"

    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

    return True 

def hapus_keranjang(current_user):
    id_user = current_user.get("id_user", "")
    user_items = keranjang.get(id_user, [])
    while True:
        jud_utama()
        jud_sub("Hapus Produk Dari Keranjang")
        pilihan_id = [
            inquirer.List(
                "keranjang",
                message="Pilih produk yang mau dihapus",
                choices=[f"{p['id_produk']} │ {p['varian']} ({p['kemasan']}) │ {p['harga']}" for p in user_items])]
        jawaban = inquirer.prompt(pilihan_id)
        if jawaban is None:
            return
        teks = jawaban["keranjang"]
        id_terpilih = teks.split(" │ ")[0].strip()

        produk = next((p for p in user_items if p["id_produk"] == id_terpilih), None)
        if not produk:
            pesan_peringatan("Produk tidak ditemukan!", Fore.RED, 12)       
            inp_enter()
            return

        print(("═"*50).center(70))
        print("")
        table = PrettyTable()
        table.field_names = ["    NAMA    ", "         DATA         "]
        table.add_row(["ID", produk["id_produk"]])
        table.add_row(["Varian", produk["varian"]])
        table.add_row(["Kemasan", produk["kemasan"]])
        table.add_row(["Harga", f"Rp{produk['harga']}"])
        table.align["    NAMA    "] = "l"
        table.align["         DATA         "] = "l"
        table_str = table.get_string()
        for line in table_str.split("\n"):
            print(line.center(70))
        print("")
        print(("═"*50).center(70))

        konfirmasi = [
            inquirer.List(
                "konfirm",
                message=f"Konfirmasi ingin menghapus {produk['varian']} ({produk['kemasan']}) dari keranjang?",
                choices=["            1 │ Ya", "            2 │ Tidak"])]
        jawab_konfirmasi = inquirer.prompt(konfirmasi)
        if not jawab_konfirmasi:
            return
        if jawab_konfirmasi["konfirm"] == "            1 │ Ya":
            user_items.remove(produk)
            if user_items:
                keranjang[id_user] = user_items
            else:
                if id_user in keranjang:
                    del keranjang[id_user]
            save_keranjang_to_csv(keranjang)
            pesan_berhasil("Produk berhasil dihapus dari keranjang anda!")
            inp_enter()
            return
        else:
            pesan_peringatan("Produk batal dihapus!", Fore.RED, 12)
            inp_enter()
            return


# MENU PESANAN
# ════════════════════════════════════════════════════
def pesanan_anda(current_user):
    while True:
        jud_utama()
        jud_sub("Daftar Pesanan Anda")
        pilih = tamp_kons("2.4")
        if pilih == "1 │ DIKEMAS":
            produk_dikemas(current_user)
        elif pilih == "2 │ DIKIRIM":
            produk_dikirim(current_user)
        elif pilih == "3 │ SELESAI":
            jud_utama()
            jud_sub("Pesanan Selesai")
            produk_selesai(current_user)
            print("")
            inp_enter()
        elif pilih == "4 │ DIBATALKAN":
            jud_utama()
            jud_sub("Pesanan Dibatalkan")
            produk_dibatalkan(current_user)
            print("")
            inp_enter()
        elif pilih == "5 │ KEMBALI":
            break


def produk_dikemas(current_user):
    while True:
        jud_utama()
        jud_sub("Daftar Pesanan Dikemas Anda")
        if daftar_dikemas(current_user) is None:
            inp_enter()
            return
        else:
            print("")
            print(("═"*50).center(70))
            pilih = tamp_kons("3.2")
            if pilih == "1 │ CANCEL PRODUK":
                cancel_produk(current_user)
            elif pilih == "2 │ KEMBALI":
                break

def daftar_dikemas(current_user):
    jud_utama()
    jud_sub("Pesanan Dikemas")
    id_user = current_user.get("id_user", "")
    user_pembelian = pembelian.get(id_user, [])
    p_dikemas = [p for p in user_pembelian if p.get("status_order") == "Dipesan"]

    if not p_dikemas:
        pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
        print("")
        return None
    
    table = PrettyTable()
    table.field_names = ["ID", "VARIAN", "UKURAN", "TGL PESAN", "JUMLAH", "TOTAL HARGA"]
    for idx, item in enumerate(p_dikemas, start=1):
        harga = int(item.get("total_harga", 0))
        table.add_row([
            item.get("id_order"),
            item.get("varian"),
            item.get("kemasan"),
            item.get("tanggal_pesan"),
            item.get("jumlah"),
            f"Rp{harga:,}"])

    table.align["ID"] = "l"
    table.align["VARIAN"] = "l"
    table.align["UKURAN"] = "l"
    table.align["TGL PESAN"] = "l"
    table.align["JUMLAH"] = "r"
    table.align["TOTAL HARGA"] = "r"

    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

    return True 

def cancel_produk(current_user):
    id_user = current_user.get("id_user", "")
    user_pembelian = pembelian.get(id_user, [])
    while True:
        jud_utama()
        jud_sub("Cancel Pesanan")
        pesanan_aktif = [
            p for p in pembelian[id_user]
            if p["status_order"] == "Dipesan"]
        if not pesanan_aktif:
            pesan_peringatan("Tidak ada pesanan yang dapat dibatalkan.", Fore.YELLOW, 20)
            inp_enter()
            return
        pilihan_id = [
            inquirer.List(
                "pesanan",
                message="Pilih produk yang mau dibatalkan",
                choices=[f"{p['id_order']} │ {p['varian']} ({p['kemasan']}) │ {p['total_harga']}" for p in pesanan_aktif])]
        jawaban = inquirer.prompt(pilihan_id)
        if jawaban is None:
            return
        teks = jawaban["pesanan"]
        id_terpilih = teks.split(" │ ")[0].strip()

        produk = next((p for p in pesanan_aktif if p["id_order"] == id_terpilih), None)
        if not produk:
            pesan_peringatan("Pesanan tidak ditemukan!", Fore.RED, 12)       
            inp_enter()
            return

        print(("═"*50).center(70))
        print("")
        table = PrettyTable()
        table.field_names = ["    NAMA    ", "         DATA         "]
        table.add_row(["ID Order", produk["id_order"]])
        table.add_row(["Varian", produk["varian"]])
        table.add_row(["Kemasan", produk["kemasan"]])
        table.add_row(["Tanggal Dipesan", produk["tanggal_pesan"]])
        table.add_row(["Jumlah", produk["jumlah"]])
        table.add_row(["Total Harga", f"Rp{produk['total_harga']}"])
        table.align["    NAMA    "] = "l"
        table.align["         DATA         "] = "l"
        table_str = table.get_string()
        for line in table_str.split("\n"):
            print(line.center(70))
        print("")
        print(("═"*50).center(70))

        alasan = input("╰┈➤ Masukkan alasan pembatalan: ").strip()
        print("")

        konfirmasi = [
            inquirer.List(
                "konfirm",
                message=f"Konfirmasi ingin membatalkan pesanan {produk['varian']} ({produk['kemasan']})?",
                choices=["            1 │ Ya", "            2 │ Tidak"])]
        jawab_konfirmasi = inquirer.prompt(konfirmasi)
        if not jawab_konfirmasi:
            return
        
        if jawab_konfirmasi["konfirm"] == "            1 │ Ya":
            produk["status_order"] = "Dibatalkan"
            produk["tanggal_dikirim"] = ""
            produk["tanggal_sampai"] = ""
            produk["batal_oleh"] = current_user.get("us", "")
            produk["alasan"] = alasan
            master = next((p for p in produk_list if p["id_produk"] == produk["id_produk"]), None)
            if master:
                master["stok"] = int(master["stok"]) + int(produk["jumlah"])
                save_produk_to_csv(produk_list)

            kembalikan_saldo = True
            if kembalikan_saldo:
                saldo_back = int(produk["total_harga"] * 50/100)
                current_user["saldo"] = int(current_user.get("saldo", 0)) + saldo_back
                user_bos = None
                for id_user, user in akun.items():
                    if user.get("role") == "Bos":
                        user_bos = id_user
                        break
                if user_bos:
                    akun[user_bos]["saldo"] = max(0, int(akun[user_bos].get("saldo", 0)) - saldo_back)
                pesan_berhasil(f"Saldo pembelian sebesar Rp{saldo_back:,} telah dikembalikan ke akun anda")
                save_akun_to_csv(akun)

            save_pembelian_to_csv(pembelian)
            pesan_berhasil("Produk berhasil dibatalkan!")
            inp_enter()
            return
        else:
            pesan_peringatan("Produk batal dibatalkan!", Fore.RED, 12)
            inp_enter()
            return


def produk_dikirim(current_user):
    while True:
        jud_utama()
        jud_sub("Daftar Pesanan Dikirim Anda")
        if daftar_dikirim(current_user) is None:
            inp_enter()
            return
        else:
            print("")
            print(("═"*50).center(70))
            pilih = tamp_kons("3.3")
            if pilih == "1 │ TERIMA PRODUK":
                terima_produk(current_user)
            elif pilih == "2 │ KEMBALI":
                break

def daftar_dikirim(current_user):
    jud_utama()
    jud_sub("Pesanan Dikirim")
    id_user = current_user.get("id_user", "")
    user_pembelian = pembelian.get(id_user, [])
    p_dikirim = [p for p in user_pembelian if p.get("status_order") == "Dikirim"]

    if not p_dikirim:
        pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
        print("")
        return None
    
    table = PrettyTable()
    table.field_names = ["ID", "VARIAN", "UKURAN", "TGL PESAN", "TGL KIRIM", "JUMLAH", "TOTAL HARGA"]
    for idx, item in enumerate(p_dikirim, start=1):
        harga = int(item.get("total_harga", 0))
        table.add_row([
            item.get("id_order"),
            item.get("varian"),
            item.get("kemasan"),
            item.get("tanggal_pesan"),
            item.get("tanggal_dikirim"),
            item.get("jumlah"),
            f"Rp{harga:,}"])

    table.align["ID"] = "l"
    table.align["VARIAN"] = "l"
    table.align["UKURAN"] = "l"
    table.align["TGL PESAN"] = "l"
    table.align["TGL KIRIM"] = "l"
    table.align["JUMLAH"] = "r"
    table.align["TOTAL HARGA"] = "r"

    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

    return True 

def terima_produk(current_user):
    id_user = current_user.get("id_user", "")
    user_pembelian = pembelian.get(id_user, [])
    while True:
        jud_utama()
        jud_sub("Terima Produk")
        pesanan_aktif = [
            p for p in pembelian[id_user]
            if p["status_order"] == "Dikirim"]
        if not pesanan_aktif:
            pesan_peringatan("Tidak ada pesanan yang dapat diterima.", Fore.YELLOW, 20)
            inp_enter()
            return
        pilihan_id = [
            inquirer.List(
                "pesanan",
                message="Pilih produk yang diterima",
                choices=[f"{p['id_order']} │ {p['varian']} ({p['kemasan']}) │ {p['total_harga']}" for p in pesanan_aktif])]
        jawaban = inquirer.prompt(pilihan_id)
        if jawaban is None:
            return
        teks = jawaban["pesanan"]
        id_terpilih = teks.split(" │ ")[0].strip()

        produk = next((p for p in pesanan_aktif if p["id_order"] == id_terpilih), None)
        if not produk:
            pesan_peringatan("Pesanan tidak ditemukan!", Fore.RED, 12)       
            inp_enter()
            return

        print(("═"*50).center(70))
        print("")
        table = PrettyTable()
        table.field_names = ["    NAMA    ", "         DATA         "]
        table.add_row(["ID Order", produk["id_order"]])
        table.add_row(["Varian", produk["varian"]])
        table.add_row(["Kemasan", produk["kemasan"]])
        table.add_row(["Tanggal Dipesan", produk["tanggal_pesan"]])
        table.add_row(["Jumlah", produk["jumlah"]])
        table.add_row(["Total Harga", f"Rp{produk['total_harga']}"])
        table.align["    NAMA    "] = "l"
        table.align["         DATA         "] = "l"
        table_str = table.get_string()
        for line in table_str.split("\n"):
            print(line.center(70))
        print("")
        print(("═"*50).center(70))

        konfirmasi = [
            inquirer.List(
                "konfirm",
                message=f"Konfirmasi bahwa pesanan {produk['varian']} ({produk['kemasan']}) telah diterima?",
                choices=["            1 │ Ya", "            2 │ Tidak"])]
        jawab_konfirmasi = inquirer.prompt(konfirmasi)
        if not jawab_konfirmasi:
            return
        
        if jawab_konfirmasi["konfirm"] == "            1 │ Ya":
            produk["tanggal_sampai"] = datetime.now().strftime("%Y-%m-%d")
            produk["status_order"] = "Selesai"
            save_pembelian_to_csv(pembelian)
            pesan_berhasil("Produk telah diterima!")
            inp_enter()
            return
        else:
            pesan_peringatan("Produk batal diterima!", Fore.RED, 12)
            inp_enter()
            return


def produk_selesai(current_user):
    id_user = current_user.get("id_user", "")
    user_pembelian = pembelian.get(id_user, [])
    p_diterima = [p for p in user_pembelian if p.get("status_order") == "Selesai"]

    if not p_diterima:
        pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
        return None
    
    table = PrettyTable()
    table.field_names = ["ID", "VARIAN", "UKURAN", "TGL PESAN", "TGL KIRIM", "TGL SAMPAI", "JML", "TOTAL HARGA"]
    for idx, item in enumerate(p_diterima, start=1):
        harga = int(item.get("total_harga", 0))
        table.add_row([
            item.get("id_order"),
            item.get("varian"),
            item.get("kemasan"),
            item.get("tanggal_pesan"),
            item.get("tanggal_dikirim"),
            item.get("tanggal_sampai"),
            item.get("jumlah"),
            f"Rp{harga:,}"])

    table.align["ID"] = "l"
    table.align["VARIAN"] = "l"
    table.align["UKURAN"] = "l"
    table.align["TGL PESAN"] = "l"
    table.align["TGL KIRIM"] = "l"
    table.align["TGL SAMPAI"] = "l"
    table.align["JUMLAH"] = "r"
    table.align["TOTAL HARGA"] = "r"

    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

    return True 


def produk_dibatalkan(current_user):
    id_user = current_user.get("id_user", "")
    user_pembelian = pembelian.get(id_user, [])
    p_dibatalkan = [p for p in user_pembelian if p.get("status_order") == "Dibatalkan"]

    if not p_dibatalkan:
        pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
        return None
    
    table = PrettyTable()
    table.field_names = ["ID", "VARIAN", "UKURAN", "TGL PESAN", "JML", "TOTAL HARGA", "ALASAN"]
    for idx, item in enumerate(p_dibatalkan, start=1):
        harga = int(item.get("total_harga", 0))
        table.add_row([
            item.get("id_order"),
            item.get("varian"),
            item.get("kemasan"),
            item.get("tanggal_pesan"),
            item.get("jumlah"),
            f"Rp{harga:,}",
            item.get("alasan")])

    table.align["ID"] = "l"
    table.align["VARIAN"] = "l"
    table.align["UKURAN"] = "l"
    table.align["TGL PESAN"] = "l"
    table.align["JML"] = "r"
    table.align["TOTAL HARGA"] = "r"
    table.align["ALASAN"] = "c"

    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

    return True 


# MENU SALDO
# ════════════════════════════════════════════════════
def saldo(current_user):
    while True:
        jud_utama()
        jud_sub("Saldo Anda")
        pesan_peringatan(f"Rp{current_user.get('saldo', 0):,}".replace(",", "."), Fore.CYAN, 20)
        print("")
        print(("═"*50).center(70))
        pilih = tamp_kons("2.5")
        if pilih == "1 │ TOP UP":
            top_up(current_user)
        elif pilih == "2 │ KEMBALI":
            break

def top_up(current_user):
    while True:
        jud_utama()
        jud_sub("Top Up Saldo")
        inp = input("Masukkan jumlah saldo top up (ketik 'kembali' untuk kembali): ").strip()
        if inp == "kembali":
            return None
        try:
            topup = int(inp)
            if topup == 0 or topup < 0:
                pesan_peringatan("Jumlah top up tidak boleh nol atau negatif!", Fore.YELLOW, 20)
                inp_enter()
                continue
            elif topup < 10000:
                pesan_peringatan("Jumlah top up minimal Rp10.000!", Fore.YELLOW, 30)
                inp_enter()
                continue
            else:
                konfirmasi = [
                    inquirer.List(
                        "konfirm",
                        message=f"Konfirmasi ingin top up sebesar Rp{topup:,}?",
                        choices=["            1 │ Ya", "            2 │ Tidak"])]
                jawab_konfirmasi = inquirer.prompt(konfirmasi)
                if not jawab_konfirmasi:
                    return
                if jawab_konfirmasi["konfirm"] == "            1 │ Ya":
                    current_user["saldo"] = current_user.get("saldo", 0) + topup
                    if "id_user" in current_user:
                        akun[current_user["id_user"]] = current_user
                        save_akun_to_csv(akun)
                    pesan_berhasil(f"Top up sebesar Rp{topup:,} berhasil!")
                    inp_enter()
                    break
                else:
                    pesan_peringatan("Tidak jadi melakukan top up!", Fore.RED, 12)
                    inp_enter()
                    return
        except ValueError:
            pesan_peringatan("Input tidak valid! Silakan masukkan angka.", Fore.YELLOW, 30)
            inp_enter()
            