from fuzzy_logic import *  
  
data_mahasiswa = []  
  
def is_valid_name(nama):  
    return all(char.isalpha() or char.isspace() for char in nama)  
  
def input_data():  
    while True:  
        nama = input("Masukkan nama mahasiswa (atau ketik 'selesai' untuk selesai): ").strip()  
          
        # Memeriksa apakah 'selesai' ada dalam input  
        if 'selesai' in nama.lower():    
            break  
  
        if not is_valid_name(nama):  
            print("Nama hanya boleh terdiri dari huruf dan spasi. Silakan coba lagi.")  
            continue  
  
        # Pengecekan untuk nilai tes  
        while True:  
            try:  
                nilai = float(input("Masukkan nilai tes (0-100): "))  
                if 0 <= nilai <= 100:  
                    break  # Keluar dari loop jika input valid  
                else:  
                    print("Nilai harus antara 0 dan 100. Silakan coba lagi.")  
            except ValueError:  
                print("Input tidak valid. Harap masukkan angka.")  
  
        # Pengecekan untuk waktu pengerjaan  
        while True:  
            try:  
                waktu = float(input("Masukkan waktu pengerjaan (0-150 menit): "))  
                if 0 <= waktu <= 150:  
                    break  # Keluar dari loop jika input valid  
                else:  
                    print("Waktu harus antara 0 dan 150 menit. Silakan coba lagi.")  
            except ValueError:  
                print("Input tidak valid. Harap masukkan angka.")  
  
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
  
def urutkan_hasil(hasil_fuzzy):  
    return sorted(hasil_fuzzy, key=lambda x: x[1], reverse=True)  
  
def tampilkan_hasil(hasil_terurut):  
    print("\nHasil Keputusan:")  
    for nama, nilai in hasil_terurut:  
        if nilai < 50:  
            status = "Ditolak"  
        elif 50 <= nilai < 75:  
            status = "Dipertimbangkan"  
        else:  
            status = "Diterima"  
        print(f"{nama}: {nilai:.2f} - Status: {status}")  
  
def main():  
    perhitungan_fuzzy, nilai_tes, waktu_pengerjaan, keputusan = setup_fuzzy()  
      
    while True:  
        print("\nMenu:")  
        print("1. Masukkan Data Mahasiswa")  
        print("2. Eksekusi Program Fuzzy")  
        print("3. Keluar")  
          
        pilihan = input("Pilih menu (1/2/3): ").strip()  # Menggunakan input untuk pilihan menu  
          
        if pilihan == '1':  
            input_data()  
  
        elif pilihan == '2':  
            if len(data_mahasiswa) < 2:  # Pengecekan jumlah data mahasiswa  
                print("Minimal harus ada 2 data mahasiswa untuk menjalankan program fuzzy.")  
            else:  
                hasil_fuzzy = eksekusi_fuzzy(perhitungan_fuzzy)  
                hasil_terurut = urutkan_hasil(hasil_fuzzy)  
                tampilkan_hasil(hasil_terurut)  
  
        elif pilihan == '3':  
            print("Keluar dari program.")  
            break  
          
        else:  
            print("Pilihan tidak valid. Silakan coba lagi.")  
  
if __name__ == "__main__":  
    main()  
