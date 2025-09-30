print ("=================================")
print (" MENGHITUNG GAJI KARYAWAN PT BOM ")
print ("=================================")

nama_karyawan = input("masukkan nama karyawan: ")
jabatan_karyawan = input("masukkan jabatan karyawan (peracik/pengantar): ")
hari_kerja = int(input("jumlah hari kerja: "))
jam_kerja = int(input("jumlah jam kerja: "))
jumlah_lembur = int(input("jumlah lembur: "))

harga_per1pcs_petasan = 5000
bayaran_perjam = 0
bayaran_perlembur = 0

if jabatan_karyawan == "peracik":
    if hari_kerja >= 24 and jam_kerja >= 8 and jumlah_lembur >= 4:
        bayaran_perjam = 25000
        bayaran_perlembur = 15000
    elif hari_kerja >= 18 and jam_kerja >= 6 and jumlah_lembur >= 2:
        bayaran_perjam = 20000
        bayaran_perlembur = 10000
    else:
        bayaran_perjam = 15000
        bayaran_perlembur = 10000

elif jabatan_karyawan == "pengantar":
    if hari_kerja >= 20 and jam_kerja >= 7 and jumlah_lembur >= 7:
        bayaran_perjam = 25000
        bayaran_perlembur = 20000
    elif hari_kerja >= 16 and jam_kerja >= 5 and jumlah_lembur >= 4:
        bayaran_perjam = 20000
        bayaran_perlembur = 15000
else:
        bayaran_perjam = 15000
        bayaran_perlembur = 12000

total_gaji = ((bayaran_perjam * jam_kerja) * hari_kerja) + (jumlah_lembur * bayaran_perlembur)

print ("=================================")
print (" MENGHITUNG GAJI KARYAWAN PT BOM ")
print ("=================================")
print(f"nama karyawan : {nama_karyawan}")
print(f"harga 1pcs petasan : {harga_per1pcs_petasan:}")
print(f"jumlah hari kerja : {hari_kerja}")
print(f"jumlah jam kerja : {jam_kerja} ")
print(f"jumlah lembur : {jumlah_lembur}")
print(f"bayaran per jam : {bayaran_perjam:}")
print(f"bayaran per lembur : {bayaran_perlembur:}")
print(f"total gaji : {total_gaji:}")