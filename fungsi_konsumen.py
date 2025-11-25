import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_enter
from menu import daftar_produk
from prettytable import PrettyTable
from data import akun, save_akun_to_csv, keranjang, produk_list, save_keranjang_to_csv, current_user, save_pembelian_to_csv, pembelian, save_produk_to_csv
from colorama import Fore, Style, init
from datetime import datetime

init(autoreset=True)

def tamp_kons(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ AKUN'.center(25), '2 | LIHAT PRODUK'.center(33), '3 | KERANJANG BELANJA'.center(39),  '4 | PESANAN'.center(29), '5 | RIWAYAT BELANJA'.center(29), '6 | SALDO'.center(27), '7 | LOGOUT'.center(27)],
        "2.1" : ['1 │ LIHAT DATA DIRI'.center(37), '2 │ EDIT DATA DIRI'.center(36), '3 │ KEMBALI'.center(29)],
        "2.2" : ['1 │ TAMBAH KE KERANJANG'.center(41), '2 │ PESAN SEKARANG'.center(35), '3 │ KEMBALI'.center(29)],
        "2.3" : ['1 │ HAPUS PRODUK DARI KERANJANG'.center(50), '2 │ PESAN SEKARANG'.center(35), '3 │ KEMBALI'.center(29)],
        "3.1" : ['1 │ TAMBAH KE KERANJANG'.center(33), '2 │ PESAN SEKARANG'.center(33), '3 │ KEMBALI'.center(29)],
        "4.1" : ['1 │ TOP UP'.center(28), '2 │ KEMBALI'.center(29)]}
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


# MENU AKUN
# ════════════════════════════════════════════════════
def menu_akun(current_user):
    while True:
        jud_utama()
        jud_sub("Menu Akun")
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
    id_user = current_user.get("id", "")
    while True:
        jud_utama()
        jud_sub("Tambah ke Keranjang")
        pilihan_id = [
            inquirer.List(
                "id_produk",
                message="Pilih produk yang akan ditambahkan",
                choices=[f"{p['id']} │ {p['varian']} ({p['kemasan']}) │ Rp{p['harga']}" for p in produk_list])]
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
        if int(produk["stok"]) <= 0:
            pesan_peringatan("Stok produk telah habis! Tidak dapat dimasukkan ke keranjang.", Fore.RED, 12)
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

        konfirmasi = [
            inquirer.List(
                "konfirm",
                message=f"Konfirmasi ingin memasukkan {produk['varian']} ({produk['kemasan']}) ke keranjang?",
                choices=["            1 │ Ya", "            2 │ Tidak"])]
        jawab_konfirmasi = inquirer.prompt(konfirmasi)
        if not jawab_konfirmasi:
            return
        if jawab_konfirmasi["konfirm"] == "            1 │ Ya":
            user_items = keranjang.get(id_user, [])

            existing = next((item for item in user_items if item["id_produk"] == id_terpilih), None)
            if existing:
                pesan_peringatan("Produk sudah ada di keranjang anda!", Fore.YELLOW, 12)
                inp_enter()
                return

            user_items.append({
                "id_produk": produk["id"],
                "varian": produk["varian"],
                "kemasan": produk["kemasan"],
                "harga": int(produk["harga"])})

            save_keranjang_to_csv(keranjang)
            pesan_berhasil("Produk berhasil ditambahkan ke keranjang anda!")
            inp_enter()
            return

        else:
            pesan_peringatan("Produk batal dimasukkan!", Fore.RED, 12)
            inp_enter()
            return

