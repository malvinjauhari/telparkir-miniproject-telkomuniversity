# Konstanta
TARIF_MOTOR_PERTAMA = 2000
TARIF_MOTOR_BERIKUTNYA = 1000
TARIF_MOBIL_PERTAMA = 4000
TARIF_MOBIL_BERIKUTNYA = 2000

# Nilai Maksimum
MAKSIMUM_MOTOR = 8000
MAKSIMUM_MOBIL = 16000

BATAS_GRATIS_MENIT = 15
PERSEN_DISKON = 20
PEMBAGI_PERSEN = 100
DENDA_TIKET_HILANG = 10000
KATA_SELESAI = "SELESAI"

# Aturan
JAM_MINIMUM = 1
JAM_MAKSIMUM = 8
JAM_TERAKHIR = 24 #Karena batas akhir 24 jam
MENIT_PERJAM = 60
MENIT_MAKSIMUM = 59
TAMBAHAN_PEMBULATAN = 59

# Pendefinisian
NOL = 0
SATU = 1
DUA = 2
JUMLAH_JAM = 9  
NILAI_AWAL_TERLAMA = -1
LEBAR_GRAFIK = 1

print("--------------------------------------------")
print("TEL-PARKIR INTEGRATED SYSTEM")
print("Developed By Alvin Jauhari")
print()

JAM_TABEL = JAM_MINIMUM

for JAM_TABEL in range(JAM_MINIMUM, JUMLAH_JAM):
    if JAM_TABEL == JAM_MINIMUM:
        TAMPILAN_TARIF_MOTOR = TARIF_MOTOR_PERTAMA
        TAMPILAN_TARIF_MOBIL = TARIF_MOBIL_PERTAMA
    else:
        TAMPILAN_TARIF_MOTOR = TARIF_MOTOR_PERTAMA + (JAM_TABEL - SATU) * TARIF_MOTOR_BERIKUTNYA
        TAMPILAN_TARIF_MOBIL = TARIF_MOBIL_PERTAMA + (JAM_TABEL - SATU) * TARIF_MOBIL_BERIKUTNYA
    print(JAM_TABEL, "Rp ", TAMPILAN_TARIF_MOTOR, "Rp", "|", TAMPILAN_TARIF_MOBIL)

# Reset jumlah
jumlah_kendaraan = NOL
jumlah_motor = NOL
jumlah_mobil = NOL
jumlah_durasi = NOL
jumlah_bayar = NOL
jumlah_gratis = NOL
jumlah_diskon = NOL
waktu_valid = NOL

jumlah_tiket_hilang = NOL
durasi_terlama = NILAI_AWAL_TERLAMA
bayar_tertinggi = NILAI_AWAL_TERLAMA

plat_durasi_terlama = "-"
plat_bayar_tertinggi = "-"

print()
# Input dan validasi
platnomor = str(input("Masukkan Plat Nomor Anda atau ketik (SELESAI) untuk keluar dari program: "))

