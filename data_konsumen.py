keranjang_user = {
    "owen": {
        "1": { "nm": "popcorn1", "sz": "L", "pz": 25000, "jumlah": 2 },
        "3": { "nm": "popcorn3", "sz": "S", "pz": 15000, "jumlah": 1 }}}


def init_keranjang_user(current_user):
    if current_user not in keranjang_user:
        keranjang_user[current_user] = {}

pesanan = {}

riwayat = {}

rating = {}