def pesan(current_user):
    id_user = current_user.get("id", "")
    saldo_user = int(current_user.get("saldo", 0))
    while True:
        jud_utama()
        jud_sub("Pesan Produk")
        pilihan_id = [
            inquirer.List(
                "id_produk",
                message="Pilih produk yang akan dipesan",
                choices=[f"{p['id']} │ {p['varian']} ({p['kemasan']}) │ Rp{p['harga']}" for p in produk_list])]
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
        if int(produk["stok"]) <= 0:
            pesan_peringatan("Stok produk telah habis! Tidak dapat dipesan", Fore.RED, 12)
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
                    pesan_peringatan("Jumlah top up tidak boleh nol atau negatif!", Fore.YELLOW, 20)
                    inp_enter()
                    continue
                elif jumlah > int(produk["stok"]) :
                    pesan_peringatan("Jumlah produk melebihi stok yang tersedia!", Fore.YELLOW, 30)
                    inp_enter()
                    continue
                else:
                    total_harga = int(produk["harga"]) * jumlah
                    if saldo_user < total_harga:
                        pesan_peringatan("Saldo anda tidak mencukupi untuk membeli produk ini!", Fore.RED, 12)
                        inp_enter()
                        return
            except ValueError:
                pesan_peringatan("Input tidak valid! Silakan masukkan angka.", Fore.YELLOW, 30)
                inp_enter()

            now = datetime.now().strftime("%Y%m%d%H%M%S")
            id_order = f"O{now}"

            pembelian[id_user].append({
                "id_order": id_order,
                "id_produk": produk["id"],
                "varian": produk["varian"],
                "kemasan": produk["kemasan"],
                "harga": int(produk["harga"]),
                "id_user": id_user,
                "tanggal_pesan": datetime.now().strftime("%Y-%m-%d"),
                "tanggal_dikirim": "",
                "tanggal_sampai": "",
                "jumlah": jumlah,
                "total_harga": total_harga,
                "status": "Dipesan",
                "batal_oleh": "",
                "alasan": ""})

            current_user["saldo"] = saldo_user - total_harga
            produk["stok"] = int(produk["stok"]) - jumlah

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
        daftar_keranjang(current_user)
        print("")
        print(("═"*50).center(70))
        pilih = tamp_kons("2.3")
        if pilih == "1 │ HAPUS PRODUK DARI KERANJANG":
            hapus_keranjang(current_user)
        elif pilih == "2 │ PESAN SEKARANG":
            pesan(current_user)
        elif pilih == "3 │ KEMBALI":
            break

def daftar_keranjang(current_user):
    id_user = current_user.get("id", "")
    user_items = keranjang.get(id_user, [])

    if not user_items:
        pesan_peringatan("Daftar keranjang masih kosong.", Fore.YELLOW, 12)
        return
    
    table = PrettyTable()
    table.field_names = ["NO", "ID", "VARIAN", "UKURAN", "HARGA"]
    for idx, item in enumerate(user_items, start=1):
        pid = item.get("id_produk")
        varian = item.get("varian")
        kemasan = item.get("kemasan")
        harga = int(item.get("harga", 0))
        table.add_row([
            idx,
            pid,
            varian,
            kemasan,
            f"Rp{harga:,}"])

    table.align["NO"] = "l"
    table.align["ID"] = "l"
    table.align["VARIAN"] = "l"
    table.align["UKURAN"] = "l"
    table.align["HARGA"] = "r"

    table_str = table.get_string()
    for line in table_str.split("\n"):
        print(line.center(70))

def hapus_keranjang(current_user):
    id_user = current_user.get("id", "")
    user_items = keranjang.get(id_user, [])
    while True:
        jud_utama()
        jud_sub("Hapus Produk Dari Keranjang")
        pilihan_id = [
            inquirer.List(
                "id_keranjang",
                message="Pilih produk yang mau dihapus",
                choices=[f"{p['id_produk']} │ {p['varian']} ({p['kemasan']}) │ {p['harga']}" for p in user_items])]
        jawaban = inquirer.prompt(pilihan_id)
        if jawaban is None:
            return
        teks = jawaban["id_keranjang"]
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


# MENU RIWAYAT BELANJA
# ════════════════════════════════════════════════════



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

