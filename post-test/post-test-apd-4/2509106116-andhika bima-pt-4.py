
nim = int(input("Masukkan 3 digit terakhir NIM kamu: "))
stamina = nim
chakra = 0

print("\n=== Misi 1: Menyempurnakan Rasengan ===")
print(f"Stamina awal Naruto: {stamina}")

while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print(f"Total Chakra yang dikumpulkan: {chakra}")
print(f"Sisa stamina Naruto: {stamina}")

if chakra >= 200:
    print("Naruto berhasil menyempurnakan Rasengan!")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra...")


nim1  = int(input("Masukkan 2 digit terakhir NIM kamu: "))

tinggi_menara =nim1

print("\n=== Misi 2: Infiltrasi Menara ===")
print(f"Tinggi menara: {tinggi_menara} meter")

gulungan = 0

for meter in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print(f"Naruto berhasil mengumpulkan {gulungan} gulungan informasi!")

nim2 = int(input("Masukkan digit terakhir kedua NIM kamu: "))


koridor = nim2

print("\n=== Misi 3: Penyelidikan Markas Rahasia ===")
print(f"Jumlah koridor: {koridor}")

intelijen = 0
perangkap = 0

for k in range(1, koridor + 1):
    print(f"\nKoridor {k}:")
    for r in range(1, 4):
        print(f"  Ruangan {r}:", end=" ")
        if r % 2 == 1:
            print("Berisi Data Intelijen")
            intelijen += 1
        else:
            print("Berisi Perangkap Peledak")
            perangkap += 1

print("\n=== Hasil Penyelidikan ===")
print(f"Total Data Intelijen yang ditemukan: {intelijen}")
print(f"Total Perangkap Peledak yang dijinakkan: {perangkap}")
