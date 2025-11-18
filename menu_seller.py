import os
import inquirer
from prettytable import PrettyTable
from colorama import Fore, Style
from colorama import Fore, Style, init
init(autoreset=True)


current_seller = {
    "username": "seller1",
    "nama": "khanza",
    "email": "seller1@gmail.com",
    "no_hp": "08123456789"
}

## daftar produk popcorn
produk_list = [
    # popcorn rasa caramel
    {"id": "C1", "varian": "Caramel",  "kemasan": "Small",  "harga": 5000,  "status": "Tersedia"},
    {"id": "C2", "varian": "Caramel",  "kemasan": "Medium", "harga": 10000, "status": "Tersedia"},
    {"id": "C3", "varian": "Caramel",  "kemasan": "Large",  "harga": 18000, "status": "Tersedia"},

    # popcorn rasa blueberry
    {"id": "B1", "varian": "Blueberry","kemasan": "Small",  "harga": 5000,  "status": "Tersedia"},
    {"id": "B2", "varian": "Blueberry","kemasan": "Medium", "harga": 10000, "status": "Tersedia"},
    {"id": "B3", "varian": "Blueberry","kemasan": "Large",  "harga": 18000, "status": "Tersedia"},

    # popcorn rasa matcha
    {"id": "M1", "varian": "Matcha",   "kemasan": "Small",  "harga": 5000,  "status": "Tersedia"},
    {"id": "M2", "varian": "Matcha",   "kemasan": "Medium", "harga": 10000, "status": "Tersedia"},
    {"id": "M3", "varian": "Matcha",   "kemasan": "Large",  "harga": 18000, "status": "Tersedia"},
]

# kosong karena perlu input dari user
pesanan_list = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# MENU SELLER UTAMA
def menu_seller():
    while True:
        clear()
        print("=== MENU SELLER POPCORN ===")
        pertanyaan_menu = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "Akun",
                    "Penjualan",
                    "Pembelian",
                    "Pemesanan",
                    "Status Pemesanan",
                    "Logout"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan_menu)
        if jawaban is None:
            break

        menu = jawaban["menu"]

        if menu == "Akun":
            menu_akun()
        elif menu == "Penjualan":
            menu_penjualan()
        elif menu == "Pembelian":
            menu_pembelian()
        elif menu == "Pemesanan":
            menu_pemesanan()
        elif menu == "Status Pemesanan":
            menu_status_pemesanan()
        elif menu == "Logout":
            break

