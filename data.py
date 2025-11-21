import csv
import os

# -----------------------------
# AKUN
# -----------------------------
_default_akun = {
    "1": {"us": "1", "pw": "1", "role": "Bos", "status": "Aktif", "tgl": ""},
    "2": {"us": "2", "pw": "2", "role": "Seller", "status": "Aktif", "tgl": ""},
    "3": {"us": "3", "pw": "3", "role": "Konsumen", "status": "Aktif", "tgl": ""},
}

CSV_AKUN_FILE = "user.csv"
CSV_AKUN_FIELDS = ["id", "us", "pw", "role", "status", "tgl"]

def save_akun_to_csv(akun_dict: dict) -> None:
    with open(CSV_AKUN_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_AKUN_FIELDS)
        writer.writeheader()
        for id_key in sorted(akun_dict.keys(), key=lambda k: int(k)):
            user = akun_dict[id_key]
            writer.writerow({
                "id": id_key,
                "us": user.get("us", ""),
                "pw": user.get("pw", ""),
                "role": user.get("role", ""),
                "status": user.get("status", ""),
                "tgl": user.get("tgl", ""),
            })

def load_akun_from_csv() -> dict:
    if os.path.exists(CSV_AKUN_FILE):
        akun_dict = {}
        with open(CSV_AKUN_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("id"):
                    continue
                akun_dict[str(row["id"])] = {
                    "us": row.get("us", ""),
                    "pw": row.get("pw", ""),
                    "role": row.get("role", ""),
                    "status": row.get("status", ""),
                    "tgl": row.get("tgl", ""),
                }
        if akun_dict:
            return akun_dict
    # jika file tidak ada atau kosong
    save_akun_to_csv(_default_akun)
    return dict(_default_akun)

# Initialize akun
try:
    akun = load_akun_from_csv()
except Exception:
    akun = dict(_default_akun)

# -----------------------------
# PRODUK
# -----------------------------
CSV_PRODUK_FILE = "produk.csv"
CSV_PRODUK_FIELDS = ["id", "varian", "kemasan", "harga", "status", "tgl"]

_default_produk = [
    {"id": "1", "varian": "Blueberry", "kemasan": "Large", "harga": 18000, "status": "Tersedia", "tgl": ""},
    {"id": "2", "varian": "Blueberry", "kemasan": "Medium", "harga": 15000, "status": "Tersedia", "tgl": ""},
    {"id": "3", "varian": "Blueberry", "kemasan": "Small", "harga": 10000, "status": "Tersedia", "tgl": ""},
]

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
                produk_list.append({
                    "id": row.get("id", ""),
                    "varian": row.get("varian", ""),
                    "kemasan": row.get("kemasan", ""),
                    "harga": int(row.get("harga", 0)),
                    "status": row.get("status", ""),
                    "tgl": row.get("tgl", ""),
                })
        if produk_list:
            return produk_list
    # jika file tidak ada atau kosong
    save_produk_to_csv(_default_produk)
    return list(_default_produk)

# Initialize produk
try:
    produk_list = load_produk_from_csv()
except Exception:
    produk_list = list(_default_produk)