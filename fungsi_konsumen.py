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
        "1": ['1 │ AKUN'.center(25), '2 | LIHAT PRODUK'.center(33), '3 | KERANJANG BELANJA'.center(39),  '4 | RIWAYAT PESANAN'.center(37), '5 | SALDO'.center(27), '6 | LOGOUT'.center(27)],
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
                    pesan_peringatan("Jumlah top up tidak boleh nol atau negatif!", Fore.YELLOW, 20)
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

            now = datetime.now().strftime("%Y%m%d")
            id_order = f"O{now}"

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

