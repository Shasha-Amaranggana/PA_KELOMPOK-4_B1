from data import akun, produk
import inquirer
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_no


# FUNGSI UMUM
# ════════════════════════════════════════════════════
def daftar_produk():
    global produk
    if len(produk) == 0:
        pesan_berhasil("Daftar produk belum ada.")
    else:
        print("ID     NAMA       UKURAN     HARGA      STOK       RATE")
        print("──" * 30)
        no = 1
        for nomor, k in produk.items():
            print(no,"| ", k["nm"], " "*(14 - len(k["nm"])), k["sz"], " "*(9 - len(k["sz"])), k["pz"], " "*(11 - len(k["pz"])), k["stk"], " "*(9 - len(k["stk"])), k["rt"])
            no = no + 1

