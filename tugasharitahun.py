# input jumlah hari
x = int(input("Masukkan jumlah hari: "))

# hitung tahun
tahun = x // 365
sisa_hari = x % 365

# hitung bulan
bulan = sisa_hari // 30
hari = sisa_hari % 30

# output
print("Tahun :", tahun)
print("Bulan :", bulan)
print("Hari  :", hari)