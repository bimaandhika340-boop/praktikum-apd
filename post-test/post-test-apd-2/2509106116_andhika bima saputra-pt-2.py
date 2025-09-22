nama = input("Masukkan nama pelanggan: ")
jumlah_batu_bata = int(input("Masukkan jumlah batu bata yang dibeli: "))
jumlah_semen = int(input("Masukkan jumlah karung semen yang dibeli: "))
                   
harga_batu_bata = 100
harga_semen = 100000


total_awal = (jumlah_batu_bata * harga_batu_bata) + (jumlah_semen * harga_semen)


is_paket_ultra = jumlah_batu_bata == 2000 and jumlah_semen == 16
is_paket_hemat = jumlah_batu_bata == 500 and jumlah_semen == 5

if is_paket_ultra:
    diskon_persen = 30 / 100
    keterangan_diskon = "Paket Ultra Mantap (30%)"
elif is_paket_hemat:
    diskon_persen = 15 / 100
    keterangan_diskon = "Paket Hemat (15%)"
else:
    diskon_persen = 0
    keterangan_diskon = "Tidak Ada Diskon"

jumlah_diskon = total_awal * diskon_persen
total_akhir = float(total_awal - jumlah_diskon)


print(f"Nama Pelanggan: {nama}")
print("| Barang     | Jumlah   | Harga Satuan       |")
print(f"| Batu Bata  | {jumlah_batu_bata:<8} | Rp{harga_batu_bata:<17,} |")
print(f"| Semen      | {jumlah_semen:<8} | Rp{harga_semen:<17,}")
print(f"Total Biaya Awal          : Rp {total_awal:,.0f}")
print(f"Diskon yang Didapat       : {keterangan_diskon}")
print(f"Jumlah Diskon             : Rp {jumlah_diskon:,.0f}")
print(f"TOTAL BIAYA AKHIR         : Rp {total_akhir:,.0f}")


