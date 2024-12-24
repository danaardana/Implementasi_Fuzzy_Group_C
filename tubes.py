from fuzzy_logic import *

data_mahasiswa = []

def input_data():

    while True:
        nama = input("Masukkan nama mahasiswa (atau ketik 'selesai' untuk selesai): ").strip()
        
        # Memeriksa apakah 'selesai' ada dalam input
        if 'selesai' in nama.lower():  
            break

        if not is_valid_name(nama):
            print("Nama hanya boleh terdiri dari huruf dan spasi. Silakan coba lagi.")
            continue

        nilai = float(input("Masukkan nilai tes (0-100): "))
        waktu = float(input("Masukkan waktu pengerjaan (0-150 menit): "))
        data_mahasiswa.append((nama, nilai, waktu))

def eksekusi_fuzzy(perhitungan_fuzzy):
    hasil_fuzzy = []

    for nama, nilai, waktu in data_mahasiswa:
        perhitungan_fuzzy.input['Nilai Tes'] = nilai
        perhitungan_fuzzy.input['Waktu Pengerjaan'] = waktu
        perhitungan_fuzzy.compute()
        hasil_nilai = perhitungan_fuzzy.output['Keputusan']
        
        # Simpan hasil dalam list
        hasil_fuzzy.append((nama, hasil_nilai))
        
    return hasil_fuzzy

def main():
    perhitungan_fuzzy, nilai_tes, waktu_pengerjaan, keputusan = setup_fuzzy()
    
    while True:
        print("\nMenu:")
        print("1. Masukkan Data Mahasiswa")
        print("2. Eksekusi Program Fuzzy")
        print("3. Keluar")
        
        pilihan_menu = input("Pilih menu (1/2/3): ")
        
        if pilihan_menu == '1':
            input_data()

        elif pilihan_menu == '2':
            if not data_mahasiswa:
                print("Tidak ada data mahasiswa. Silakan masukkan data terlebih dahulu.")
            else:
                hasil_fuzzy = eksekusi_fuzzy(perhitungan_fuzzy)
                hasil_terurut = urutkan_hasil(hasil_fuzzy)
                tampilkan_hasil(hasil_terurut)

        elif pilihan_menu == '3':
            print("Keluar dari program.")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
