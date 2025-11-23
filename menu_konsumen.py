import inquirer
from help import jud_utama, jud_sub, pesan_berhasil
from fungsi_konsumen import menu_akun, lihat_produk, keranjang_belanja, belanja, pesanan_anda, saldo
from menu import menu_akun

def tamp_kons(jenis):
    message = "Silakan pilih menu"
    daftar_menu = {
        "1": ['1 │ AKUN'.center(25), '2 | LIHAT PRODUK'.center(33), '3 | KERANJANG BELANJA'.center(39),  '4 | BELANJA'.center(29), '5 | RIWAYAT'.center(29), '6 | SALDO'.center(27), '7 | LOGOUT'.center(27)],
        "2.1" : ['1 │ LIHAT DATA DIRI'.center(37), '2 │ EDIT DATA DIRI'.center(36), '3 │ KEMBALI'.center(29)]}
    choices = daftar_menu[jenis]
    answer = inquirer.prompt([
        inquirer.List(
            'menu',
            message = message,
            choices = choices)])
    pilihan = answer['menu'].strip()
    return pilihan 

def menu_konsumen(current_user):
    while True:
        jud_utama()
        jud_sub(f"Selamat Datang!")
        pilih = tamp_kons("1")
        if pilih == "1 │ AKUN":
            menu_akun(current_user)
        elif pilih == "2 | LIHAT PRODUK":
            jud_utama()
            jud_sub("Daftar Produk")
            lihat_produk()
        elif pilih == "3 | KERANJANG BELANJA":
            jud_utama()
            jud_sub("Keranjang Belanja")
            keranjang_belanja(current_user)
        elif pilih == "4 | BELANJA":
            jud_utama()
            jud_sub("Belanja")
            belanja(current_user)
        elif pilih == "5 | RIWAYAT":
            jud_utama()
            jud_sub("Riwayat Belanja")
            pesanan_anda(current_user)
        elif pilih == "6 | SALDO":
            jud_utama()
            jud_sub("Saldo")
            saldo(current_user)
        elif pilih == "7 | LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break