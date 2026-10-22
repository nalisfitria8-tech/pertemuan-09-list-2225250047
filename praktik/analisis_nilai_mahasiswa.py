# Program Praktik: Analisis Nilai Mahasiswa
# Mata Kuliah: Algoritma dan Pemrograman

def rata_rata(data):
    """Menghitung rata-rata dari suatu list numerik dengan aman (menangani list kosong)."""
    if len(data) == 0:
        return 0
    return sum(data) / len(data)

def nilai_lulus(data, batas=60):
    """Menyaring dan mengembalikan list nilai yang memenuhi batas kelulusan."""
    hasil = []
    for x in data:
        if x >= batas:
            hasil.append(x)
    return hasil

# List data nilai mahasiswa
nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Memproses data menggunakan fungsi dan fungsi agregasi bawaan Python
lulus = nilai_lulus(nilai)
jumlah_lulus = len(lulus)
jumlah_belum_lulus = len(nilai) - jumlah_lulus

# Menampilkan hasil analisis secara terstruktur dan mudah dibaca
print("=== LAPORAN ANALISIS NILAI MAHASISWA ===")
print(f"Data Seluruh Nilai : {nilai}")
print(f"Banyak Data        : {len(nilai)}")
print(f"Total Nilai        : {sum(nilai)}")
print(f"Rata-rata Nilai    : {rata_rata(nilai):.2f}")
print(f"Nilai Minimum      : {min(nilai)}")
print(f"Nilai Maksimum     : {max(nilai)}")
print(f"Nilai Lulus (>=60) : {lulus}")
print(f"Jumlah Lulus       : {jumlah_lulus}")
print(f"Jumlah Belum Lulus : {jumlah_belum_lulus}")