import csv
import os


# AKUN
# ════════════════════════════════════════════════════
CSV_AKUN_FILE = "user.csv"
CSV_AKUN_FIELDS = ["id_user", "us", "pw", "role", "status_user", "tanggal_daftar", "email", "no_hp", "alamat", "saldo"]

_default_akun = {
    "U_B1": {"id_user": "U_B1", "us": "Shasha11", "pw": "Shasha11", "role": "Bos", "status_user": "Aktif", "tanggal_daftar": "2025-10-10", "email": "Shaasha11@gmail.com", "no_hp": "081348861965", "alamat": "Jalan Durian", "saldo": 0},
    "U_S1": {"id_user": "U_S1", "us": "Kanja22", "pw": "Kanjaa22", "role": "Seller", "status_user": "Aktif", "tanggal_daftar": "2025-10-10", "email": "Kanja22@gmail", "no_hp": "083812518903", "alamat": "Jalan Markisa", "saldo": 0},
    "U_K1": {"id_user": "U_K1", "us": "Owen33", "pw": "Owennn33", "role": "Konsumen", "status_user": "Aktif", "tanggal_daftar": "2025-10-10", "email": "Owenn33@gmail.com", "no_hp": "085248494138", "alamat": "Jalan Mangga", "saldo": 0},}

def save_akun_to_csv(akun_dict: dict) -> None:
    with open(CSV_AKUN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_AKUN_FIELDS)
        writer.writeheader()
        for id_key in sorted(akun_dict.keys()):
            user = akun_dict[id_key]
            if not isinstance(user, dict):
                continue
            writer.writerow({
                "id_user": user.get("id_user", id_key),
                "us": user.get("us",""),
                "pw": user.get("pw",""),
                "role": user.get("role",""),
                "status_user": user.get("status_user",""),
                "tanggal_daftar": user.get("tanggal_daftar",""),
                "email": user.get("email",""),
                "no_hp": user.get("no_hp",""),
                "alamat": user.get("alamat",""),
                "saldo": int(user.get("saldo", 0)),})

