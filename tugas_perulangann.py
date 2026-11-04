# perulangan

jumlah = int(input("Masukkan Jumlah Mahasiswa: "))
total_nilai = 0

for i in range(1, jumlah + 1):
    nilai = float(input(f"Masukkan Nilai Mahasiswa {i}: "))
    total_nilai += nilai

rata_rata = total_nilai / jumlah
print("=============================")
print(f"Nilai Rata-rata: {rata_rata}")