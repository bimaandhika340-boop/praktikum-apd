
admin_user = "andhikaaa"
admin_pass = "123456"
guest_user = "andhika"
guest_pass = "12345"

akun_tambahan = []

paket_sepatu = [
    ["Sneakers Basic", 1, 250000],
    ["Running Pro", 1, 400000],
    ["Casual Street", 1, 350000],
    ["Formal Leather", 1, 500000],
    ["Anak Sekolah", 1, 200000]
] 

data_pelanggan = []

while True:
    print("\n=== SISTEM MANAJEMEN TOKO SEPATU ===")
    print("1. Login")
    print("2. Register Akun Baru")
    print("3. Keluar")

    pilih_awal = input("Pilih menu: ")

    if pilih_awal == "2":
        print("\n=== REGISTER AKUN BARU ===")
        new_user = input("Masukkan username baru: ")
        new_pass = input("Masukkan password baru: ")

        duplikat = False
        if new_user == admin_user or new_user == guest_user:
            duplikat = True
        for a in akun_tambahan:
            if a[0] == new_user:
                duplikat = True

        if duplikat:
            print("Username sudah terdaftar! Silakan coba lagi.")
        else:
            akun_tambahan.append([new_user, new_pass])
            print("Akun berhasil dibuat! Silakan login menggunakan akun baru.")

        input("\nTekan Enter untuk kembali ke menu awal...")

    elif pilih_awal == "1":
        print("\n=== LOGIN SISTEM TOKO SEPATU ===")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        login = False
        is_admin = False

        if username == admin_user and password == admin_pass:
            login = True
            is_admin = True
        elif username == guest_user and password == guest_pass:
            login = True
        else:
            for a in akun_tambahan:
                if username == a[0] and password == a[1]:
                    login = True
                    break

        if not login:
            print("Login gagal! Username atau password salah.")
            input("\nTekan Enter untuk kembali...")
            continue

        print("Login berhasil!\n")

        while login:
            print("\n=== MENU UTAMA TOKO SEPATU ===")
            print("1. Tambah Data Pembeli (Create)")
            print("2. Lihat Data Pembeli (Read)")
            if is_admin:
                print("3. Ubah Data Pembeli (Update)")
                print("4. Hapus Data Pembeli (Delete)")
            print("5. Lihat Daftar Sepatu")
            print("6. Logout")

            menu = input("Pilih menu: ")

            if menu == "1":
                print("\n=== TAMBAH DATA PEMBELI ===")
                id_p = input("Masukkan ID pembeli: ")
                nama = input("Masukkan nama pembeli: ")

                print("\nPilih jenis sepatu yang dibeli:")
                for i, p in enumerate(paket_sepatu):
                    print(f"{i+1}. {p[0]} - Rp{p[2]:,}")

                pilih_paket = input("Masukkan nomor sepatu: ")
                if pilih_paket.isdigit() and 1 <= int(pilih_paket) <= len(paket_sepatu):
                    jenis = paket_sepatu[int(pilih_paket)-1][0]
                    harga = paket_sepatu[int(pilih_paket)-1][2]
                else:
                    print("Pilihan tidak valid, jenis diatur ke 'Custom'")
                    jenis = "Custom"
                    harga = 0

                status = "Belum Bayar"
                data_pelanggan.append([id_p, nama, jenis, status, harga])
                print("\nData pembeli berhasil ditambahkan!")
                input("Tekan Enter untuk kembali...")

            elif menu == "2":
                print("\n=== DATA PEMBELI TOKO SEPATU ===")
                if len(data_pelanggan) == 0:
                    print("Belum ada data pembeli.")
                else:
                    for p in data_pelanggan:
                        print(f"\nID: {p[0]}")
                        print(f"Nama: {p[1]}")
                        print(f"Jenis Sepatu: {p[2]}")
                        print(f"Status Pembayaran: {p[3]}")
                        print(f"Total Harga: Rp{p[4]:,}")
                        print("-" * 35)
                    print(f"\nTotal pembeli terdaftar: {len(data_pelanggan)}")
                input("\nTekan Enter untuk kembali...")

            elif menu == "3" and is_admin:
                print("\n=== UBAH DATA PEMBELI ===")
                id_cari = input("Masukkan ID pembeli yang ingin diubah: ")
                ketemu = False
                for p in data_pelanggan:
                    if p[0] == id_cari:
                        ketemu = True
                        print("\nData ditemukan!")
                        print("1. Ubah nama")
                        print("2. Ubah jenis sepatu")
                        print("3. Ubah status pembayaran")
                        pilihan = input("Pilih data yang ingin diubah: ")

                        if pilihan == "1":
                            p[1] = input("Masukkan nama baru: ")
                        elif pilihan == "2":
                            print("\nPilih jenis sepatu baru:")
                            for i, x in enumerate(paket_sepatu):
                                print(f"{i+1}. {x[0]} - Rp{x[2]:,}")
                            pilih_paket = input("Masukkan nomor sepatu: ")
                            if pilih_paket.isdigit() and 1 <= int(pilih_paket) <= len(paket_sepatu):
                                p[2] = paket_sepatu[int(pilih_paket)-1][0]
                                p[4] = paket_sepatu[int(pilih_paket)-1][2]
                            else:
                                print("Pilihan tidak valid, tidak ada perubahan jenis.")
                        elif pilihan == "3":
                            p[3] = input("Masukkan status baru (Belum Bayar / Lunas): ")
                        else:
                            print("Pilihan tidak valid.")

                        print("\nData berhasil diubah!")
                        break

                if not ketemu:
                    print("Data dengan ID tersebut tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

            elif menu == "4" and is_admin:
                print("\n=== HAPUS DATA PEMBELI ===")
                id_hapus = input("Masukkan ID pembeli yang ingin dihapus: ")
                ketemu = False
                for p in data_pelanggan:
                    if p[0] == id_hapus:
                        ketemu = True
                        data_pelanggan.remove(p)
                        print("Data pembeli berhasil dihapus!")
                        break
                if not ketemu:
                    print("Data dengan ID tersebut tidak ditemukan.")
                input("\nTekan Enter untuk kembali...")

            elif menu == "5":
                print("\n=== DAFTAR JENIS SEPATU ===")
                for p in paket_sepatu:
                    print(f"{p[0]} | Harga: Rp{p[2]:,}")
                input("\nTekan Enter untuk kembali...")

            elif menu == "6":
                print("\nAnda telah logout. Terima kasih!")
                login = False
                input("Tekan Enter untuk kembali ke menu awal...")
                break

            else:
                print("Menu tidak valid!")
                input("Tekan Enter untuk kembali...")

    elif pilih_awal == "3":
        print("\nTerima kasih telah menggunakan sistem toko sepatu!")
        
        break

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")