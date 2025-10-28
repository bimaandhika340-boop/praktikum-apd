import os
import time

#  VARIABEL GLOBAL 
DATA_PENGGUNA = {"andhika": "150407", "tamu": "12345", "admin": "108"}
STOK_SEPATU = {
    "Sneakers Basic": 250000,
    "Running Pro": 400000,
    "Casual Street": 350000,
    "Formal Leather": 500000,
}
riwayat_transaksi = []  # Menyimpan semua transaksi
login_user = None       # Menyimpan user yang sedang login


# =================== FUNGSI & PROSEDUR ===================

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# === Fungsi Register Akun Baru ===
def register():
    global DATA_PENGGUNA
    clear_screen()
    print("\n=== REGISTER AKUN BARU ===")
    username = input("Masukkan username: ")

    if username in DATA_PENGGUNA:
        print("Username sudah terdaftar!")
        return

    password = input("Masukkan password: ")
    DATA_PENGGUNA[username] = password
    print("Akun Berhasil Ditambahkan")
    print(f"Akun {username} berhasil dibuat! Silakan login untuk melanjutkan.\n")


# === Fungsi & Prosedur Menu Utama ===
def tampilkan_menu():
    print("\n=== MENU TOKO SEPATUKU ===")
    print("1. Lihat Daftar Sepatu")
    print("2. Beli Sepatu")
    print("3. Lihat Riwayat Transaksi")
    print("4. Logout")


def hitung_total(harga, jumlah):
    try:
        return harga * jumlah
    except TypeError:
        print("Error: Input jumlah atau harga tidak valid!")
        return 0


def tampilkan_sepatu():
    print("\n=== DAFTAR SEPATU ===")
    for i, (nama, harga) in enumerate(STOK_SEPATU.items(), start=1):
        print(f"{i}. {nama} - Rp {harga:,}")


