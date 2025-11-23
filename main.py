import inquirer
import re
from datetime import datetime
from menu import menu_boss, menu_seller
from data import akun, save_akun_to_csv
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan, inp_enter
from menu_konsumen import menu_konsumen
from colorama import Fore, Style, init
init(autoreset=True)

def login():
    global current_user
    jud_utama()
    jud_sub("Silakan Login")
    username = input("Username: ".center(45))
    password = input("Password: ".center(45))
    try:
        if username == "" or password == "":
            pesan_peringatan("Semua kolom harus diisi!", Fore.YELLOW, 12)
            raise ValueError
        found = False
        for nomor, user in akun.items():
            if user["us"] == username and user["pw"] == password:
                found = True
                if user["status"].lower() != "aktif":
                    pesan_peringatan(f"Akun '{username}' saat ini {user['status']}. Tidak bisa login!", Fore. RED, 30)
                    raise ValueError
                pesan_berhasil(f"Login berhasil! Selamat datang, {username}!")
                inp_enter()
                if user["role"] == "Bos":
                    menu_boss()
                elif user["role"] == "Seller":
                    current_user = user
                    menu_seller(current_user)
                elif user["role"] == "Konsumen":
                    current_user = user
                    menu_konsumen(current_user)
                inp_enter()
                return
        if not found:
            pesan_peringatan("Username atau Password salah atau akun belum terdaftar!", Fore.RED, 27)
            raise ValueError
    except ValueError:
        inp_enter()
        return None
    
def register():
    jud_utama()
    jud_sub("Silakan Registrasi")
    print(Fore.BLUE + "  > Username min 5 karakter, mengandung huruf/angka," + Style.RESET_ALL)
    print(Fore.BLUE + "    tidak mengandung karakter spesial!" + Style.RESET_ALL)
    print(Fore.BLUE + "  > Password min 8 karakter, mengandung huruf besar & kecil & angka," + Style.RESET_ALL)
    print(Fore.BLUE + "    tidak mengandung karakter spesial!" + Style.RESET_ALL)
    print(Fore.BLUE + "  > Email harus valid dan berakhiran '@gmail.com'" + Style.RESET_ALL)
    print(Fore.BLUE + "  > No. HP harus valid dan berawalan '08'" + Style.RESET_ALL)
    print("")
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    email = input("Email: ".center(40))
    no_hp = input("No HP: ".center(40))
    alamat = input("Alamat: ".center(40))
    try:
        if username == "" or password == "" or email == "" or no_hp == "" or alamat == "":
            pesan_peringatan("Semua kolom harus diisi!", Fore.YELLOW, 12)
            inp_enter()
            return None
        if not re.search(r"^[a-zA-Z0-9]{5,}$", username):
            raise ValueError
        if not re.search(r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$", password):
            raise ValueError
        if not no_hp.startswith("08"):
            raise ValueError
        if not email.endswith("@gmail.com"):
            raise ValueError
        for user in akun.values():
            if user["us"] == username or user["email"] == email:
                pesan_peringatan("User atau email telah tersedia", Fore.RED, 12)
                raise ValueError
        existing_ids = [k for k in akun.keys() if k.startswith("U_K")]
        last_num = max([int(k.replace("U_K", "")) for k in existing_ids], default=0)
        new_id = f"U_K{last_num + 1}"
        akun.update({
            new_id: {
                "id": new_id,
                "us": username,
                "pw": password,
                "role": "Konsumen",
                "status": "Aktif",
                "tgl": datetime.now().strftime("%Y-%m-%d"),
                "email": email,
                "no_hp": no_hp,
                "alamat": alamat,
                "saldo": 0}})
        save_akun_to_csv(akun)
        pesan_berhasil("Anda berhasil registrasi! Silakan login untuk melanjutkan.")
        inp_enter()
        return True
    except ValueError:
        pesan_peringatan("Pastikan data yang diinput sesuai syarat!", Fore.YELLOW, 12)       
        inp_enter()
        return None

while True:
    jud_utama()
    jud_sub("Selamat Datang")
    questions = [
        inquirer.List(
            "menu",
            message="Silakan pilih menu",
            choices=[
                "1 | LOGIN".center(28),
                "2 | REGISTER".center(30),
                "3 | KELUAR".center(28)])]
    answer = inquirer.prompt(questions)["menu"].strip()

    if answer == "1 | LOGIN":
        login()
    elif answer == "2 | REGISTER":
        register()
    elif answer == "3 | KELUAR":
        jud_utama()
        jud_sub("Terima kasih telah menggunakam program kami!")
        print("(Trauma buat nih program, help)".center(70))
        break