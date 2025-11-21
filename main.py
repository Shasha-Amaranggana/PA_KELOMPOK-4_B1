import inquirer
import re
from datetime import datetime
from menu_bos import menu_boss
from data import akun, save_akun_to_csv, current_seller
from help import jud_utama, jud_sub, pesan_berhasil, pesan_peringatan
from menu_konsumen import menu_konsumen
from menu_seller import menu_seller

def login():
    global current_seller
    jud_utama()
    jud_sub("Silakan Login")
    username = input("Username: ".center(45))
    password = input("Password: ".center(45))
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
                    current_seller = user
                    menu_seller(current_seller)
                    return
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
    print("   > Email harus valid dan berakhiran '@gmail.com'")
    print("   > No. HP harus valid dan berawalan '08'")
    print("")
    username = input("Username: ".center(40)).strip()
    password = input("Password: ".center(40)).strip()
    email = input("Email: ".center(40)).strip()
    no_hp = input("No HP: ".center(40)).strip()
    try:
        if username == "" or password == "" or email == "" or no_hp == "":
            pesan_peringatan("Semua kolom harus diisi!", 12)
            input("→ 「 Enter untuk kembali 」")
            return None
        for user in akun.values():
            if user["us"] == username or user["email"] == email:
                pesan_peringatan("User atau email telah tersedia", 12)
                input("→ 「 Enter untuk kembali 」")
                return None
        existing_ids = [k for k in akun.keys() if k.startswith("U_K")]
        last_num = max([int(k.split("_")[1]) for k in existing_ids], default=0)
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
                "alamat": "",
                "saldo": 0}})
        save_akun_to_csv(akun)
        pesan_berhasil(f"Anda berhasil registrasi! Silakan login.")
        input("→ 「 Enter untuk kembali 」")
        return True
    except ValueError:
        pesan_peringatan("Pastikan data yang diinput sesuai syarat!", 12)       
        input("→ 「 Enter untuk kembali 」")
        return None

while True:
    jud_utama()
    jud_sub("Selamat Datang")
    questions = [
        inquirer.List(
            "menu",
            message="Pilih menu",
            choices=[
                "1 | LOGIN".center(33),
                "2 | REGISTER".center(35),
                "3 | KELUAR".center(33)])]
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