while platnomor != KATA_SELESAI:
    platnomor_valid = NOL
    while platnomor_valid == NOL:
        # Jika platnomor tidak diinputkan/kosong
        if platnomor == "": 
            print("Plat Nomor Tidak Boleh Kosong")
            platnomor = str(input("Masukkan Plat Nomor Anda: "))
        else:
            platnomor_valid = SATU

    jenis = str(input("Masukkan jenis kendaraan anda (motor/mobil): "))
    #Jika jenis kendaraan tidak ada pada sistem, maka terjadilah looping
    while jenis != "motor" and jenis != "mobil":
        print("Jenis kendaraan anda tidak ditemukan di sistem, Mohon inputkan motor/mobil")
        jenis = str(input("Masukkan jenis kendaraan anda (motor/mobil): "))
    
    jam_masuk = int(input("Masukkan jam masuk kendaraan anda (0-23): "))
    #Jika jam masuk yang diinputkan tidak sesuai antara 0-23, Maka akan terjadi looping:
    while jam_masuk < NOL or jam_masuk >= JAM_TERAKHIR:
        print("Jam yang anda inputkan tidak valid, harus antara 0-23")
        jam_masuk = int(input("Masukkan jam masuk kendaraan anda (0-23): "))
    
    jam_keluar = int(input("Masukkan jam keluar kendaraan anda (0-23): "))
    #Jika jam masuk yang diinputkan tidak sesuai antara 0-23, Maka akan terjadi looping ke inputan sebelumnya
    while jam_keluar < NOL or jam_keluar >= JAM_TERAKHIR:
        print("Jam yang anda inputkan tidak valid, harus antara 0-23")
        jam_keluar = int(input("Masukkan jam keluar kendaraan anda (0-23): "))
    
    menit_masuk = int(input("Masukkan menit masuk kendaraan anda (0-59): "))
    while menit_masuk < NOL or menit_masuk > MENIT_MAKSIMUM:
        print("Menit yang anda inputkan tidak valid, harus antara 0-59")
        menit_masuk = int(input("Masukkan menit masuk kendaraan anda (0-59): "))
    
    menit_keluar = int(input("Masukkan menit keluar kendaraan anda (0-59): "))
    while menit_keluar < NOL or menit_keluar > MENIT_MAKSIMUM:
        print("Menit yang anda inputkan tidak valid, harus antara 0-59")
        menit_keluar = int(input("Masukkan menit keluar kendaraan anda (0-59): "))
    
    # WAKTU
    waktu_valid = NOL  # Reset untuk setiap kendaraan baru
    while waktu_valid == NOL:
        total_masuk = (jam_masuk * MENIT_PERJAM) + menit_masuk
        total_keluar = (jam_keluar * MENIT_PERJAM) + menit_keluar

        #Kode Dibuat Oleh AI

        # Jika waktu keluar kurang dari waktu masuk
        if total_keluar < total_masuk:
            print("Waktu tidak boleh lebih awal dari waktu masuk")
            jam_keluar = int(input("Jam keluar 0-23: "))
            while jam_keluar < NOL or jam_keluar >= JAM_TERAKHIR:
                print("Jam keluar tidak valid")
                jam_keluar = int(input("Jam keluar 0-23: "))
            menit_keluar = int(input("Menit keluar (0-59): "))
            while menit_keluar < NOL or menit_keluar > MENIT_MAKSIMUM:
                print("Menit tidak valid")
                menit_keluar = int(input("Menit keluar (0-59): "))
        else:
            waktu_valid = SATU  # Waktu valid, keluar dari loop
        
        #Kode Dibuat Oleh AI

    #Mengecek apakah punya kartu, dan jawabannya harus diantara ya dan tidak
    kartu = input("Apakah anda memiliki kartu civitas? (ya/tidak): ")
    while kartu != "ya" and kartu != "tidak":
        print("Jawaban yang anda masukkan tidak valid")
        kartu = input("Apakah anda memiliki kartu civitas? (ya/tidak): ")
    
    #Mengecek apakah tiketnya hilang, dan jawabannya harus diantara ya dan tidak
    tiket_hilang = input("Apakah tiket anda hilang? (ya/tidak): ")
    while tiket_hilang != "ya" and tiket_hilang != "tidak":
        print("Jawaban anda tidak valid")
        tiket_hilang = input("Apakah tiket anda hilang? (ya/tidak): ")

    # RUMUS
    total_masuk = jam_masuk * MENIT_PERJAM + menit_masuk
    total_keluar = jam_keluar * MENIT_PERJAM + menit_keluar
    durasi_menit = total_keluar - total_masuk

    # Kode ini dibuat oleh AI
    durasi_jam = durasi_menit // MENIT_PERJAM
    sisa_menit = durasi_menit % MENIT_PERJAM
    # Kode ini dibuat oleh AI

    # Kalau durasi kurang dari jumlah batas gratis

    if durasi_menit <= BATAS_GRATIS_MENIT:
        jam_tagihan = NOL
    else:
    # Tagihan normalnya
        jam_tagihan = (durasi_menit + TAMBAHAN_PEMBULATAN) // MENIT_PERJAM

    # Validasi jenis kendaraan
    if jenis == "motor":
        if jam_tagihan == NOL:
            tarif_dasar = NOL
        # Kondisi jam tagihan bernilai 1
        elif jam_tagihan == SATU:
            tarif_dasar = TARIF_MOTOR_PERTAMA
        else:
            tarif_dasar = TARIF_MOTOR_PERTAMA + (jam_tagihan - SATU) * TARIF_MOTOR_BERIKUTNYA
    elif jenis == "mobil":
        if jam_tagihan == NOL:
            tarif_dasar = NOL
        #Kondisi jam tagihan mobil
        elif jam_tagihan == SATU:
            tarif_dasar = TARIF_MOBIL_PERTAMA
        else:
            tarif_dasar = TARIF_MOBIL_PERTAMA + (jam_tagihan - SATU) * TARIF_MOBIL_BERIKUTNYA
    else:
        tarif_dasar = NOL

        # Kode ini dibuat oleh AI
    if jenis == "motor" and tarif_dasar > MAKSIMUM_MOTOR:
        tarif_dasar = MAKSIMUM_MOTOR
    elif jenis == "mobil" and tarif_dasar > MAKSIMUM_MOBIL:
        tarif_dasar = MAKSIMUM_MOBIL
        # Kode ini dibuat oleh AI

    diskon = NOL
    # Diskon hanya berlaku jika user punya kartu civitas

    # Jika user tidak kehilangan tiket, mendapatkan diskon
    if kartu == "ya" and tiket_hilang == 'tidak' and tarif_dasar > NOL:
        diskon = tarif_dasar * PERSEN_DISKON // PEMBAGI_PERSEN

    denda = NOL
    # Kondisi ketika tiket hilang

    if tiket_hilang == "ya":
        denda = DENDA_TIKET_HILANG

    # Total pembayaran parkir
    total_bayar = tarif_dasar - diskon + denda

    print()
    print("----------STRUK TEL-PARKIR------------------------------")
    print("Berikut ini adalah biaya parkir anda:")
    print("Plat Nomor           :", platnomor)
    print("Jenis Kendaraan      :", jenis)
    print("Jam Masuk            :", jam_masuk, ":", menit_masuk)
    print("Jam Keluar           :", jam_keluar, ":", menit_keluar)
    print("Durasi               :", durasi_jam, "jam", sisa_menit, "menit")
    print("Jam Tagihan          :", jam_tagihan, "jam")
    print("Tarif Dasar          :", tarif_dasar)
    print("Diskon               :", diskon)
    print("Denda Tiket Hilang   :", denda)
    print("Total Bayar          :", total_bayar)
    print("---------------------------------------------------------")

    #Kode ini dibuat oleh AI
    
    # + SATU Karena Membulatkan waktunya
    jumlah_kendaraan = jumlah_kendaraan + SATU
    jumlah_durasi = jumlah_durasi + durasi_menit
    jumlah_bayar = jumlah_bayar + total_bayar

    if jenis == "motor":
        jumlah_motor = jumlah_motor + SATU
    elif jenis == "mobil":
        jumlah_mobil = jumlah_mobil + SATU
    
    if jam_tagihan == NOL:
        jumlah_gratis = jumlah_gratis + SATU
    if diskon > NOL:
        jumlah_diskon = jumlah_diskon + SATU
    if tiket_hilang == "ya":
        jumlah_tiket_hilang = jumlah_tiket_hilang + SATU

    if durasi_menit > durasi_terlama:
        durasi_terlama = durasi_menit
        plat_durasi_terlama = platnomor
    if total_bayar > bayar_tertinggi:
        bayar_tertinggi = total_bayar
        plat_bayar_tertinggi = platnomor
    #Kode ini dibuat oleh AI

    platnomor = str(input("Masukkan Plat Nomor Anda atau ketik (SELESAI) untuk keluar dari program: "))

