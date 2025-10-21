    import os

# =========================================================
# === DATA DASAR AKUN
# =========================================================
akun = {
    "andhikaaa": "123456",  # admin
    "andhika": "12345"      # guest
}

akun_tambahan = {}

# =========================================================
# === DAFTAR PAKET / PRODUK (SEPATU)
# =========================================================
paket_sepatu = {
    "1": {"nama": "Sneakers Basic", "stok": 1, "harga": 250000},
    "2": {"nama": "Running Pro", "stok": 1, "harga": 400000},
    "3": {"nama": "Casual Street", "stok": 1, "harga": 350000},
    "4": {"nama": "Formal Leather", "stok": 1, "harga": 500000},
    "5": {"nama": "Anak Sekolah", "stok": 1, "harga": 200000}
}

# =========================================================
# === DATA PEMBELI
# =========================================================
data_pembeli = {}

# =========================================================
# === MENU UTAMA (LOGIN / REGISTER / KELUAR)
# =========================================================
while True:
    os.system('cls')
    print("=== SISTEM MANAJEMEN TOKO SEPATU ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")

    pilih_awal = input("Pilih menu: ")

    # =====================================================
    # === FITUR REGISTER AKUN BARU
    # =====================================================
    if pilih_awal == "2":
        os.system('cls')
        print("=== REGISTER AKUN BARU ===")
        new_user = input("Masukkan username baru: ")
        new_pass = input("Masukkan password baru: ")

        if new_user in akun or new_user in akun_tambahan:
            print("Username sudah terdaftar! Silakan coba lagi.")
        else:
            akun_tambahan[new_user] = new_pass
            print("Akun berhasil dibuat! Silakan login menggunakan akun baru.")

        input("\nTekan Enter untuk kembali ke menu awal...")

    # =====================================================
    # === FITUR LOGIN
    # =====================================================
    elif pilih_awal == "1":
        os.system('cls')
        print("=== LOGIN SISTEM TOKO SEPATU ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        login = False
        is_admin = False

        if username in akun and akun[username] == password:
            login = True
            if username == "andhikaaa":
                is_admin = True
        elif username in akun_tambahan and akun_tambahan[username] == password:
            login = True

        if not login:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
            continue

        print("Login berhasil!\n")

        # =================================================
        # === MENU UTAMA SETELAH LOGIN
        # =================================================
        while login:
            os.system('cls')
            print("=== MENU UTAMA ===")
            print("1. Tambah Data Pembeli (Create)")
            print("2. Lihat Data Pembeli (Read)")
            if is_admin:
                print("3. Ubah Data Pembeli (Update)")
                print("4. Hapus Data Pembeli (Delete)")
            print("5. Lihat Daftar Sepatu")
            print("6. Logout")

            menu = input("Pilih menu: ")

            # =============================================
            # === FITUR CREATE (TAMBAH DATA PEMBELI)
            # =============================================
            if menu == "1":
                os.system('cls')
                print("=== TAMBAH DATA PEMBELI ===")
                id_p = input("Masukkan ID pembeli: ")

                if id_p in data_pembeli:
                    print("ID pembeli sudah ada!")
                else:
                    nama = input("Masukkan nama pembeli: ")
                    print("\nPilih jenis sepatu yang dibeli:")
                    for k, v in paket_sepatu.items():
                        print(f"{k}. {v['nama']} - Rp{v['harga']:,}")

                    pilih_sepatu = input("Masukkan nomor sepatu: ")
                    if pilih_sepatu in paket_sepatu:
                        sepatu = paket_sepatu[pilih_sepatu]['nama']
                        harga = paket_sepatu[pilih_sepatu]['harga']
                    else:
                        sepatu = "Custom"
                        harga = 0

                    data_pembeli[id_p] = {
                        "nama": nama,
                        "sepatu": sepatu,
                        "status": "Belum Bayar",
                        "harga": harga
                    }
                    print("\nData pembeli berhasil ditambahkan!")

                input("Tekan Enter untuk kembali...")

            # =============================================
            # === FITUR READ (LIHAT DATA PEMBELI)
            # =============================================
            elif menu == "2":
                os.system('cls')
                print("=== DATA PEMBELI TOKO SEPATU ===")
                if not data_pembeli:
                    print("Belum ada data pembeli.")
                else:
                    for id_p, info in data_pembeli.items():
                        print(f"ID: {id_p}")
                        print(f"Nama: {info['nama']}")
                        print(f"Sepatu: {info['sepatu']}")
                        print(f"Status Pembayaran: {info['status']}")
                        print(f"Harga: Rp{info['harga']:,}")
                        print("-" * 35)
                    print(f"Total pembeli terdaftar: {len(data_pembeli)}")
                input("\nTekan Enter untuk kembali...")

            # =============================================
            # === FITUR UPDATE (ADMIN SAJA)
            # =============================================
            elif menu == "3" and is_admin:
                os.system('cls')
                print("=== UBAH DATA PEMBELI ===")
                id_cari = input("Masukkan ID pembeli: ")

                if id_cari in data_pembeli:
                    print("1. Ubah Nama")
                    print("2. Ubah Jenis Sepatu")
                    print("3. Ubah Status Pembayaran")
                    pilihan = input("Pilih data yang ingin diubah: ")

                    if pilihan == "1":
                        data_pembeli[id_cari]['nama'] = input("Masukkan nama baru: ")
                    elif pilihan == "2":
                        for k, v in paket_sepatu.items():
                            print(f"{k}. {v['nama']} - Rp{v['harga']:,}")
                        pilih_sepatu = input("Masukkan nomor sepatu: ")
                        if pilih_sepatu in paket_sepatu:
                            data_pembeli[id_cari]['sepatu'] = paket_sepatu[pilih_sepatu]['nama']
                            data_pembeli[id_cari]['harga'] = paket_sepatu[pilih_sepatu]['harga']
                    elif pilihan == "3":
                        data_pembeli[id_cari]['status'] = input("Masukkan status baru (Belum Bayar/Lunas): ")
                    else:
                        print("Pilihan tidak valid.")
                    print("Data berhasil diubah!")
                else:
                    print("Data pembeli tidak ditemukan.")

                input("\nTekan Enter untuk kembali...")

            # =============================================
            # === FITUR DELETE (ADMIN SAJA)
            # =============================================
            elif menu == "4" and is_admin:
                os.system('cls')
                print("=== HAPUS DATA PEMBELI ===")
                id_hapus = input("Masukkan ID pembeli: ")

                if id_hapus in data_pembeli:
                    del data_pembeli[id_hapus]
                    print("Data pembeli berhasil dihapus!")
                else:
                    print("Data pembeli tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

            # =============================================
            # === FITUR LIHAT DAFTAR SEPATU
            # =============================================
            elif menu == "5":
                os.system('cls')
                print("=== DAFTAR JENIS SEPATU ===")
                for v in paket_sepatu.values():
                    print(f"{v['nama']} | Harga: Rp{v['harga']:,}")
                input("\nTekan Enter untuk kembali...")

            # =============================================
            # === FITUR LOGOUT
            # =============================================
            elif menu == "6":
                print("Anda telah logout. Terima kasih!")
                login = False
                input("Tekan Enter untuk kembali ke menu awal...")
                break

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk kembali...")

    # =====================================================
    # === KELUAR DARI PROGRAM
    # =====================================================
    elif pilih_awal == "3":
        print("\nTerima kasih telah menggunakan sistem toko sepatu!")
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        #tes