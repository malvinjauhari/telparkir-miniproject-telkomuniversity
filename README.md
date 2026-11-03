PARKIRKU - TEL PARKIR INTEGRATED SYSTEMS

Nama	: M. Alvin Jauhari
Kelas	: SS1SI-50-REG-01
Dosen	: Adzanil Rachmadi Putra

TEL-PARKIR Integrated System atau ParkirKu merupakan program berbasis Python yang dirancang untuk membantu proses pencatatan kendaraan dan perhitungan biaya parkir secara otomatis. Program ini digunakan untuk5 mencatat informasi kendaraan berdasarkan nomor polisi, jenis kendaraan, waktu masuk, waktu keluar, kepemilikan kartu civitas, serta kondisi tiket parkir. Sistem menyediakan dua kategori kendaraan, yaitu motor dan mobil, dengan tarif parkir yang berbeda berdasarkan durasi penggunaan tempat parkir.

Fitur utama TEL PARKIR meliputi validasi input pengguna, perhitungan durasi parkir dalam satuan menit, pembulatan durasi menjadi jam tagihan, pemberian parkir gratis untuk durasi maksimal 15 menit, pemberian diskon sebesar 20% bagi pengguna kartu civitas yang tidak kehilangan tiket, serta penambahan denda sebesar Rp10.000 apabila tiket hilang. Setelah proses pembayaran, program akan menampilkan struk parkir secara otomatis. Selain itu, program memiliki fitur rekapitulasi harian yang mencakup jumlah kendaraan, jumlah motor dan mobil, rata-rata durasi parkir, rata-rata pembayaran, jumlah kendaraan gratis, jumlah penerima diskon, jumlah tiket hilang, durasi parkir terlama, dan pembayaran tertinggi.

Dekomposisi Masalah:
Dekomposisi masalah merupakan proses membagi permasalahan utama menjadi beberapa bagian yang lebih kecil agar lebih mudah diselesaikan melalui pemrograman. Dalam program TEL PARKIR, permasalahan dibagi menjadi beberapa tahapan berikut:

Sub-Masalah	Plan Pemrograman	Letak di Program (Baris)
Mendefinisikan konstanta (tarif, batas waktu, diskon)	Assignment Variables	2 - 26
Mencetak tabel tarif dinamis sebagai informasi awal	For Loop (Iterasi)	40 - 49
Inisialisasi variabel rekapitulasi (0 / nilai awal)	Assignment	51 - 62
Menerima banyak data kendaraan hingga operator selesai	Sentinel Loop (!= "selesai")	65 - 215
Memastikan format input pengguna sesuai aturan sistem	Validation / Guard Loop	67 - 123
Memastikan waktu keluar tidak mendahului waktu masuk	Guard Loop	108 - 123
Menghitung durasi menit, tagihan jam, dan tarif dasar	Kalkulasi Numerik	136 - 165
Menghitung diskon civitas dan denda tiket hilang	Kondisional (If-Else)	167 - 177
Mencetak struk parkir per kendaraan	Output	182 - 192
Menghitung rekap (total kendaraan, pendapatan, maks)	Akumulator & Pencarian Max	194 - 213
Menampilkan ringkasan data harian (mencegah Div/0)	Output & Kondisional	218 - 231

Flowchart/ Pseudocode:
total_masuk = (jam_masuk * 60) + menit_masuk
total_keluar = (jam_keluar * 60) + menit_keluar
durasi_menit = total_keluar - total_masuk

IF durasi_menit <= 15 THEN
    jam_tagihan = 0
ELSE
    jam_tagihan = (durasi_menit + 59) DIV 60
END IF

IF jenis == "motor" THEN
    IF jam_tagihan == 0 THEN 
        tarif_dasar = 0
    ELSE IF jam_tagihan == 1 THEN 
        tarif_dasar = 2000
    ELSE 
        tarif_dasar = 2000 + (jam_tagihan - 1) * 1000
    END IF
ELSE IF jenis == "mobil" THEN
    IF jam_tagihan == 0 THEN 
        tarif_dasar = 0
    ELSE IF jam_tagihan == 1 THEN 
        tarif_dasar = 5000
    ELSE 
        tarif_dasar = 5000 + (jam_tagihan - 1) * 3000
    END IF
END IF

IF kartu == "ya" AND tiket_hilang == "tidak" AND tarif_dasar > 0 THEN
    diskon = (tarif_dasar * 20) DIV 100
