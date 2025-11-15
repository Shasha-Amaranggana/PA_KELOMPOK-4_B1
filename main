import inquirer
import re
import menu_bos

print("haloo bang")

akun = {
    "1" : {"us" : "1", "pw" : "1", "role" : "bos"},
    "2" : {"us" : "2", "pw" : "2", "role" : "seller"},
    "3" : {"us" : "3", "pw" : "3", "role" : "konsumen"}}

def login():
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if username == "" or password == "":
            raise ValueError
        for nomor, user in akun.items():
            if user["us"] == username and user["pw"] == password:
                if user["role"] == "bos":
                    menu_bos()
                elif user["role"] == "seller":
                    menu_seller()
                else:
                    menu_konsumen()
        raise ValueError
    except ValueError:
        input("→ 「 Enter untuk kembali 」")
        return None
    
def register():
    print("   > Username min 5 karakter, mengandung huruf/angka,")
    print("     tidak mengandung karakter spesial!")
    print("   > Password min 8 karakter, mengandung huruf besar & kecil & angka,")
    print("     tidak mengandung karakter spesial!")
    print("")
    username = input("Username: ".center(40))
    password = input("Password: ".center(40))
    try:
        if username == "" or password == "":
            raise ValueError
        elif not re.search(r"^[a-zA-Z0-9]{4,}$", username):
            raise ValueError
        else:
            pola_pw = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
            if not re.search(pola_pw, password):
                raise ValueError
            else:
                for nomor, user in akun.items():
                    if user["us"] == username:
                        raise ValueError
                akun.update({
                    str(len(akun)+1): {
                        "us": username,
                        "pw": password,
                        "st": "konsumen"}})
                input("→ 「 Enter untuk kembali 」")
                return True
    except ValueError:
        input("→ 「 Enter untuk kembali 」")
        return None

def menu_seller():
    while True:
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu seller:",
                choices=[
                    "1. Akun",
                    "2. Daftar Produk",
                    "3. Logout"])]
        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Akun":
            print("Akun")
        elif answer == "2. Daftar Produk":
            print("Daftar Produk")
        elif answer == "3. Logout":
            break

def menu_konsumen():
    while True:
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu konsumen:",
                choices=[
                    "1. Akun",
                    "2. Daftar Produk",
                    "3. Logout"])]
        answer = inquirer.prompt(questions)["menu"]

        if answer == "1. Akun":
            print("Akun")
        elif answer == "2. Daftar Produk":
            print("Daftar Produk")
        elif answer == "3. Logout":
            break

while True:
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