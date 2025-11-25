import csv
import os

# AKUN
# ════════════════════════════════════════════════════
CSV_AKUN_FILE = "user.csv"
CSV_AKUN_FIELDS = ["id", "us", "pw", "role", "status", "tgl", "email", "no_hp", "alamat", "saldo"]

_default_akun = {
    "U_B1": {"id": "U_B1", "us": "Shasha", "pw": "1", "role": "Bos", "status": "Aktif", "tgl": "2025-10-10", "email": "Shaasha04@gmail.com", "no_hp": "081348861965", "alamat": "Jalan Durian", "saldo": 0},
    "U_S1": {"id": "U_S1", "us": "Kanja", "pw": "2", "role": "Seller", "status": "Aktif", "tgl": "2025-10-10", "email": "Kanja34@gmail.com", "no_hp": "081234567890", "alamat": "Jalan Anggur", "saldo": 0},
    "U_K1": {"id": "U_K1", "us": "Owen", "pw": "3", "role": "Konsumen", "status": "Aktif", "tgl": "2025-10-10", "email": "Owenn00@gmail.com", "no_hp": "080987654321", "alamat": "Jalan Mangga", "saldo": 0},
    }

def save_akun_to_csv(akun_dict: dict) -> None:
    with open(CSV_AKUN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_AKUN_FIELDS)
        writer.writeheader()
        for id_key in sorted(akun_dict.keys()):
            user = akun_dict[id_key]
            if not isinstance(user, dict):
                continue
            writer.writerow({
                "id": user.get("id", id_key),
                "us": user.get("us", ""),
                "pw": user.get("pw", ""),
                "role": user.get("role", ""),
                "status": user.get("status", ""),
                "tgl": user.get("tgl", ""),
                "email": user.get("email", ""),
                "no_hp": user.get("no_hp", ""),
                "alamat": user.get("alamat", ""),
                "saldo": user.get("saldo", 0),})