# menu akun
def menu_akun():
    while True:
        clear()
        print("=== MENU AKUN SELLER ===")
        pertanyaan = [
            inquirer.List(
                "menu_akun",
                message="Pilih menu:",
                choices=[
                    "Lihat Data Diri",
                    "Edit Data Diri",
                    "Kembali"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        if jawaban is None:
            break

        pilihan = jawaban["menu_akun"]

        if pilihan == "Lihat Data Diri":
            lihat_data_diri()
        elif pilihan == "Edit Data Diri":
            edit_data_diri()
        elif pilihan == "Kembali":
            break


def lihat_data_diri():
    clear()
    print("=== DATA DIRI SELLER ===")

    table = PrettyTable()
    table.field_names = ["Field", "Data"]

    table.add_row(["Username", current_seller.get("username", "-")])
    table.add_row(["Nama", current_seller.get("nama", "-")])
    table.add_row(["Email", current_seller.get("email", "-")])
    table.add_row(["No. HP", current_seller.get("no_hp", "-")])

    table.align["Field"] = "l"
    table.align["Data"] = "l"

    print(table)
    input("Tekan enter untuk kembali ke Menu Akun...")


def edit_data_diri():
    clear()
    print("=== EDIT DATA DIRI SELLER ===")
    print(Fore.YELLOW + "Biarkan default jika tidak ingin mengubah.\n")

    pertanyaan = [
        inquirer.Text(
            "nama",
            message="Nama baru",
            default=current_seller.get("nama", "")
        ),
        inquirer.Text(
            "email",
            message="Email baru",
            default=current_seller.get("email", "")
        ),
        inquirer.Text(
            "no_hp",
            message="No. HP baru",
            default=current_seller.get("no_hp", "")
        )
    ]

    jawaban = inquirer.prompt(pertanyaan)
    if jawaban is None:
        return

    current_seller["nama"] = jawaban["nama"] or current_seller["nama"]
    current_seller["email"] = jawaban["email"] or current_seller["email"]
    current_seller["no_hp"] = jawaban["no_hp"] or current_seller["no_hp"]

    print(Fore.GREEN + "Data diri berhasil diperbarui!")
    input("Tekan enter untuk kembali ke Menu Akun...")

# menu penjualan (CRUD produk)
def menu_penjualan():
    while True:
        clear()
        print("=== MENU PENJUALAN (PRODUK POPCORN) ===")
        pertanyaan = [
            inquirer.List(
                "menu_penjualan",
                message="Pilih menu:",
                choices=[
                    "Tambah Produk",
                    "Lihat Produk",
                    "Edit Produk",
                    "Hapus Produk",
                    "Kembali"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        if jawaban is None:
            break

        pilihan = jawaban["menu_penjualan"]

        if pilihan == "Tambah Produk":
            create_produk()
        elif pilihan == "Lihat Produk":
            tampilkan_daftar_produk()
        elif pilihan == "Edit Produk":
            update_produk()
        elif pilihan == "Hapus Produk":
            delete_produk()
        elif pilihan == "Kembali":
            break


def create_produk():
    clear()
    print("=== TAMBAH PRODUK POPCORN ===")

    pertanyaan = [
        inquirer.Text("varian", message="Masukkan varian rasa baru"),
        inquirer.Text("kemasan", message="Masukkan ukuran kemasan (Small/Medium/Large)"),
        inquirer.Text("harga", message="Masukkan harga sesuai kemasan"),
        inquirer.List(
            "status",
            message="Status ketersediaan produk",
            choices=["Tersedia", "Habis"]
        )
    ]
    jawaban = inquirer.prompt(pertanyaan)

    if jawaban is None:
        return

    try:
        harga = int(jawaban["harga"])
    except ValueError:
        print(Fore.RED + "Harga harus berupa angka! Tekan enter untuk kembali...")
        input()
        return

    # buat id otomatis yang baru 
    varian = jawaban["varian"].strip()
    if varian == "":
        print(Fore.RED + "Varian tidak boleh kosong.")
        input("Tekan enter untuk kembali...")
        return

    kode = varian[0].upper()
    existing_ids = [p["id"] for p in produk_list if p["id"].startswith(kode)]
    # pakai max num agar tidak ada id duplikat
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
        "kemasan": jawaban["kemasan"],
        "harga": harga,
        "status": jawaban["status"]
    }

    produk_list.append(produk_baru)
    print(Fore.GREEN + f"Produk berhasil ditambahkan dengan ID {new_id}")
    input("Tekan enter untuk kembali...")


def tampilkan_daftar_produk():
    clear()
    if not produk_list:
        print(Fore.YELLOW + "Belum ada produk yang ditambahkan.")
        input("Tekan enter untuk kembali...")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Varian", "Kemasan", "Harga", "Status"]

    for p in produk_list:
        table.add_row([
            p["id"],
            p["varian"],
            p["kemasan"],
            f"Rp{p['harga']}",
            p["status"]
        ])

    table.align["ID"] = "c"
    table.align["Varian"] = "l"
    table.align["Kemasan"] = "l"
    table.align["Harga"] = "r"
    table.align["Status"] = "c"

    table_str = table.get_string()
    lines = table_str.split("\n")
    width = len(lines[0]) if lines else 0

    print("=== DAFTAR PRODUK POPCORN ===".center(width))
    print(table_str)
    input("\nTekan enter untuk kembali...")


def update_produk():
    clear()
    if not produk_list:
        print(Fore.YELLOW + "Belum ada produk yang bisa diubah.")
        input("Tekan enter untuk kembali...")
        return

    pilihan_id = [
        inquirer.List(
            "id_produk",
            message="Pilih produk yang akan diubah:",
            choices=[f"{p['id']} - {p['varian']} ({p['kemasan']})" for p in produk_list]
        )
    ]
    jawaban = inquirer.prompt(pilihan_id)
    if jawaban is None:
        return

    teks = jawaban["id_produk"]
    id_terpilih = teks.split(" - ")[0]

    produk = next((p for p in produk_list if p["id"] == id_terpilih), None)

    if not produk:
        print(Fore.RED + "Produk tidak ditemukan.")
        input("Tekan enter untuk kembali...")
        return

    clear()

    table = PrettyTable()
    table.field_names = ["Field", "Data"]
    table.add_row(["ID", produk["id"]])
    table.add_row(["Varian", produk["varian"]])
    table.add_row(["Kemasan", produk["kemasan"]])
    table.add_row(["Harga", f"Rp{produk['harga']}"])
    table.add_row(["Status", produk["status"]])
    table.align["Field"] = "l"
    table.align["Data"] = "l"

    table_str = table.get_string()
    lines = table_str.split("\n")
    width = len(lines[0]) if lines else 0

    print("=== UBAH DATA PRODUK ===".center(width))
    print(table_str)
    print()

    pertanyaan_update = [
        inquirer.Text(
            "varian",
            message="Varian baru",
            default=produk["varian"]
        ),
        inquirer.Text(
            "kemasan",
            message="Kemasan baru",
            default=produk["kemasan"]
        ),
        inquirer.Text(
            "harga",
            message="Harga baru",
            default=str(produk["harga"])
        ),
        inquirer.List(
            "status",
            message="Status ketersediaan",
            choices=["Tersedia", "Habis"],
            default=produk["status"]
        )
    ]

    jawab_update = inquirer.prompt(pertanyaan_update)
    if jawab_update is None:
        return

    produk["varian"] = jawab_update["varian"] or produk["varian"]
    produk["kemasan"] = jawab_update["kemasan"] or produk["kemasan"]

    if jawab_update["harga"]:
        try:
            produk["harga"] = int(jawab_update["harga"])
        except ValueError:
            print(Fore.RED + "Harga baru tidak valid, harga lama dipertahankan.")

    produk["status"] = jawab_update["status"]

    print(Fore.GREEN + "Data produk berhasil diubah!")
    input("Tekan enter untuk kembali...")


def delete_produk():
    clear()
    if not produk_list:
        print(Fore.YELLOW + "Belum ada produk yang bisa dihapus.")
        input("Tekan enter untuk kembali...")
        return

    pilihan_id = [
        inquirer.List(
            "id_produk",
            message="Pilih produk yang akan dihapus:",
            choices=[f"{p['id']} - {p['varian']} ({p['kemasan']})" for p in produk_list]
        )
    ]
    jawaban = inquirer.prompt(pilihan_id)
    if jawaban is None:
        return

    teks = jawaban["id_produk"]
    id_terpilih = teks.split(" - ")[0]

    produk = next((p for p in produk_list if p["id"] == id_terpilih), None)

    if not produk:
        print(Fore.RED + "Produk tidak ditemukan.")
        input("Tekan enter untuk kembali...")
        return

    konfirmasi = [
        inquirer.Confirm(
            "yakin",
            message=f"Yakin ingin menghapus produk '{produk['varian']} ({produk['kemasan']})'?",
            default=False
        )
    ]
    jawab_konfirmasi = inquirer.prompt(konfirmasi)
    if jawab_konfirmasi and jawab_konfirmasi["yakin"]:
        produk_list.remove(produk)
        print(Fore.GREEN + "Produk berhasil dihapus.")
    else:
        print(Fore.RED + "Produk batal dihapus.")
    input("Tekan enter untuk kembali...")

# menu pembelian
def menu_pembelian():
    while True:
        clear()
        print("=== MENU PEMBELIAN ===")
        pertanyaan = [
            inquirer.List(
                "menu_pembelian",
                message="Pilih menu:",
                choices=[
                    "Lihat Ringkasan Pembelian",
                    "Pemesanan",
                    "Status Pemesanan",
                    "Kembali"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        if jawaban is None:
            break

        pilihan = jawaban["menu_pembelian"]

        if pilihan == "Lihat Ringkasan Pembelian":
            lihat_ringkasan_pembelian()
        elif pilihan == "Pemesanan":
            menu_pemesanan()
        elif pilihan == "Status Pemesanan":
            menu_status_pemesanan()
        elif pilihan == "Kembali":
            break

def lihat_ringkasan_pembelian():
    clear()
    print("=== RINGKASAN PEMBELIAN ===")

    if not pesanan_list:
        print(Fore.YELLOW + "Belum ada data pembelian / pesanan.")
    else:
        total_transaksi = len(pesanan_list)
        total_omzet = sum(p["total_harga"] for p in pesanan_list)

        print(f"Total Transaksi : {total_transaksi}")
        print(f"Total Omzet     : Rp{total_omzet}")
        print("-" * 30)

        table = PrettyTable()
        table.field_names = ["ID", "Nama User", "Total Harga", "Status"]

        for psn in pesanan_list:
            table.add_row([
                psn["id_pesanan"],
                psn["nama_user"],
                f"Rp{psn['total_harga']}",
                psn.get("status_pesanan", "")
            ])

        table.align["ID"] = "c"
        table.align["Nama User"] = "l"
        table.align["Total Harga"] = "r"
        table.align["Status"] = "c"
        print(table)

    input("Tekan enter untuk kembali...")

# menu pemesanan
def menu_pemesanan():
    while True:
        clear()
        print("=== MENU PEMESANAN ===")
        pertanyaan = [
            inquirer.List(
                "menu_pemesanan",
                message="Pilih menu:",
                choices=[
                    "Lihat Pemesanan",
                    "Hapus Pemesanan",
                    "Kembali"
                ]
            )
        ]
        jawaban = inquirer.prompt(pertanyaan)
        if jawaban is None:
            break

        pilihan = jawaban["menu_pemesanan"]

        if pilihan == "Lihat Pemesanan":
            lihat_pemesanan()
        elif pilihan == "Hapus Pemesanan":
            hapus_pemesanan()
        elif pilihan == "Kembali":
            break

def lihat_pemesanan():
    clear()
    title = "DAFTAR PEMESANAN"
    print(title.center(70, "="))

    if not pesanan_list:
        print(Fore.YELLOW + "Belum ada pemesanan.")
    else:
        table = PrettyTable()
        table.field_names = [
            "ID Pesanan",
            "Nama User",
            "Produk",
            "Jumlah",
            "Total Harga",
            "Status"
        ]

        for psn in pesanan_list:
            table.add_row([
                psn["id_pesanan"],
                psn["nama_user"],
                psn["produk"],
                psn["jumlah"],
                f"Rp{psn['total_harga']}",
                psn.get("status_pesanan", "")
            ])
        for field in table.field_names:
            table.align[field] = "c"
        table.align["Produk"] = "l"
        print(table)
    input("Tekan enter untuk kembali...")

def hapus_pemesanan():
    clear()
    if not pesanan_list:
        print(Fore.YELLOW + "Belum ada pemesanan yang bisa dihapus.")
        input("Tekan enter untuk kembali...")
        return

    pilihan_pesanan = [
        inquirer.List(
            "id_pesanan",
            message="Pilih pemesanan yang akan dihapus:",
            choices=[f"{p['id_pesanan']} - {p['nama_user']} ({p['produk']})" for p in pesanan_list]
        )
    ]
    jawaban = inquirer.prompt(pilihan_pesanan)
    if jawaban is None:
        return

    teks = jawaban["id_pesanan"]
    id_terpilih = int(teks.split(" - ")[0])

    pesanan = next((p for p in pesanan_list if p["id_pesanan"] == id_terpilih), None)

    if not pesanan:
        print(Fore.RED + "Pemesanan tidak ditemukan.")
        input("Tekan enter untuk kembali...")
        return

    konfirmasi = [
        inquirer.Confirm(
            "yakin",
            message=f"Yakin ingin menghapus pemesanan ID {pesanan['id_pesanan']}?",
            default=False
        )
    ]
    jawab_konfirmasi = inquirer.prompt(konfirmasi)
    if jawab_konfirmasi and jawab_konfirmasi["yakin"]:
        pesanan_list.remove(pesanan)
        print(Fore.GREEN + "Pemesanan berhasil dihapus.")
    else:
        print(Fore.RED + "Pemesanan batal dihapus.")
    input("Tekan enter untuk kembali...")