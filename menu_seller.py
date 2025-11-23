import csv
import inquirer
from prettytable import PrettyTable
from data import akun, produk_list, save_produk_to_csv, save_akun_to_csv
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_enter
from colorama import Fore, Style, init
from menu_bos import daftar_produk
init(autoreset=True)

pesanan_list = []

def tamp_sell(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ AKUN'.center(25), '2 │ PENJUALAN'.center(31), '3 │ PEMBELIAN'.center(31),  '4 │ PEMESANAN'.center(31), '5 │ STATUS PEMESANAN'.center(37), '6 │ LOGOUT'.center(27)],
        "2.1" : ['1 │ LIHAT DATA DIRI'.center(37), '2 │ EDIT DATA DIRI'.center(36), '3 │ KEMBALI'.center(29)],
        "2.2" : ['1 │ TAMBAH PRODUK'.center(35), '2 │ LIHAT PRODUK'.center(34), '3 │ EDIT PRODUK'.center(33), '4 │ HAPUS PRODUK'.center(34), '5 │ KEMBALI'.center(29)],
        "2.3" : ['1 │ LIHAT RINGKASAN PEMBELIAN'.center(47), '2 │ KEMBALI'.center(29)],
        "2.4" : ['1 │ LIHAT PEMESANAN'.center(37), '2 │ HAPUS PEMESANAN'.center(37), '3 │ KEMBALI'.center(29)],
        "2.5" : ['1 │ BUAT STATUS AWAL PESANAN'.center(46), '2 │ LIHAT STATUS PESANAN'.center(41), '3 │ KEMBALI'.center(29)]}
    choices = daftar_menu[jenis]
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan 

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
        elif pilih == "5 │ STATUS PEMESANAN":
            menu_status_pemesanan()
        elif pilih == "6 │ LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break

# MENU AKUN
# ════════════════════════════════════════════════════
def menu_akun(current_user):
    while True:
        jud_utama()
        jud_sub("Menu Akun Seller")
        pilih = tamp_sell("2.1")
        if pilih == "1 │ LIHAT DATA DIRI":
            jud_utama()
            jud_sub("Data Diri Seller")
            lihat_data_diri(current_user)
            print("")
            inp_enter()
        elif pilih == "2 │ EDIT DATA DIRI":
            jud_utama()
            jud_sub("Edit Data Diri Seller")
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
        inquirer.Text("alamat", message="Alamat baru", default=current_user.get("alamat", "")),
    ]
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

    if "id" in current_user:
        akun[current_user["id"]] = current_user
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
    existing_ids = [p["id"] for p in produk_list if p["id"].startswith(kode)]
    max_num = 0
    for pid in existing_ids:
        tail = pid[1:]
        if tail.isdigit():
            num = int(tail)
            if num > max_num:
                max_num = num
    new_id = f"{kode}{max_num + 1}"

    produk_baru = {
        "id": new_id,
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
            "id_produk",
            message="Pilih produk yang akan diubah",
            choices=[f"{p['id']} │ {p['varian']} ({p['kemasan']})" for p in produk_list])]
    jawaban = inquirer.prompt(pilihan_id)
    if jawaban is None:
        return
    teks = jawaban["id_produk"]
    id_terpilih = teks.split(" │ ")[0].strip()
    produk = next((p for p in produk_list if p["id"] == id_terpilih), None)

    if not produk:
        pesan_peringatan("Produk tidak ditemukan!", Fore.RED, 12)       
        inp_enter()
        return
    
    print(("═"*50).center(70))
    print("")
    table = PrettyTable()
    table.field_names = ["    NAMA    ", "         DATA         "]
    table.add_row(["ID", produk["id"]])
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

    produk["varian"] = jawab_update["varian"] or produk["varian"]
    produk["kemasan"] = kemasan_map[jawab_update["kemasan"]] or produk["kemasan"]
    if jawab_update["harga"] or jawab_update["stok"]:
        try:
            produk["harga"] = int(jawab_update["harga"])
            produk["stok"] = int(jawab_update["stok"]) 
        except ValueError:
            pesan_peringatan("Harga dan stok baru tidak valid! Harga dan stok lama dipertahankan.", Fore.YELLOW, 30)       
    save_produk_to_csv(produk_list)
    pesan_berhasil("Data produk berhasil diubah!")
    inp_enter()