def load_akun_from_csv() -> dict:
    if os.path.exists(CSV_AKUN_FILE):
        akun_dict = {}
        with open(CSV_AKUN_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("id"):
                    continue
                akun_dict[str(row["id"])] = {
                    "id": row.get("id", ""),
                    "us": row.get("us", ""),
                    "pw": row.get("pw", ""),
                    "role": row.get("role", ""),
                    "status": row.get("status", ""),
                    "tgl": row.get("tgl", ""),
                    "email": row.get("email", ""),
                    "no_hp": row.get("no_hp", ""),
                    "alamat": row.get("alamat", ""),
                    "saldo": int(row.get("saldo", 0))}
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
CSV_PRODUK_FIELDS = ["id", "varian", "kemasan", "harga", "stok"]

_default_produk = [
    {"id": "C1", "varian": "Caramel", "kemasan": "Small", "harga": 5000, "stok": 15, "status" : "Tersedia"},
    {"id": "C2", "varian": "Caramel", "kemasan": "Medium", "harga": 10000, "stok": 25, "status" : "Tersedia"},
    {"id": "C3", "varian": "Caramel", "kemasan": "Large", "harga": 18000, "stok": 0, "status" : "Habis"},
    {"id": "B1", "varian": "Blueberry", "kemasan": "Small", "harga": 5000, "stok": 35, "status" : "Tersedia"},
    {"id": "B2", "varian": "Blueberry", "kemasan": "Medium", "harga": 10000, "stok": 10, "status" : "Tersedia"},
    {"id": "B3", "varian": "Blueberry", "kemasan": "Large", "harga": 18000, "stok": 20, "status" : "Tersedia"},
    {"id": "M1", "varian": "Matcha", "kemasan": "Small", "harga": 5000, "stok": 30, "status" : "Tersedia"},
    {"id": "M2", "varian": "Matcha", "kemasan": "Medium", "harga": 10000, "stok": 45, "status" : "Tersedia"},
    {"id": "M3", "varian": "Matcha", "kemasan": "Large", "harga": 18000, "stok": 40, "status" : "Tersedia"}]

def save_produk_to_csv(produk_list: list) -> None:
    with open(CSV_PRODUK_FILE, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "varian", "kemasan", "harga", "stok", "status"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for produk in produk_list:
            writer.writerow({
                "id": produk.get("id", ""),
                "varian": produk.get("varian", ""),
                "kemasan": produk.get("kemasan", ""),
                "harga": produk.get("harga", 0),
                "stok": produk.get("stok", 0),
                "status": produk.get("status", "")})

def load_produk_from_csv() -> list:
    if os.path.exists(CSV_PRODUK_FILE):
        produk_list = []
        with open(CSV_PRODUK_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("id"):
                    continue
                stok = int(row.get("stok", 0))
                status = "Tersedia" if stok > 0 else "Habis"
                produk_list.append({
                    "id": row.get("id", ""),
                    "varian": row.get("varian", ""),
                    "kemasan": row.get("kemasan", ""),
                    "harga": int(row.get("harga", 0)),
                    "stok": stok,
                    "status": status,})
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
CSV_PEMBELIAN_FIELDS = ["id_order", "id_produk", "varian", "kemasan", "harga", "id_user", "tanggal_pesan", "tanggal_dikirim", "tanggal_sampai", "jumlah", "total_harga", "status", "batal_oleh", "alasan"]

_default_pembelian = {
    "U_B1": [
        {"id_order": "O1", "id_produk": "C1", "varian": "Caramel", "kemasan": "Medium", "harga": 10000, "id_user": "U_B1", "tanggal_pesan": "2025-10-10", "tanggal_dikirim": "", "tanggal_sampai": "", "jumlah": 1, "total_harga": 10000, "status": "Dipesan", "batal_oleh": "", "alasan": ""}]}

def save_pembelian_to_csv(pembelian_dict: dict) -> None:
    with open(CSV_PEMBELIAN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_PEMBELIAN_FIELDS)
        writer.writeheader()
        for id_user, items in pembelian_dict.items():
            for item in items:
                writer.writerow({
                    "id_order": item.get("id_order", ""),
                    "id_produk": item.get("id_produk", ""),
                    "varian": item.get("varian", ""),
                    "kemasan": item.get("kemasan", ""),
                    "harga": item.get("harga", 0),
                    "id_user": id_user,
                    "tanggal_pesan": item.get("tanggal_pesan", ""),
                    "tanggal_dikirim": item.get("tanggal_dikirim", ""),
                    "tanggal_sampai": item.get("tanggal_sampai", ""),
                    "jumlah": item.get("jumlah", 0),
                    "total_harga": item.get("total_harga", 0),
                    "status": item.get("status", ""),
                    "batal_oleh": item.get("batal_oleh", ""),
                    "alasan": item.get("alasan", "")})

def load_pembelian_from_csv() -> dict:
    pembelian_dict = {}
    if os.path.exists(CSV_PEMBELIAN_FILE):
        with open(CSV_PEMBELIAN_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_user = row.get("id_user", "")
                if not id_user:
                    continue
                if id_user not in pembelian_dict:
                    pembelian_dict[id_user] = []
                pembelian_dict[id_user].append({
                    "id_order": row.get("id_order", ""),
                    "id_produk": row.get("id_produk", ""),
                    "varian": row.get("varian", ""),
                    "kemasan": row.get("kemasan", ""),
                    "harga": int(row.get("harga", 0)),
                    "tanggal_pesan": row.get("tanggal_pesan", ""),
                    "tanggal_dikirim": row.get("tanggal_dikirim", ""),
                    "tanggal_sampai": row.get("tanggal_sampai", ""),
                    "jumlah": int(row.get("jumlah", 0)),
                    "total_harga": int(row.get("total_harga", 0)),
                    "status": row.get("status", ""),
                    "batal_oleh": row.get("batal_oleh", ""),
                    "alasan": row.get("alasan", "")})
                
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
CSV_KERANJANG_FIELDS = ["id_user", "id_produk", "varian", "kemasan", "harga"]

_default_keranjang = {
    "U_B1": [
        {"id_produk": "C1", "varian": "Caramel", "kemasan": "Medium", "harga": 10000}]}

def save_keranjang_to_csv(keranjang_dict: dict) -> None:
    with open(CSV_KERANJANG_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_KERANJANG_FIELDS)
        writer.writeheader()
        for id_user, items in keranjang_dict.items():
            for item in items:
                writer.writerow({
                    "id_user": id_user,
                    "id_produk": item.get("id_produk", ""),
                    "varian": item.get("varian", ""),
                    "kemasan": item.get("kemasan", ""),
                    "harga": item.get("harga", 0)})

def load_keranjang_from_csv() -> dict:
    keranjang_dict = {}
    if os.path.exists(CSV_KERANJANG_FILE):
        with open(CSV_KERANJANG_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                id_user = row.get("id_user", "")
                if not id_user:
                    continue
                if id_user not in keranjang_dict:
                    keranjang_dict[id_user] = []
                keranjang_dict[id_user].append({
                    "id_produk": row.get("id_produk", ""),
                    "varian": row.get("varian", ""),
                    "kemasan": row.get("kemasan", ""),
                    "harga": int(row.get("harga", 0))})
        if keranjang_dict:
            return keranjang_dict
    save_keranjang_to_csv(_default_keranjang)
    return dict(_default_keranjang)

try:
    keranjang = load_keranjang_from_csv()
except Exception:
    keranjang = dict(_default_keranjang)
