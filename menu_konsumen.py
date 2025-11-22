import inquirer
from help import jud_utama, jud_sub, pesan_berhasil
from fungsi_konsumen import lihat_akun, lihat_produk

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

def menu_konsumen(username):
    while True:
        jud_utama()
        jud_sub(f"Selamat Datang, {username}!")
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
                choices=[
                    "1 | LIHAT AKUN",
                    "2 | LIHAT PRODUK",
                    "3 | KERANJANG BELANJA",
                    "4 | PESANAN ANDA",
                    "5 | RIWAYAT",
                    "6 | SALDO",
                    "7 | LOGOUT"])]
        answer = inquirer.prompt(questions)["menu"]

        if answer == "1 | LIHAT AKUN":
            jud_utama()
            jud_sub("Akun Saya")
            lihat_akun(username)
        elif answer == "2 | LIHAT PRODUK":
            jud_utama()
            jud_sub("Daftar Produk")
            lihat_produk()
        elif answer == "3 | KERANJANG BELANJA":
            jud_utama()
            jud_sub("Keranjang Belanja")
            keranjang_belanja(username)
        elif answer == "4 | PESANAN ANDA":
            jud_utama()
            jud_sub("Pesanan Anda")
            pesanan_anda(username)
        elif answer == "5 | RIWAYAT":
            jud_utama()
            jud_sub("Riwayat Belanja")
            riwayat(username)
        elif answer == "6 | SALDO":
            jud_utama()
            jud_sub("Saldo")
            saldo(username)
        elif answer == "7 | LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break