# REKAP AKHIR
print()
print("----REKAP HARIAN KENDARAAN TEL-PARKIR---")
if jumlah_kendaraan == NOL:
    print("Belum ada kendaraan yang tercatat")
else:
    # Menghitung rata rata durasi
    rata_rata_durasi = jumlah_durasi // jumlah_kendaraan

    rata_jam = rata_rata_durasi // MENIT_PERJAM
    rata_menit = rata_rata_durasi % MENIT_PERJAM
    rata_rata_bayar = jumlah_bayar // jumlah_kendaraan

    print("Jumlah Kendaraan          :", jumlah_kendaraan)
    print("Jumlah Motor              :", jumlah_motor)
    print("Jumlah Mobil              :", jumlah_mobil)
    print("Rata Rata Durasi          :", rata_jam, "jam", rata_menit, "menit")
    print("Rata Rata Bayar           :", rata_rata_bayar)
    print("Kendaraan Gratis          :", jumlah_gratis)
    print("Kendaraan Mendapat Diskon :", jumlah_diskon)
    print("Jumlah Tiket Hilang       :", jumlah_tiket_hilang)
    print("Durasi Terlama            :", plat_durasi_terlama, '(', durasi_terlama, "menit )")
    print("Total Bayar Tertinggi     :", plat_bayar_tertinggi, '(', bayar_tertinggi, "rupiah )")
    print()
    print("----Grafik jumlah kendaraan--------------")
    print("Motor |", "#" * jumlah_motor)
    print("Mobil |", "#" * jumlah_mobil)
    print("----TEL INTEGRATED SYSTEM------------------")