import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_enter
from data_konsumen import keranjang_user, init_keranjang_user
from menu import daftar_produk
from prettytable import PrettyTable
from data import akun, save_akun_to_csv
from colorama import Fore, Style, init
init(autoreset=True)

def tamp_kons(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ AKUN'.center(25), '2 | LIHAT PRODUK'.center(33), '3 | KERANJANG BELANJA'.center(39),  '4 | BELANJA'.center(29), '5 | RIWAYAT'.center(29), '6 | SALDO'.center(27), '7 | LOGOUT'.center(27)],
        "2.1" : ['1 │ LIHAT DATA DIRI'.center(37), '2 │ EDIT DATA DIRI'.center(36), '3 │ KEMBALI'.center(29)],
        "4.1" : ['1 │ TOP UP'.center(28), '2 │ KEMBALI'.center(29)]}
    choices = daftar_menu[jenis]
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan 


# MENU AKUN
# ════════════════════════════════════════════════════
def menu_akun(current_user):
    while True:
        jud_utama()
        jud_sub("Menu Akun")
        # import tamp_kons here to avoid circular import at module load time
        from menu_konsumen import tamp_kons
        pilih = tamp_kons("2.1")
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


# MENU LIHAT PRODUK
# ════════════════════════════════════════════════════
def lihat_produk():
    while True:
        jud_utama()
        jud_sub("Daftar Produk")
        daftar_produk()  

        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Belanja",
                    "2. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Belanja":
            belanja()
        elif answer == "2. Kembali":
            break


# MENU KERANJANG BELANJA
# ════════════════════════════════════════════════════
def keranjang_belanja():
    while True:
        jud_utama()
        jud_sub("Keranjang Belanja")

        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Lihat Keranjang Belanja",
                    "2. Edit Keranjang Belanja",
                    "3. Pesan Sekarang",
                    "4. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Lihat Keranjang Belanja":
            lihat_keranjang()

        elif answer == "2. Edit Keranjang Belanja":
            edit_keranjang()

        elif answer == "3. Pesan Sekarang":
            pesan_sekarang()

        elif answer == "4. Kembali":
            break

def lihat_keranjang(username):
    init_keranjang_user(username)
    keranjang = keranjang_user[username]

    if not keranjang:
        pesan_peringatan("KERANJANG MASIH KOSONG", Fore.YELLOW, 30)
        return

    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Size", "Harga", "Jumlah", "Total"]
    table.align["ID"] = "l"
    table.align["Nama Produk"] = "l"
    table.align["Size"] = "l"
    table.align["Harga"] = "r"
    table.align["Jumlah"] = "r"
    table.align["Total"] = "r"

    for pid, item in keranjang.items():
        harga = int(item["pz"])
        jumlah = int(item["jumlah"])
        total = harga * jumlah

        table.add_row([
            pid,
            item["nm"],
            item["sz"],
            f"Rp{harga:,}",
            jumlah,
            f"Rp{total:,}"
        ])

    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))
    print("\n")

def edit_keranjang(username, keranjang_user):
    
    if username not in keranjang_user or not keranjang_user[username]:
        print("Keranjang Anda masih kosong.")
        return
    print("=== Edit Keranjang Belanja ===")

    table = PrettyTable()
    table.field_names = ["ID", "Nama Produk", "Size", "Harga", "Jumlah", "Total"]

    for pid, item in keranjang_user[username].items():
        total = item["harga"] * item["jumlah"]
        table.add_row([pid, item["nama"], item["size"], item["harga"], item["jumlah"], total])
    print(table)

    hapus_id = input("\nMasukkan ID produk yang ingin dihapus: ")

    if hapus_id not in keranjang_user[username]:
        print(" ID tidak ditemukan di keranjang.")
        return

    del keranjang_user[username][hapus_id]
    print("Barang berhasil dihapus dari keranjang")





# MENU BELANJA
# ════════════════════════════════════════════════════
def belanja():
    while True:
        jud_utama()
        jud_sub("Pesan")
        daftar_produk()  
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Tambah ke Keranjang",
                    "2. Beli Sekarang",
                    "3. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Tambah ke Keranjang":
            tambah_keranjang()

        elif answer == "2. Beli Sekarang":
            beli_sekarang()

        elif answer == "3. Kembali":
            break


# MENU RIWAYAT
# ════════════════════════════════════════════════════
def pesanan_anda():
    while True:
        jud_utama()
        jud_sub("Riwayat")

        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1. Riwayat pemesanan",
                    "2. Edit pemesanan(Cancel)",
                    "3. Kembali"])]

        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Riwayat pemesanan":
            riwayat_pemesanan()

        elif answer == "2. Edit pemesanan(Cancel)":
            edit_pemesanan()

        elif answer == "3. Kembali":
            break


# MENU SALDO
# ════════════════════════════════════════════════════
def saldo(current_user):
    while True:
        jud_utama()
        jud_sub("Saldo Anda")
        pesan_peringatan(f"Rp{current_user.get('saldo', 0):,}".replace(",", "."), Fore.CYAN, 20)
        print("")
        print(("═"*50).center(70))
        pilih = tamp_kons("4.1")
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
                current_user["saldo"] = current_user.get("saldo", 0) + topup
                if "id" in current_user:
                    akun[current_user["id"]] = current_user
                    save_akun_to_csv(akun)
                pesan_berhasil(f"Top up sebesar Rp {topup:,} berhasil!")
                inp_enter()
                break
        except ValueError:
            pesan_peringatan("Input tidak valid! Silakan masukkan angka.", Fore.YELLOW, 30)
            inp_enter()