ELSE
    diskon = 0
END IF

IF tiket_hilang == "ya" THEN
    denda = 10000
ELSE
    denda = 0
END IF
total_bayar = tarif_dasar - diskon + denda
Penjelasan Alur Perhitungan
1.Program menerima data waktu masuk dan waktu keluar kendaraan.
2.Waktu dikonversikan menjadi satuan menit agar durasi parkir dapat dihitung.
3.Apabila durasi parkir maksimal 15 menit, kendaraan mendapatkan fasilitas parkir gratis.
4.Apabila durasi melebihi 15 menit, sistem membulatkan durasi ke atas menjadi jam tagihan.
5.Tarif dasar dihitung berdasarkan jenis kendaraan, yaitu motor atau mobil.
6.Pengguna yang memiliki kartu civitas dan tidak kehilangan tiket memperoleh diskon sebesar 20%.
7.Apabila tiket hilang, sistem menambahkan denda sebesar Rp10.000.
8.Total pembayaran dihitung dari tarif dasar dikurangi diskon kemudian ditambah denda.
9.Program menampilkan struk pembayaran.

Tabel Penelusuran (Trace Table Simulasi Hitung Biaya)
Plat	Jenis	Masuk	Keluar	Kartu	Tiket hilang	Urutan
A 1111 AA	Motor	13:00	13:40	Tidak	Tidak	Pertama
B 2222 BB	Mobil	06:50	09:10	Ya	Tidak	Kedua
C 3333 CC	Motor	15:00	15:15	Tidak	Tidak	Ketiga

Kendaraan ke-	Durasi	Jam tagih	Tarif dasar	Diskon	Total bayar	Jumlah	Total pendapatan	Durasi terlama
Awal	-	-	-	-	-	0	0	-1
1	40	1	2.000	0	2.000	1	2.000	40
2	140	3	8.000	1.600	6.400	2	8.400	140
3	15	0	0	0	0	3	8.400	140
Mengapa durasi terlama awalnya -1?
Karena dalam instruksi meminta nilai awal durasi_terlama = -1, sehingga kendaraan pertama tetap bisa tercatat sebagai durasi terlama, termasuk jika durasinya 0 menit.

Tabel Kasus Uji (Testing)
Pengujian dilakukan untuk memastikan program dapat menghasilkan perhitungan sesuai aturan yang telah ditentukan. Pengujian dibagi menjadi tiga kategori, yaitu kasus normal, kasus batas, dan kasus tidak valid.
Kasus Normal
No.	Masukan	Hasil yang Diharapkan	Hasil Program
1	Motor, 08:00–09:00, tanpa kartu, tiket tidak hilang	Tarif Rp2.000, total Rp2.000	Sesuai
2	Mobil, 08:00–10:00, tanpa kartu, tiket tidak hilang	Tarif Rp8.000, total Rp8.000	Sesuai
3	Motor, 08:00–10:00, memiliki kartu, tiket tidak hilang	Tarif Rp3.000, diskon Rp600, total Rp2.400	Sesuai


Kasus 
No.	Masukan	Hasil yang Diharapkan	Hasil Program
1	Motor, durasi 15 menit	Gratis, total Rp0	Sesuai
2	Motor, durasi 16 menit	1 jam tagihan, total Rp2.000	Sesuai
3	Mobil, durasi 8 jam, tanpa kartu	Tarif 8 jam, total Rp26.000	Sesuai
Kasus Tidak Valid
No.	Masukan	Hasil yang Diharapkan	Hasil Program
1	Nomor plat kosong	Program menolak input dan meminta nomor plat kembali	Sesuai
2	Jenis kendaraan selain motor/mobil	Program menolak input dan meminta jenis kendaraan yang benar	Sesuai
3	Jam masuk 25	Program menolak input dan meminta jam antara 0–23	Sesuai
4	Menit masuk 100	Seharusnya diterima karena rentang menit adalah 0–59	Belum sesuai, program menolak input

Analisis hasil pengujian:
Berdasarkan kasus uji, program telah mampu menangani sebagian besar kondisi normal, batas, dan input yang tidak sesuai. Namun, ditemukan kesalahan pada validasi menit masuk dan menit keluar. Kondisi program menggunakan menit_masuk >= MENIT_MAKSIMUM, sehingga angka 59 ikut ditolak. Seharusnya menggunakan menit_masuk > MENIT_MAKSIMUM agar nilai 59 dapat diterima.

