import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def setup_fuzzy():
    # Definisikan variabel input
    nilai_tes = ctrl.Antecedent(np.arange(0, 101, 1), 'Nilai Tes')
    waktu_pengerjaan = ctrl.Antecedent(np.arange(0, 151, 1), 'Waktu Pengerjaan')

    # Definisikan variabel output
    keputusan = ctrl.Consequent(np.arange(0, 101, 1), 'Keputusan')

    # Fungsi keanggotaan untuk Nilai Tes
    nilai_tes['Rendah'] = fuzz.trimf(nilai_tes.universe, [0, 30, 40])
    nilai_tes['Sedang'] = fuzz.trimf(nilai_tes.universe, [30, 50, 70])
    nilai_tes['Tinggi'] = fuzz.trimf(nilai_tes.universe, [60, 80, 95])
    nilai_tes['Sangat Tinggi'] = fuzz.trimf(nilai_tes.universe, [80, 95, 100])

    # Fungsi keanggotaan untuk Waktu Pengerjaan
    waktu_pengerjaan['Cepat'] = fuzz.trimf(waktu_pengerjaan.universe, [0, 20, 60])
    waktu_pengerjaan['Sedang'] = fuzz.trimf(waktu_pengerjaan.universe, [20, 60, 120])
    waktu_pengerjaan['Lama'] = fuzz.trimf(waktu_pengerjaan.universe, [80, 120, 150])

    # Fungsi keanggotaan untuk Keputusan
    keputusan['Ditolak'] = fuzz.trimf(keputusan.universe, [0, 50, 75])
    keputusan['Dipertimbangkan'] = fuzz.trimf(keputusan.universe, [50, 75, 100])
    keputusan['Diterima'] = fuzz.trimf(keputusan.universe, [75, 100, 100])

    # Aturan fuzzy
    rules = [
        ctrl.Rule(nilai_tes['Rendah'] & waktu_pengerjaan['Cepat'], keputusan['Ditolak']),
        ctrl.Rule(nilai_tes['Rendah'] & waktu_pengerjaan['Sedang'], keputusan['Ditolak']),
        ctrl.Rule(nilai_tes['Rendah'] & waktu_pengerjaan['Lama'], keputusan['Ditolak']),
        ctrl.Rule(nilai_tes['Sedang'] & waktu_pengerjaan['Cepat'], keputusan['Dipertimbangkan']),
        ctrl.Rule(nilai_tes['Sedang'] & waktu_pengerjaan['Sedang'], keputusan['Dipertimbangkan']),
        ctrl.Rule(nilai_tes['Sedang'] & waktu_pengerjaan['Lama'], keputusan['Diterima']),
        ctrl.Rule(nilai_tes['Tinggi'] & waktu_pengerjaan['Cepat'], keputusan['Diterima']),
        ctrl.Rule(nilai_tes['Tinggi'] & waktu_pengerjaan['Sedang'], keputusan['Diterima']),
        ctrl.Rule(nilai_tes['Tinggi'] & waktu_pengerjaan['Lama'], keputusan['Dipertimbangkan']),
        ctrl.Rule(nilai_tes['Sangat Tinggi'] & waktu_pengerjaan['Cepat'], keputusan['Diterima']),
        ctrl.Rule(nilai_tes['Sangat Tinggi'] & waktu_pengerjaan['Sedang'], keputusan['Diterima']),
        ctrl.Rule(nilai_tes['Sangat Tinggi'] & waktu_pengerjaan['Lama'], keputusan['Diterima']),
    ]

    # Membuat sistem kontrol
    keputusan_akhir = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(keputusan_akhir), nilai_tes, waktu_pengerjaan, keputusan

def urutkan_hasil(hasil_fuzzy):
    # Mengurutkan berdasarkan nilai keputusan
    return sorted(hasil_fuzzy, key=lambda x: x[1], reverse=True)

def tampilkan_hasil(hasil_fuzzy):
    print("\nHasil Keputusan:")

    for nama, nilai in hasil_fuzzy:

        if nilai < 50:
            status = "Ditolak"

        elif 50 <= nilai < 75:
            status = "Dipertimbangkan"

        else:
            status = "Diterima"

        print(f"Nama : {nama} - Status: {status}")

        # Bila menampilkan nilai dari aturan fuzzy    
        #print(f"Nama {nama} : {nilai:.2f} - Status: {status}")

def is_valid_name(nama):
    # Memeriksa apakah nama hanya terdiri dari huruf dan spasi
    return all(char.isalpha() or char.isspace() for char in nama)