def simpan_transaksi(nama_sepatu, jumlah, total):
    global riwayat_transaksi
    transaksi = {
        "pembeli": login_user,
        "sepatu": nama_sepatu,
        "jumlah": jumlah,
        "total": total,
        "waktu": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    riwayat_transaksi.append(transaksi)


def login(percobaan=3):
    global login_user
    if percobaan == 0:
        print("Terlalu banyak percobaan! Keluar program...")
        return False

    print("\n=== LOGIN TOKO SEPATUKU ===")
    username = input("Masukkan Username: ")
    password = input("Masukkan Password: ")

    if username in DATA_PENGGUNA and DATA_PENGGUNA[username] == password:
        login_user = username
        print(f"\nLogin berhasil! Selamat datang, {login_user}.")
        return True
    else:
        print("Username atau password salah!")
        return login(percobaan - 1)


def lihat_riwayat():
    if len(riwayat_transaksi) == 0:
        print("\nBelum ada transaksi.")
    else:
        print("\n=== RIWAYAT TRANSAKSI ===")
        for t in riwayat_transaksi:
            print(
                f"[{t['waktu']}] {t['pembeli']} membeli {t['jumlah']} {t['sepatu']} total Rp {t['total']:,}"
            )


# =================== MENU ADMIN: DATA PELANGGAN ===================
def kelola_data_pelanggan():
    global DATA_PENGGUNA
    while True:
        print("\n=== MENU DATA PELANGGAN ===")
        print("1. Lihat Semua Pelanggan")
        print("2. Tambah Pelanggan Baru")
        print("3. Ubah Data Pelanggan")
        print("4. Hapus Pelanggan")
        print("5. Kembali ke Menu Utama")
        try:
            pilih = int(input("Pilih menu (1-5): "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilih == 1:
            if len(DATA_PENGGUNA) == 0:
                print("Belum ada data pelanggan.")
            else:
                print("\n=== DAFTAR PELANGGAN ===")
                for i, (user, pw) in enumerate(DATA_PENGGUNA.items(), start=1):
                    print(f"{i}. Username: {user} | Password: {pw}")

        elif pilih == 2:
            print("\n=== TAMBAH PELANGGAN BARU ===")
            username = input("Masukkan username baru: ")
            if username in DATA_PENGGUNA:
                print("Username sudah terdaftar!")
            else:
                password = input("Masukkan password: ")
                DATA_PENGGUNA[username] = password
                print(f"Pelanggan {username} berhasil ditambahkan.")

        elif pilih == 3:
            print("\n=== UBAH DATA PELANGGAN ===")
            username = input("Masukkan username yang ingin diubah: ")
            if username in DATA_PENGGUNA:
                password_baru = input("Masukkan password baru: ")
                DATA_PENGGUNA[username] = password_baru
                print(f"Password pelanggan '{username}' berhasil diubah.")
            else:
                print("Pelanggan tidak ditemukan.")

        elif pilih == 4:
            print("\n=== HAPUS DATA PELANGGAN ===")
            username = input("Masukkan username yang ingin dihapus: ")
            if username in DATA_PENGGUNA:
                konfirmasi = input(f"Yakin ingin menghapus {username}? (y/n): ").lower()
                if konfirmasi == "y":
                    del DATA_PENGGUNA[username]
                    print(f"Pelanggan '{username}' berhasil dihapus.")
                else:
                    print("Penghapusan dibatalkan.")
            else:
                print("Pelanggan tidak ditemukan.")

        elif pilih == 5:
            break
        else:
            print("Pilihan tidak tersedia!")


# =================== PROGRAM UTAMA ===================
def main():
    global login_user
    clear_screen()

    while True:
        print("=== SELAMAT DATANG DI TOKO SEPATUKU ===")
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        try:
            menu_awal = int(input("Pilih menu (1-3): "))
        except ValueError:
            print("Input harus berupa angka!\n")
            continue

        if menu_awal == 1:
            if not login():
                return
            break
        elif menu_awal == 2:
            register()
        elif menu_awal == 3:
            print("Terima kasih! Program selesai.\n")
            return
        else:
            print("Pilihan tidak valid!\n")

    while True:
        tampilkan_menu()
        try:
            pilihan = int(input("Pilih menu (1-4): "))
        except ValueError:
            print("Input harus berupa angka!")
            continue

        if pilihan == 1:
            tampilkan_sepatu()

        elif pilihan == 2:
            tampilkan_sepatu()
            try:
                pilihan_sepatu = int(input("Pilih nomor sepatu: "))
                nama_sepatu = list(STOK_SEPATU.keys())[pilihan_sepatu - 1]
                harga = STOK_SEPATU[nama_sepatu]
                jumlah = int(input("Masukkan jumlah: "))

                total = hitung_total(harga, jumlah)
                simpan_transaksi(nama_sepatu, jumlah, total)
                print(f"Total harga: Rp {total:,}")
                print("Transaksi berhasil!")

            except (ValueError, IndexError):
                print("Input tidak valid, silakan ulangi!")

        elif pilihan == 3:
            lihat_riwayat()

        elif pilihan == 4:
            print(f"Terima kasih, {login_user}! Anda telah logout.\n")
            login_user = None
            break

        else:
            print("Pilihan tidak tersedia!")

        # === MENU TAMBAHAN KHUSUS ADMIN ===
        if login_user == "admin":
            print("\n=== MENU ADMIN ===")
            print("a. Tambah Sepatu Baru")
            print("b. Kelola Data Pelanggan")
            print("c. Kembali ke Menu Utama")
            admin_choice = input("Pilih: ").lower()
            if admin_choice == "a":
                nama_baru = input("Masukkan nama sepatu baru: ")
                try:
                    harga_baru = int(input("Masukkan harga sepatu: "))
                    STOK_SEPATU[nama_baru] = harga_baru
                    print(f"Sepatu {nama_baru} berhasil ditambahkan.")
                except ValueError:
                    print("Harga harus berupa angka!")
            elif admin_choice == "b":
                kelola_data_pelanggan()
            elif admin_choice == "c":
                continue


# Jalankan program
if __name__ == "__main__":
    main()