Catatan Galat:
•Terjadi SyntaxError: expected ':' saat mendefinisikan perulangan while platnomor != KATA_SELESAI. Saya menemukannya karena program langsung terhenti (crash) sebelum dieksekusi. Diperbaiki dengan menambahkan titik dua (:) di akhir baris evaluasi kondisi.
•Muncul error ZeroDivisionError: division by zero pada bagian rekap akhir jika program langsung diketik "selesai" tanpa memasukkan satupun data kendaraan (karena mencoba rata_rata_durasi = jumlah_durasi / jumlah_kendaraan dimana jumlah_kendaraan bernilai 0). Diperbaiki dengan membungkus kalkulasi rata-rata dengan pengecekan if jumlah_kendaraan == NOL:.
•Sebelumnya perhitungan pembulatan jam ke atas keliru, yang menyebabkan parkir 1 jam 1 menit hanya dihitung 1 jam (karena pembagian integer //). Ditemukan melalui pengujian manual (Tabel Kasus Uji). Diperbaiki dengan mengimplementasikan trik penambahan menit 59 sebelum dibagi 60 (durasi_menit + TAMBAHAN_PEMBULATAN) // MENIT_PERJAM.
•IndentationError: expected an indented block saat menulis kode di dalam perulangan while dan blok if-else. Program gagal berjalan karena ada baris kode yang posisinya tidak sejajar atau menjorok dengan benar ke dalam scope logika yang semestinya. Saya menemukan letak error ini dengan melihat baris yang ditunjukkan pada pesan terminal, dan solusinya cukup mudah, yaitu tinggal diatur posisinya (menambah spasi/tab) agar sejajar dengan struktur blok yang tepat.

Refleksi
Konsep yang paling saya pahami dalam pembuatan sistem ini adalah alur percabangan berlapis (if-else) untuk menentukan tarif dasar sesuai jenis kendaraan, serta penerapan perulangan bersyarat (sentinel loop) untuk menahan program tetap berjalan hingga dihentikan. Bagian yang masih terasa sedikit menantang adalah merancang guard-loop untuk validasi waktu keluar-masuk agar durasi tidak bernilai negatif, karena logika perbandingan akumulasi total menit harus benar-benar dijaga agar tidak terjadi loop tanpa akhir (infinite loop).

Pengungkapan Penggunaan AI
Dalam proses pengerjaan program TEL PARKIR, saya menggunakan bantuan Artificial Intelligence (AI) sebagai pendamping untuk memahami konsep pemrograman Python, mengevaluasi alur program, serta membantu menyusun dokumentasi README.



Bagian yang dibantu AI:
1.Membantu menjelaskan konsep dekomposisi masalah dan penerapan konsep penjaga, akumulator, counter, serta sentinel.
2.Membantu menyusun pseudocode berdasarkan alur perhitungan biaya parkir.
3.Membantu menyusun contoh tabel penelusuran dan kasus pengujian.
4.Membantu mengidentifikasi kemungkinan kesalahan sintaks, runtime, dan logika.
5.Membantu merancang code menggunakan fitur auto suggestion
6.Membantu merapikan struktur dokumentasi agar sesuai dengan ketentuan tugas.

Saran AI yang digunakan:
•Penggunaan pseudocode untuk menjelaskan tahapan perhitungan biaya.
•Penggunaan tabel penelusuran untuk membandingkan perhitungan manual dengan hasil program.
•Penggunaan try-except sebagai alternatif untuk menangani input angka yang tidak valid.
•Menambahkan fungsi tampilkan menit dan jam agar hasilnya lebih detail dan akurat
•Perbaikan rumus tarif motor dan validasi menit agar sesuai dengan aturan.

Saran AI yang tidak digunakan:
•Membuat variabel baru serta pendeklarasian fungsi yang tidak sesuai dengan ketentuan tugas
•Menambahkan append, try/except

Saya tidak menggunakan seluruh saran AI secara langsung tanpa pemeriksaan. Setiap saran perlu disesuaikan dengan kode program, ketentuan tugas, dan pemahaman saya sendiri. Penggunaan AI hanya sebagai alat bantu, sedangkan pemahaman terhadap alur program dan hasil akhirnya tetap menjadi tanggung jawab saya sebagai mahasiswa.
