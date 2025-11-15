import inquirer

def menu_boss():
    while True:
        questions = [
            inquirer.List(
                "menu",
                message="Pilih menu:",
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