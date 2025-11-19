import csv
import os

# Default akun data used when no CSV exists yet
_default_akun = {
    "1": {"us": "1", "pw": "1", "role": "bos", "status": "Aktif", "tgl": ""},
    "2": {"us": "2", "pw": "2", "role": "seller", "status": "Aktif", "tgl": ""},
    "3": {"us": "3", "pw": "3", "role": "konsumen", "status": "Aktif", "tgl": ""},
}

CSV_FILE = "users.csv"
CSV_FIELDS = ["id", "us", "pw", "role", "status", "tgl"]


def save_akun_to_csv(akun_dict: dict) -> None:
    """Write the entire akun dict to users.csv (overwrites file)."""
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        # Keep rows in numerical id order if possible
        def _key(k: str):
            try:
                return int(k)
            except Exception:
                return k
        for id_key in sorted(akun_dict.keys(), key=_key):
            user = akun_dict[id_key]
            writer.writerow({
                "id": id_key,
                "us": user.get("us", ""),
                "pw": user.get("pw", ""),
                "role": user.get("role", ""),
                "status": user.get("status", ""),
                "tgl": user.get("tgl", ""),
            })


def _append_user_to_csv(new_id: str, user: dict) -> None:
    """Append a single user to users.csv, creating file/header if needed."""
    header_needed = (not os.path.exists(CSV_FILE)) or os.path.getsize(CSV_FILE) == 0
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        if header_needed:
            writer.writeheader()
        writer.writerow({
            "id": new_id,
            "us": user.get("us", ""),
            "pw": user.get("pw", ""),
            "role": user.get("role", ""),
            "status": user.get("status", ""),
            "tgl": user.get("tgl", ""),
        })


def load_akun_from_csv() -> dict:
    """Load akun from users.csv. If missing or empty, seed with defaults to CSV."""
    if os.path.exists(CSV_FILE):
        akun_dict = {}
        with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("id"):
                    continue
                id_key = str(row["id"])  # ensure string keys
                akun_dict[id_key] = {
                    "us": row.get("us", ""),
                    "pw": row.get("pw", ""),
                    "role": row.get("role", ""),
                    "status": row.get("status", ""),
                    "tgl": row.get("tgl", ""),
                }
        if akun_dict:  # loaded real data
            return akun_dict
        # File exists but empty or only header -> seed with defaults
        save_akun_to_csv(_default_akun)
        return dict(_default_akun)
    # CSV does not exist -> seed it with defaults
    save_akun_to_csv(_default_akun)
    return dict(_default_akun)


# Initialize akun on import
try:
    akun = load_akun_from_csv()
except Exception:
    # Fallback to defaults if something goes wrong reading CSV
    akun = dict(_default_akun)
