
# Penerapan Sistem Fuzzy Logic

Program berbasis terminal ini dirancang untuk mengevaluasi kelayakan data berdasarkan dua parameter utama: Nilai Tes dan Waktu Pengerjaan. Dengan menggunakan pendekatan logika fuzzy, program ini dapat memberikan keputusan yang lebih fleksibel dan realistis.




## Instalasi Library

Persiapan untuk menggunakan Library skfuzzy dan numpy

```bash
    pip install scikit-fuzzy
    pip install numpy
```
    
## List Fungsi dan Aturan

Fungsi Nilai Test

![Fungsi Nilai Test](https://github.com/danaardana/tubes_dkb/blob/main/images/nilai_test.jpg?raw=true)



Fungsi Waktu Pengerjaan

![Fungsi Waktu Pengerjaan](https://github.com/danaardana/tubes_dkb/blob/main/images/waktu_pengerjaan.jpg?raw=true)



Aturan Fuzzy

![Aturan Fuzzy](https://github.com/danaardana/tubes_dkb/blob/main/images/aturan_fuzzy.jpg?raw=true)



Fungsi Keanggotaan Output (Takagi-Sugeno)

![Fungsi Keanggotaan Output (Takagi-Sugeno)](https://github.com/danaardana/tubes_dkb/blob/main/images/keanggotaan_output.jpg?raw=true)


## List Fungsi

**setup_fuzzy():** Menginisialisasi variabel input (nilai tes dan waktu pengerjaan) serta output (keputusan) dengan fungsi keanggotaan dan aturan fuzzy yang relevan. Menghasilkan objek simulasi kontrol fuzzy.

**urutkan_hasil(hasil_fuzzy):** Mengurutkan hasil keputusan berdasarkan nilai keputusan secara menurun.

**tampilkan_hasil(hasil_fuzzy):** Menampilkan hasil keputusan untuk setiap mahasiswa, termasuk status (Ditolak, Dipertimbangkan, Diterima) berdasarkan nilai keputusan.

**is_valid_name(nama):** Memeriksa validitas nama mahasiswa, memastikan hanya terdiri dari huruf dan spasi.

**input_data():** Mengumpulkan data mahasiswa, termasuk nama, nilai tes, dan waktu pengerjaan, hingga pengguna mengetik 'selesai'.

**eksekusi_fuzzy(perhitungan_fuzzy):** Menghitung hasil fuzzy untuk setiap mahasiswa berdasarkan input nilai dan waktu, dan menyimpan hasilnya dalam daftar.

**main():** Fungsi main() berfungsi sebagai antarmuka utama untuk program kontrol fuzzy. 

