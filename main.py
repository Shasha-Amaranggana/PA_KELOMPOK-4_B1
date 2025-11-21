import inquirer
import re
from datetime import datetime
from menu_bos import menu_boss
from data import akun, save_akun_to_csv
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from menu_seller import menu_seller
from menu_konsumen import menu_konsumen

def login():
    jud_utama()
    jud_sub("Silakan Login")
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if username == "" or password == "":
            pesan_peringatan("Semua kolom harus diisi!", 12)
            raise ValueError
        found = False
        for nomor, user in akun.items():
            if user["us"] == username and user["pw"] == password:
                found = True
                if user["status"].lower() != "aktif":
                    pesan_peringatan(f"Akun '{username}' saat ini {user['status']}. Tidak bisa login!", 30)
                    raise ValueError
                pesan_berhasil(f"Login berhasil! Selamat datang, {username}!")
                input("→ 「 Enter untuk lanjut 」")
                if user["role"] == "Bos":
                    menu_boss()
                elif user["role"] == "Seller":
                    menu_seller()
                elif user["role"] == "Konsumen":
                    menu_konsumen(username)
                input("→ 「 Enter untuk kembali 」")
                return
        if not found:
            pesan_peringatan("Username atau Password salah atau akun belum terdaftar!", 27)
            raise ValueError
    except ValueError:
        input("→ 「 Enter untuk kembali 」")
        return None
    
def register():
    jud_utama()
    jud_sub("Silakan Registrasi")
    print("   > Username min 5 karakter, mengandung huruf/angka,")
    print("     tidak mengandung karakter spesial!")
    print("   > Password min 8 karakter, mengandung huruf besar & kecil & angka,")
    print("     tidak mengandung karakter spesial!")
    print("")
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if username == "" or password == "":
            pesan_peringatan("Semua kolom harus diisi!", 12)
            raise ValueError
        elif not re.search(r"^[a-zA-Z0-9]{5,}$", username):
            pesan_peringatan("Sesuaikan dengan syarat yang tersedia", 12)
            raise ValueError
        else:
            pola_pw = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
            if not re.search(pola_pw, password):
                pesan_peringatan("Sesuaikan dengan syarat yang tersedia", 12)
                raise ValueError
            else:
                for nomor, user in akun.items():
                    if user["us"] == username:
                        pesan_peringatan("User telah tersedia", 12)
                        raise ValueError
                akun.update({
                    str(len(akun)+1): {
                        "us": username,
                        "pw": password,
                        "role": "Konsumen",
                        "status" : "Aktif",
                        "tgl" : datetime.now().strftime("%Y-%m-%d")}})
                save_akun_to_csv(akun)
                pesan_berhasil("Registrasi berhasil! Silakan login.") 
                input("→ 「 Enter untuk kembali 」")
                return True
    except ValueError:
        input("→ 「 Enter untuk kembali 」")
        return None

while True:
    jud_utama()
    jud_sub("Selamat Datang")
    questions = [
        inquirer.List(
            "menu",
            message="Pilih menu:",
            choices=[
                "1 | LOGIN",
                "2 | REGISTER",
                "3 | KELUAR"])]
    answer = inquirer.prompt(questions)["menu"]

    if answer == "1 | LOGIN":
        login()
    elif answer == "2 | REGISTER":
        register()
    elif answer == "3 | KELUAR":
        jud_utama()
        jud_sub("Terima kasih telah menggunakam program kami!")
        print("(Trauma buat nih program, help)".center(60))
        break