def delete_produk():
    global produk_list
    if len(produk_list) == 0:
        pesan_peringatan("Daftar produk masih kosong.", Fore.YELLOW, 12)
        input("→ 「 Enter untuk kembali 」")
        return
    pilihan_id = [
        inquirer.List(
            "id_produk",
            message="Pilih produk yang akan dihapus",
            choices=[f"{p['id']} │ {p['varian']} ({p['kemasan']})" for p in produk_list])]
    jawaban = inquirer.prompt(pilihan_id)
    if jawaban is None:
        return
    teks = jawaban["id_produk"]
    id_terpilih = teks.split(" │ ")[0].strip()
    produk = next((p for p in produk_list if p["id"] == id_terpilih), None)

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
    global pesanan_list
    if len(pesanan_list) == 0:
        pesan_peringatan("Daftar pembelian masih kosong.", Fore.YELLOW, 12)
    else:
        total_transaksi = len(pesanan_list)
        total_omzet = sum(p["total_harga"] for p in pesanan_list)

        print(f"Total Transaksi : {total_transaksi}")
        print(f"Total Omzet     : Rp{total_omzet}")
        print("-" * 30)

        table = PrettyTable()
        table.field_names = ["NO", " ID_U ", " ID_P ", " NAMA USER ", "TOTAL HARGA", " STATUS "]
        for idx, p in enumerate(pesanan_list, start=1):
            table.add_row([
                idx,
                p["id_user"],
                p["id_pesanan"],
                p["nama_user"],
                f"Rp{p['total_harga']}",
                p.get("status_pesanan", "")])
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
        elif pilihan == "2 │ HAPUS PEMESANAN":
            jud_utama()
            jud_sub("Hapus Pemesanan")
            hapus_pemesanan()
            print("")
            inp_enter()
        elif pilihan == "3 │ KEMBALI":
            break

def lihat_pemesanan():
    global pesanan_list
    if len(pesanan_list) == 0:
        pesan_peringatan("Daftar pemesanan masih kosong.", Fore.YELLOW, 12)
        return
    else:
        table = PrettyTable()
        table.field_names = ["NO", " ID_U ", " ID_P ", " NAMA USER ", " PRODUK ", "TOTAL HARGA", " STATUS "]

        for psn in pesanan_list:
            table.add_row([
                psn["id_pesanan"],
                psn["nama_user"],
                psn["produk"],
                psn["jumlah"],
                f"Rp{psn['total_harga']}",
                psn.get("status_pesanan", "")])
        for field in table.field_names:
            table.align[field] = "c"
        table.align["Produk"] = "l"
        print(table)
    inp_enter()

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

# MENU STATUS PEMESANAN
# ════════════════════════════════════════════════════
def menu_status_pemesanan():
    while True:
        jud_utama()
        jud_sub("Menu Status Pemesanan")
        pilihan = tamp_sell("2.5")
        if pilihan == "1 │ BUAT STATUS AWAL PESANAN":
            jud_utama()
            jud_sub("Status Awal Pesanan")
            buat_status_pesanan_awal()
            print("")
            inp_enter()
        elif pilihan == "2 │ LIHAT STATUS PESANAN":
            jud_utama()
            jud_sub("Lihat Status Pemesanan")
            lihat_status_pesanan()
            print("")
            inp_enter()
        elif pilihan == "3 │ KEMBALI":
            break

def buat_status_pesanan_awal():
    pesanan_tanpa_status = [p for p in pesanan_list if not p.get("status_pesanan")]

    if not pesanan_tanpa_status:
        pesan_peringatan("Tidak ada pesanan yang belum memiliki status.", Fore.YELLOW, 20)
        return

    pilihan_pesanan = [
        inquirer.List(
            "id_pesanan",
            message="Pilih pesanan yang akan diberi status awal:",
            choices=[f"{p['id_pesanan']} - {p['nama_user']} ({p['produk']})" for p in pesanan_tanpa_status])]
    jawaban = inquirer.prompt(pilihan_pesanan)
    if jawaban is None:
        return

    teks = jawaban["id_pesanan"]
    id_terpilih = int(teks.split(" - ")[0])

    pesanan = next((p for p in pesanan_list if p["id_pesanan"] == id_terpilih), None)

    if not pesanan:
        pesan_peringatan("Pesanan tidak ditemukan.", Fore.RED, 12)
        return

    status_awal_choices = ["Menunggu", "Diproses", "Dikonfirmasi"]
    tanya_status = [
        inquirer.List(
            "status_awal",
            message="Pilih status pesanan awal:",
            choices=status_awal_choices)]
    jawab_status = inquirer.prompt(tanya_status)
    if jawab_status is None:
        return
    pesanan["status_pesanan"] = jawab_status["status_awal"]
    pesan_berhasil(f"Status pesanan ID {pesanan['id_pesanan']} berhasil diatur menjadi '{pesanan['status_pesanan']}'.")

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