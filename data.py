import csv
import os

# AKUN
# ════════════════════════════════════════════════════
_default_akun = {
    "U_B1": {"id": "U_B1", "us": "1", "pw": "1", "role": "Bos", "status": "Aktif", "tgl": "2025-10-10", "email": "Shaasha04@gmail.com", "no_hp": "081348861965", "alamat": "Jalan Durian", "saldo": 0},
    "U_S1": {"id": "U_S1", "us": "2", "pw": "2", "role": "Seller", "status": "Aktif", "tgl": "2025-10-10", "email": "Kanja34@gmail.com", "no_hp": "081234567890", "alamat": "Jalan Anggur", "saldo": 0},
    "U_K1": {"id": "U_K1", "us": "3", "pw": "3", "role": "Konsumen", "status": "Aktif", "tgl": "2025-10-10", "email": "Owenn00@gmail.com", "no_hp": "080987654321", "alamat": "Jalan Mangga", "saldo": 0},
    }

CSV_AKUN_FILE = "user.csv"
CSV_AKUN_FIELDS = ["id", "us", "pw", "role", "status", "tgl", "email", "no_hp", "alamat", "saldo"]

def save_akun_to_csv(akun_dict: dict) -> None:
    with open(CSV_AKUN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_AKUN_FIELDS)
        writer.writeheader()
        for id_key in sorted(akun_dict.keys()):
            user = akun_dict[id_key]
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
    current_seller = None
    current_konsume = None
except Exception:
    akun = dict(_default_akun)


# PRODUK
# ════════════════════════════════════════════════════

CSV_PRODUK_FILE = "produk.csv"
CSV_PRODUK_FIELDS = ["id", "varian", "kemasan", "harga", "stok", "status", "tgl"]

_default_produk = [
    {"id": "C1", "varian": "Caramel", "kemasan": "Small", "harga": 5000, "stok": 15, "status": "Tersedia", "tgl": ""},
    {"id": "C2", "varian": "Caramel", "kemasan": "Medium", "harga": 10000, "stok": 25, "status": "Tersedia", "tgl": ""},
    {"id": "C3", "varian": "Caramel", "kemasan": "Large", "harga": 18000, "stok": 0, "status": "Habis", "tgl": ""},
    {"id": "B1", "varian": "Blueberry", "kemasan": "Small", "harga": 5000, "stok": 35, "status": "Tersedia", "tgl": ""},
    {"id": "B2", "varian": "Blueberry", "kemasan": "Medium", "harga": 10000, "stok": 10, "status": "Tersedia", "tgl": ""},
    {"id": "B3", "varian": "Blueberry", "kemasan": "Large", "harga": 18000, "stok": 20, "status": "Tersedia", "tgl": ""},
    {"id": "M1", "varian": "Matcha", "kemasan": "Small", "harga": 5000, "stok": 30, "status": "Tersedia", "tgl": ""},
    {"id": "M2", "varian": "Matcha", "kemasan": "Medium", "harga": 10000, "stok": 45, "status": "Tersedia", "tgl": ""},
    {"id": "M3", "varian": "Matcha", "kemasan": "Large", "harga": 18000, "stok": 40, "status": "Tersedia", "tgl": ""},]

def save_produk_to_csv(produk_list: list) -> None:
    with open(CSV_PRODUK_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_PRODUK_FIELDS)
        writer.writeheader()
        for p in produk_list:
            writer.writerow(p)

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
                    "status": status,
                    "tgl": row.get("tgl", ""),})
        if produk_list:
            return produk_list
    save_produk_to_csv(_default_produk)
    return list(_default_produk)

try:
    produk_list = load_produk_from_csv()
except Exception:
    produk_list = list(_default_produk)