def load_akun_from_csv() -> dict:
    if os.path.exists(CSV_AKUN_FILE):
        akun_dict = {}
        with open(CSV_AKUN_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for user in reader:
                if not user.get("id_user"):
                    continue
                akun_dict[str(user["id_user"])] = {
                    "id_user": user.get("id_user",""),
                    "us": user.get("us",""),
                    "pw": user.get("pw",""),
                    "role": user.get("role",""),
                    "status_user": user.get("status_user",""),
                    "tanggal_daftar": user.get("tanggal_daftar",""),
                    "email": user.get("email",""),
                    "no_hp": user.get("no_hp",""),
                    "alamat": user.get("alamat",""),
                    "saldo": int(user.get("saldo", 0)),}
        if akun_dict:
            return akun_dict
    save_akun_to_csv(_default_akun)
    return dict(_default_akun)

try:
    akun = load_akun_from_csv()
    current_user = None
except Exception:
    akun = dict(_default_akun)


# PRODUK
# ════════════════════════════════════════════════════

CSV_PRODUK_FILE = "produk.csv"
CSV_PRODUK_FIELDS = ["id_produk", "varian", "kemasan", "harga", "stok", "status_produk"]

_default_produk = [
    {"id_produk": "C1", "varian": "Caramel", "kemasan": "Small", "harga": 5000, "stok": 15, "status_produk" : "Tersedia"},
    {"id_produk": "C2", "varian": "Caramel", "kemasan": "Medium", "harga": 10000, "stok": 25, "status_produk" : "Tersedia"},
    {"id_produk": "C3", "varian": "Caramel", "kemasan": "Large", "harga": 18000, "stok": 0, "status_produk" : "Habis"},
    {"id_produk": "B1", "varian": "Blueberry", "kemasan": "Small", "harga": 5000, "stok": 35, "status_produk" : "Tersedia"},
    {"id_produk": "B2", "varian": "Blueberry", "kemasan": "Medium", "harga": 10000, "stok": 10, "status_produk" : "Tersedia"},
    {"id_produk": "B3", "varian": "Blueberry", "kemasan": "Large", "harga": 18000, "stok": 20, "status_produk" : "Tersedia"},
    {"id_produk": "M1", "varian": "Matcha", "kemasan": "Small", "harga": 5000, "stok": 30, "status_produk" : "Tersedia"},
    {"id_produk": "M2", "varian": "Matcha", "kemasan": "Medium", "harga": 10000, "stok": 45, "status_produk" : "Tersedia"},
    {"id_produk": "M3", "varian": "Matcha", "kemasan": "Large", "harga": 18000, "stok": 40, "status_produk" : "Tersedia"}]

def save_produk_to_csv(produk_list: list) -> None:
    with open(CSV_PRODUK_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_PRODUK_FIELDS)
        writer.writeheader()
        for produk in produk_list:
            writer.writerow({
                "id_produk": produk.get("id_produk",""),
                "varian": produk.get("varian",""),
                "kemasan": produk.get("kemasan",""),
                "harga": produk.get("harga", 0),
                "stok": produk.get("stok", 0),
                "status_produk": produk.get("status_produk",""),})

def load_produk_from_csv() -> list:
    if os.path.exists(CSV_PRODUK_FILE):
        produk_list = []
        with open(CSV_PRODUK_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for product in reader:
                if not product.get("id_produk"):
                    continue
                stok = int(product.get("stok", 0))
                status = "Tersedia" if stok > 0 else "Habis"
                produk_list.append({
                    "id_produk": product.get("id_produk",""),
                    "varian": product.get("varian",""),
                    "kemasan": product.get("kemasan",""),
                    "harga": int(product.get("harga", 0)),
                    "stok": stok,
                    "status_produk": status,})
        if produk_list:
            return produk_list
    save_produk_to_csv(_default_produk)
    return list(_default_produk)

try:
    produk_list = load_produk_from_csv()
except Exception:
    produk_list = list(_default_produk)



# PEMBELIAN
# ════════════════════════════════════════════════════

CSV_PEMBELIAN_FILE = "pembelian.csv"
CSV_PEMBELIAN_FIELDS = ["id_order", "id_produk", "varian", "kemasan", "harga", "id_user", "tanggal_pesan", "tanggal_dikirim", "tanggal_sampai", "jumlah", "total_harga", "status_order", "batal_oleh", "alasan"]

_default_pembelian = {
    "U_B1": [
        {"id_order": "O1", "id_produk": "C1", "varian": "Caramel", "kemasan": "Small", "harga": 5000, "id_user": "U_B1", "tanggal_pesan": "2025-10-10", "tanggal_dikirim": "", "tanggal_sampai": "", "jumlah": 2, "total_harga": 10000, "status_order": "Dipesan", "batal_oleh": "", "alasan": ""}]}

def save_pembelian_to_csv(pembelian_dict: dict) -> None:
    with open(CSV_PEMBELIAN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_PEMBELIAN_FIELDS)
        writer.writeheader()
        for id_user, items in pembelian_dict.items():
            for item in items:
                writer.writerow({
                    "id_order": item.get("id_order",""),
                    "id_produk": item.get("id_produk",""),
                    "varian": item.get("varian",""),
                    "kemasan": item.get("kemasan",""),
                    "harga": item.get("harga", 0),
                    "id_user": id_user,
                    "tanggal_pesan": item.get("tanggal_pesan", ""),
                    "tanggal_dikirim": item.get("tanggal_dikirim", ""),
                    "tanggal_sampai": item.get("tanggal_sampai", ""),
                    "jumlah": item.get("jumlah", 0),
                    "total_harga": item.get("total_harga", 0),
                    "status_order": item.get("status_order",""),
                    "batal_oleh": item.get("batal_oleh",""),
                    "alasan": item.get("alasan", "")})

def load_pembelian_from_csv() -> dict:
    pembelian_dict = {}
    if os.path.exists(CSV_PEMBELIAN_FILE):
        with open(CSV_PEMBELIAN_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for item in reader:
                id_user = item.get("id_user", "")
                if not id_user:
                    continue
                if id_user not in pembelian_dict:
                    pembelian_dict[id_user] = []
                pembelian_dict[id_user].append({
                    "id_order": item.get("id_order",""),
                    "id_produk": item.get("id_produk",""),
                    "varian": item.get("varian",""),
                    "kemasan": item.get("kemasan",""),
                    "harga": int(item.get("harga", 0)),
                    "tanggal_pesan": item.get("tanggal_pesan", ""),
                    "tanggal_dikirim": item.get("tanggal_dikirim", ""),
                    "tanggal_sampai": item.get("tanggal_sampai", ""),
                    "jumlah": int(item.get("jumlah", 0)),
                    "total_harga": int(item.get("total_harga", 0)),
                    "status_order": item.get("status_order",""),
                    "batal_oleh": item.get("batal_oleh",""),
                    "alasan": item.get("alasan", "")})
        if pembelian_dict:
            return pembelian_dict
    save_pembelian_to_csv(_default_pembelian)
    return dict(_default_pembelian)

try:
    pembelian = load_pembelian_from_csv()
except Exception:
    pembelian = dict(_default_pembelian)



# KERANJANG
# ════════════════════════════════════════════════════

CSV_KERANJANG_FILE = "keranjang.csv"
CSV_KERANJANG_FIELDS = ["id_user", "id_produk", "varian", "kemasan", "harga", "jumlah"]

_default_keranjang = {
    "U_B1": [
        {"id_produk": "C1", "varian": "Caramel", "kemasan": "Medium", "harga": 10000, "jumlah": 1}],}

def save_keranjang_to_csv(keranjang_dict: dict) -> None:
    with open(CSV_KERANJANG_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_KERANJANG_FIELDS)
        writer.writeheader()
        for id_user, items in keranjang_dict.items():
            for item in items:
                writer.writerow({
                    "id_user": id_user,
                    "id_produk": item.get("id_produk",""),
                    "varian": item.get("varian",""),
                    "kemasan": item.get("kemasan",""),
                    "harga": int(item.get("harga", 0)),
                    "jumlah": int(item.get("jumlah", 0)),})

def load_keranjang_from_csv() -> dict:
    keranjang_dict = {}
    if os.path.exists(CSV_KERANJANG_FILE):
        with open(CSV_KERANJANG_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for item in reader:
                id_user = item.get("id_user", "")
                if not id_user:
                    continue
                if id_user not in keranjang_dict:
                    keranjang_dict[id_user] = []
                keranjang_dict[id_user].append({
                    "id_user": id_user,
                    "id_produk": item.get("id_produk", ""),
                    "varian": item.get("varian", ""),
                    "kemasan": item.get("kemasan", ""),
                    "harga": int(item.get("harga", 0)),
                    "jumlah": int(item.get("jumlah", 0))})
        if keranjang_dict:
            return keranjang_dict
    save_keranjang_to_csv(_default_keranjang)
    return dict(_default_keranjang)

try:
    keranjang = load_keranjang_from_csv()
except Exception:
    keranjang = dict(_default_keranjang)
