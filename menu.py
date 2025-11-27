import csv
import re
import inquirer
from prettytable import PrettyTable
from datetime import datetime
from data import akun, produk_list, keranjang, pembelian, save_produk_to_csv, save_akun_to_csv, save_pembelian_to_csv
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
        "2.4" : ['1 │ LIHAT PEMESANAN'.center(37), '2 │ UBAH STATUS PESANAN'.center(42), '3 │ LIHAT STATUS PESANAN'.center(41), '4 │ HAPUS PEMESANAN'.center(37), '5 │ KEMBALI'.center(29)]}
    choices = daftar_menu[jenis]
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan



# ════════════════════════════════════════════════════
#              MENU BOS DAN FITURNYA
# ════════════════════════════════════════════════════

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
def laporan():
    print("belum kepikiran")



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
            menu_akun(current_user)
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
def menu_akun(current_user):
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
    
    email_val = (jawaban.get("email") or current_user.get("email") or "").strip()
    no_hp_val = (jawaban.get("no_hp") or current_user.get("no_hp") or "").strip()
    if not email_val.endswith("@gmail.com") or not no_hp_val.startswith("08"):
        if not email_val.endswith("@gmail.com"):
            pesan_peringatan("Email harus valid dan berakhiran '@gmail.com'!", Fore.YELLOW, 30)
        if not no_hp_val.startswith("08"):
            pesan_peringatan("No. HP harus valid dan berawalan '08'!", Fore.YELLOW, 30)
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
            produk["harga"] = int(jawab_update["harga"])
            produk["stok"] = int(jawab_update["stok"])
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
        return None

    total_transaksi = len(semua_pesanan_selesai)
    total_omzet = sum(p["total_harga"] for p in semua_pesanan_selesai)

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
            jud_sub("Daftar Pemesanan")
            lihat_pemesanan()
            print("")
            inp_enter()
        elif pilihan == "2 │ UBAH STATUS PESANAN":
            jud_utama()
            jud_sub("Ubah Status Pesanan")
            ubah_status_pesanan()
        elif pilihan == "3 │ LIHAT STATUS PESANAN":
            jud_utama()
            jud_sub("Hapus Pemesanan")
            lihat_status_pesanan()
            print("")
            inp_enter()
        elif pilihan == "4 │ HAPUS PEMESANAN":
            jud_utama()
            jud_sub("Hapus Pemesanan")
            hapus_pemesanan()
            print("")
            inp_enter()
        elif pilihan == "5 │ KEMBALI":
            break


def lihat_pemesanan():
    pesanan_aktif = []

    for id_user, daftar_pesanan in pembelian.items():
        for p in daftar_pesanan:
            if p.get("status_order") == "Dipesan":
                p["id_user"] = id_user
                pesanan_aktif.append(p)

    if not pesanan_aktif:
        pesan_peringatan("Daftar pesanan masih kosong.", Fore.YELLOW, 12)
        print("")
        return None
    
    table = PrettyTable()
    table.field_names = ["ID", "ID U", "ID P", "VARIAN", "KEMASAN", "JML", "TOTAL HARGA", "STATUS", "TANGGAL PESAN"]
    for p in pesanan_aktif:
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
    global pesanan_list
    if len(pesanan_list) == 0:
        pesan_peringatan("Daftar pemesanan masih kosong.", Fore.YELLOW, 12)
        return
    else:
        table = PrettyTable()
        table.field_names = [
            "ID Pesanan",
            "Nama User",
            "Produk",
            "Jumlah",
            "Total Harga",
            "Status"]

        for psn in pesanan_list:
            table.add_row([
                psn["id_pesanan"],
                psn["nama_user"],
                psn["produk"],
                psn["jumlah"],
                f"Rp{psn['total_harga']}",
                psn.get("status_pesanan", "(belum ada status)")])
        for field in table.field_names:
            table.align[field] = "c"
        table.align["Produk"] = "l"
        print(table)

def hapus_pemesanan():
    global pesanan_list
    if len(pesanan_list) == 0:
        pesan_peringatan("Daftar pemesanan masih kosong.", Fore.YELLOW, 12)
        return

    pilihan_pesanan = [
        inquirer.List(
            "id_pesanan",
            message="Pilih pemesanan yang akan dihapus:",
            choices=[f"{p['id_pesanan']} - {p['nama_user']} ({p['produk']})" for p in pesanan_list])
    ]
    jawaban = inquirer.prompt(pilihan_pesanan)
    if jawaban is None:
        return

    teks = jawaban["id_pesanan"]
    id_terpilih = int(teks.split(" - ")[0])

    pesanan = next((p for p in pesanan_list if p["id_pesanan"] == id_terpilih), None)

    if not pesanan:
        pesan_peringatan("Pemesanan tidak ditemukan.", Fore.RED, 12)
        inp_enter()
        return

    konfirmasi = [
        inquirer.Confirm(
            "yakin",
            message=f"Yakin ingin menghapus pemesanan ID {pesanan['id_pesanan']}?",
            default=False)]
    jawab_konfirmasi = inquirer.prompt(konfirmasi)
    if jawab_konfirmasi and jawab_konfirmasi["yakin"]:
        pesanan_list.remove(pesanan)
        pesan_peringatan("Pemesanan berhasil dihapus.", Fore.GREEN, 12)
    else:
        pesan_peringatan("Pemesanan batal dihapus.", Fore.RED, 12)
    inp_enter()