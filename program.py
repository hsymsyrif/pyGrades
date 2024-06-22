import json

class Mahasiswa:
    def __init__(self, nim, nama, jurusan, semester, nilai_mid, nilai_uas, nilai_tugas, nilai_quiz):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.semester = semester
        self.nilai_mid = nilai_mid
        self.nilai_uas = nilai_uas
        self.nilai_tugas = nilai_tugas
        self.nilai_quiz = nilai_quiz
        self.nilai_akhir = self.hitung_nilai_akhir()
        self.nilai_huruf = self.konversi_nilai_huruf()

    def hitung_nilai_akhir(self):
        return (0.3 * self.nilai_mid) + (0.4 * self.nilai_uas) + (0.2 * self.nilai_tugas) + (0.1 * self.nilai_quiz)

    def konversi_nilai_huruf(self):
        if self.nilai_akhir >= 85:
            return 'A'
        elif self.nilai_akhir >= 70:
            return 'B'
        elif self.nilai_akhir >= 55:
            return 'C'
        elif self.nilai_akhir >= 40:
            return 'D'
        else:
            return 'E'

    def to_dict(self):
        return {
            "nim": self.nim,
            "nama": self.nama,
            "jurusan": self.jurusan,
            "semester": self.semester,
            "nilai_mid": self.nilai_mid,
            "nilai_uas": self.nilai_uas,
            "nilai_tugas": self.nilai_tugas,
            "nilai_quiz": self.nilai_quiz,
            "nilai_akhir": self.nilai_akhir,
            "nilai_huruf": self.nilai_huruf
        }

    @staticmethod
    def from_dict(data):
        return Mahasiswa(data["nim"], data["nama"], data["jurusan"], data["semester"], data["nilai_mid"], data["nilai_uas"], data["nilai_tugas"], data["nilai_quiz"])

def simpan_data(daftar_mahasiswa, filename="data_mahasiswa.json"):
    with open(filename, 'w') as file:
        json.dump([mahasiswa.to_dict() for mahasiswa in daftar_mahasiswa], file)
    print("Data mahasiswa berhasil disimpan.\n")

def muat_data(filename="data_mahasiswa.json"):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Mahasiswa.from_dict(m) for m in data]
    except FileNotFoundError:
        return []

def tambah_mahasiswa(daftar_mahasiswa):
    try:
        nim = input("Masukkan NIM (10 angka): ").strip()
        if len(nim) != 10 or not nim.isdigit():
            raise ValueError("NIM harus terdiri dari 10 angka")
        nama = input("Masukkan nama mahasiswa: ").strip()
        jurusan = input("Masukkan jurusan: ").strip()
        semester = int(input("Masukkan semester: ").strip())
        nilai_mid = float(input("Masukkan nilai mid: ").strip())
        nilai_uas = float(input("Masukkan nilai uas: ").strip())
        nilai_tugas = float(input("Masukkan nilai tugas: ").strip())
        nilai_quiz = float(input("Masukkan nilai quiz: ").strip())

        mahasiswa = Mahasiswa(nim, nama, jurusan, semester, nilai_mid, nilai_uas, nilai_tugas, nilai_quiz)
        daftar_mahasiswa.append(mahasiswa)
        print(f"Mahasiswa {nama} berhasil ditambahkan!\n")
    except ValueError as e:
        print(f"Error: {e}. Silakan coba lagi.\n")

def cari_mahasiswa(daftar_mahasiswa):
    nim = input("Masukkan NIM mahasiswa yang ingin dicari: ").strip()
    for mahasiswa in daftar_mahasiswa:
        if mahasiswa.nim == nim:
            print(f"====================\nNIM: {mahasiswa.nim} \nNama: {mahasiswa.nama} \nJurusan: {mahasiswa.jurusan} \nSemester: {mahasiswa.semester}\n==================== \nNilai Mid: {mahasiswa.nilai_mid} \nNilai UAS: {mahasiswa.nilai_uas} \nNilai Tugas: {mahasiswa.nilai_tugas} \nNilai Quiz: {mahasiswa.nilai_quiz} \nNilai Akhir: {mahasiswa.nilai_akhir:.2f} \nNilai Abjad: {mahasiswa.nilai_huruf}\n====================")
            return
    print("Mahasiswa tidak ditemukan.\n")

def peringkat_mahasiswa(daftar_mahasiswa):
    if not daftar_mahasiswa:
        print("Belum ada mahasiswa yang terdaftar.\n")
        return

    daftar_mahasiswa.sort(key=lambda mahasiswa: mahasiswa.nilai_akhir, reverse=True)
    print("Peringkat mahasiswa berdasarkan nilai akhir:")
    for i, mahasiswa in enumerate(daftar_mahasiswa, 1):
        print(f"====================\n{i}. {mahasiswa.nama} \nNIM: {mahasiswa.nim} \nNilai Akhir: {mahasiswa.nilai_akhir:.2f} \nNilai Abjad: {mahasiswa.nilai_huruf}\n====================")
    print()

def rekapitulasi_nilai(daftar_mahasiswa):
    if not daftar_mahasiswa:
        print("Belum ada mahasiswa yang terdaftar.\n")
        return

    print("Rekapitulasi nilai seluruh mahasiswa:")
    for mahasiswa in daftar_mahasiswa:
        print(f"====================\nNIM: {mahasiswa.nim}\nNama: {mahasiswa.nama}\nJurusan: {mahasiswa.jurusan}\nSemester: {mahasiswa.semester}\nNilai Mid: {mahasiswa.nilai_mid}\nNilai UAS: {mahasiswa.nilai_uas}\nNilai Tugas: {mahasiswa.nilai_tugas}\nNilai Quiz: {mahasiswa.nilai_quiz}\nNilai Akhir: {mahasiswa.nilai_akhir:.2f}\nNilai Abjad: {mahasiswa.nilai_huruf}\n====================")
    print()

def tampilkan_menu():
    print("\nMenu:")
    print("1. Entri data mahasiswa")
    print("2. Pencarian data mahasiswa")
    print("3. Peringkat nilai mahasiswa")
    print("4. Rekapitulasi nilai mahasiswa")
    print("5. Simpan data")
    print("6. Muat data")
    print("7. Keluar")

def main():
    daftar_mahasiswa = muat_data()

    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (1-7): ").strip()

        if pilihan == '1':
            tambah_mahasiswa(daftar_mahasiswa)
        elif pilihan == '2':
            cari_mahasiswa(daftar_mahasiswa)
        elif pilihan == '3':
            peringkat_mahasiswa(daftar_mahasiswa)
        elif pilihan == '4':
            rekapitulasi_nilai(daftar_mahasiswa)
        elif pilihan == '5':
            simpan_data(daftar_mahasiswa)
        elif pilihan == '6':
            daftar_mahasiswa = muat_data()
            print("Data mahasiswa berhasil dimuat.\n")
        elif pilihan == '7':
            print("Terima kasih telah menggunakan program ini!\n")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.\n")

if __name__ == "__main__":
    main()
