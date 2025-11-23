import inquirer
from help import jud_utama, jud_sub, pesan_berhasil
from fungsi_konsumen import menu_akun, lihat_produk, keranjang_belanja, belanja, pesanan_anda, saldo, tamp_kons
from menu import menu_akun


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
            saldo(current_user)
        elif pilih == "7 | LOGOUT":
            pesan_berhasil("Logout Berhasil!")
            break