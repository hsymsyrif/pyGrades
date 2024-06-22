import math
import json

class Peserta:
    def __init__(self, nama, umur, panjang_tali, sudut_elevasi):
        self.nama = nama
        self.umur = umur
        self.panjang_tali = panjang_tali
        self.sudut_elevasi = sudut_elevasi
        self.tinggi_layangan = self.hitung_tinggi_layangan()

    def hitung_tinggi_layangan(self):
        return self.panjang_tali * math.sin(math.radians(self.sudut_elevasi))

    def to_dict(self):
        return {
            "nama": self.nama,
            "umur": self.umur,
            "panjang_tali": self.panjang_tali,
            "sudut_elevasi": self.sudut_elevasi,
            "tinggi_layangan": self.tinggi_layangan
        }

    @staticmethod
    def from_dict(data):
        return Peserta(data["nama"], data["umur"], data["panjang_tali"], data["sudut_elevasi"])

def simpan_data(daftar_peserta, filename="data_peserta.json"):
    with open(filename, 'w') as file:
        json.dump([peserta.to_dict() for peserta in daftar_peserta], file)
    print("Data peserta berhasil disimpan.\n")

def muat_data(filename="data_peserta.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Peserta.from_dict(p) for p in data]
    except FileNotFoundError:
        return []

def tambah_peserta(daftar_peserta):
    try:
        nama = input("Masukkan nama peserta: ").strip()
        if not nama:
            raise ValueError("Nama tidak boleh kosong")
        umur = int(input("Masukkan umur peserta: ").strip())
        panjang_tali = float(input("Masukkan panjang tali (dalam meter): ").strip())
        sudut_elevasi = float(input("Masukkan sudut elevasi (dalam derajat): ").strip())

        if umur <= 0 or panjang_tali <= 0 or sudut_elevasi < 0 or sudut_elevasi > 90:
            raise ValueError("Input data tidak valid")

        peserta = Peserta(nama, umur, panjang_tali, sudut_elevasi)
        daftar_peserta.append(peserta)
        print(f"Peserta {nama} berhasil ditambahkan!\n")
    except ValueError as e:
        print(f"Error: {e}. Silakan coba lagi.\n")

def cari_peserta(daftar_peserta):
    nama = input("Masukkan nama peserta yang ingin dicari: ").strip()
    for peserta in daftar_peserta:
        if peserta.nama.lower() == nama.lower():
            print(f"Nama: {peserta.nama}, Umur: {peserta.umur}, Panjang Tali: {peserta.panjang_tali} m, Sudut Elevasi: {peserta.sudut_elevasi} derajat, Tinggi Layangan: {peserta.tinggi_layangan:.2f} m\n")
            return
    print("Peserta tidak ditemukan.\n")

def tentukan_juara(daftar_peserta):
    if not daftar_peserta:
        print("Belum ada peserta yang terdaftar.\n")
        return

    juara = max(daftar_peserta, key=lambda peserta: peserta.tinggi_layangan)
    print(f"Juara: {juara.nama} dengan tinggi layangan {juara.tinggi_layangan:.2f} meter\n")

def tampilkan_menu():
    print("Menu:")
    print("1. Entri data peserta")
    print("2. Pencarian data peserta")
    print("3. Penentuan juara")
    print("4. Simpan data")
    print("5. Muat data")
    print("6. Keluar")

def main():
    daftar_peserta = muat_data()

    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ").strip()

        if pilihan == '1':
            tambah_peserta(daftar_peserta)
        elif pilihan == '2':
            cari_peserta(daftar_peserta)
        elif pilihan == '3':
            tentukan_juara(daftar_peserta)
        elif pilihan == '4':
            simpan_data(daftar_peserta)
        elif pilihan == '5':
            daftar_peserta = muat_data()
            print("Data peserta berhasil dimuat.\n")
        elif pilihan == '6':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
