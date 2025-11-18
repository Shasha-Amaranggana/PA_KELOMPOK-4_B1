import inquirer
import re
from menu_bos import menu_boss
from data import akun
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
                pesan_berhasil(f"Login berhasil! Selamat datang, {username}!")
                input("→ 「 Enter untuk lanjut 」")
                if user["role"] == "bos":
                    menu_boss()
                elif user["role"] == "seller":
                    menu_seller()
                elif user["role"] == "konsumen":
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
        elif not re.search(r"^[a-zA-Z0-9]{4,}$", username):
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
                        "role": "konsumen",
                        "status" : "Aktif",
                        "tgl" : ""}})
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
                "1. Login",
                "2. Register",
                "3. Keluar"])]
    answer = inquirer.prompt(questions)["menu"]

    if answer == "1. Login":
        print("Kamu memilih Login.\n")
        login()
    elif answer == "2. Register":
        print("Kamu memilih Register.\n")
        register()
    elif answer == "3. Keluar":
        print("Program selesai. Terima kasih!")
        break