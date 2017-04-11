# Implementasi Algoritma DES Dengan Mode Operasi OFB untuk Keamanan Pengiriman Pesan Antar Device

Kelompok F09

- Riyadlatin Nufus (5114100151)
- Andreas Galang Anugrah (5114100153)
## Pendahuluan
Pada era dimana kemajuan teknologi sangat pesat seperti sekarang ini, keamanan dan kerahasiaan data pada jaringan komputer menjadi isu yang sangat penting dan terus berkembang. Kemajuan teknologi informasi tidak hanya menimbulkan dampak positif, melainkan juga dampak negatif. Kejahatan-kejahatan baru bermunculan, yang semula menggunakan teknik biasa, sekarang menggunakan metode dan teknik yang semakin canggih.

Berdasarkan kondisi tersebut, pengiriman data dan penyimpanan data melalui media elektronik memerlukan suatu proses yang dapat menjamin keamanan dan keutuhan dari data yang dikirimkan tersebut. Data tersebut harus tetap rahasia selama pengiriman dan harus tetap utuh pada saat penerimaan di tujuan. Untuk memenuhi hal tersebut, dilakukan proses penyandian (enkripsi dan dekripsi) terhadap data yang akan dikirimkan. 

Terdapat banyak algoritma untuk mengimplementasikan teknik enkripsi, salah satunya adalah DES (Data Encryption Standard), dan kali ini kita menggunakan mode operasi OFB (Output FeedBack). Adapun enkripsi dilakukan pada saat pengiriman dengan cara mengubah data asli menjadi data rahasia sedangkan dekripsi dilakukan pada saat penerimaan dengan cara mengubah data rahasia menjadi data asli. Jadi data yang dikirimkan selama proses pengiriman adalah data rahasia, sehingga data asli tidak dapat diketahui oleh pihak yang tidak berkepentingan. Data asli hanya dapat diketahui oleh penerima dengan menggunakan kunci rahasia.

## Dasar Teori
**A. Sniffer**

Sniffer adalah membaca dan menganalisa setiap protokol yang melewati mesin di mana program tersebut diinstal. Secara default, sebuah komputer dalam jaringan (workstation) hanya mendengarkan dan merespon paket-paket yang dikirimkan kepada mereka. Namun demikian, kartu jaringan (network card) dapat diset oleh beberapa program tertentu, sehingga dapat memonitor dan menangkap semua lalu lintas jaringan yang lewat tanpa peduli kepada siapa paket tersebut dikirimkan. Aktifitasnya biasa disebut dengan sniffing.

Setelah host attacker menjadi host yang berada di tengah-tengah dari dua host yang saling berkomunikasi, kemudian attacker melakukan analisa traffic dengan menjalankan program ethereal. Dengan menganalisa traffic TCP yang sudah tercapture, attacker dapat mengetahui apa saja yang dilakukan oleh host client terhadap host server.

**B.	Client Server**

Client Server adalah suatu bentuk arsitektur dimana client adalah perangkat yang menerima yang akan menampilkan dan menjalankan aplikasi (software komputer) dan server adalah perangkat yang menyediakan dan bertindak sebagai pengelola aplikasi, data, dan keamanannya.

**C. DES (Data Encryption Standard)**

DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci internal (internal key) atau upa-kunci (subkey). Kunci internal dibangkitkan dari kunci eksternal (external key) yang panjangnya 64 bit. 
![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/global.jpg)

**D.	OFB (Output FeedBack)**

Pada mode OFB, data dienkripsikan dalam unit yang lebih kecil daripada ukuran blok. Unit yang dienkripsikan dapat berupa bit per bit, 2 bit, 3 bit, dan seterusnya. Bila unit yang dienkripsikan satu karakter setiap kalinya, maka mode OFB-nya disebut OFB 8-bit. Secara umum OFB n-bit mengenkripsi plainteks sebanyak n bit setiap kalinya, yang mana n = m (m = ukuran blok). Mode OFB membutuhkan sebuah antrian (queue) yang berukuran sama dengan ukuran blok masukan.

## Implementasi
**A.	Tahap Pengiriman Pesan Antar Device**
-	Server membuat socket yang terdiri dari host dan port yang didefinisikan pada program, dan mengatur hanya 5 client yang bisa connect.

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/1a.PNG)

-	Server membuka koneksi ke socket

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/1b.PNG)

-	Client melakukan koneksi ke socket yang dibuka server

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/1c.PNG)

-	Client mengirimkan informasi ke server, dimana teks yang akan dikirim di enkripsi terllebih dahulu

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/1d.PNG)

-	Server menerima informasi yang dikirimkan oleh client, dimana informasi yang telah di enkripsi  sebelumnya didekripsi dulu sebelum sampai di server.

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/1e.PNG)

**B.	Tahap Enkripsi Dekripsi**

Adapun langkah-langkah implementasi algoritma DES dengan mode OFB adalah sebagai berikut :
- Mengubah plaintext dan key kedalam bentuk biner
- Melakukan Initial Permutation (IP) pada bit plaintext menggunakan tabel IP

  Contoh :

      Input biner           : 1	0	1	0	1

      Urutan bit plaintext  : [0]	[1]	[2]	[3]	[4]

      Urutan bit IP         : [4]	[0]	[3]	[1}	[2]

      Hasil                 : 1	1	0	0	1
  Kemudian pecah hasilnya menjadi dua bagian, yaitu L0 dan R0.
- Mengenerate kunci yang akan digunakan untuk mengenkripsi plaintext dengan menggunakan tabel permutasi kompresi PC-1, pada langkah ini terjadi kompresi dengan membuang 1 bit masing-masing blok kunci dari 64 bit menjadi 56 bit. Kemudian pecah hasilnya menjadi dua bagian, yaitu C0 dan D0.
- Melakukan pergeseran kiri (Left Shift) pada C0 dan D0, sebanyak jumlah pergeseran(kali putaran) yang telah ditentukan pada tabel.

  Selanjutnya, setiap hasil putaran digabungkan kembali menjadi CiDi dan diinput kedalam tabel Permutation Compression 2 (PC-2) dan data CiDi 56 bit dikompres menjadi CiDi 48 bit.
- Mengekspansi data Ri-1 32 bit menjadi Ri 48 bit sebanyak 16 kali putaran dengan nilai perputaran 1<= i <=16 menggunakan Tabel Ekspansi (E). 

  Selanjutnya, hasil dari ekspansi tersebut (Ri) di XOR kan dengan Ki sehingga menghasilkan nilai Ai yang mana akan diproses ditahap selanjutnya.
  
  Sedangkan nilai R1 yang digunakan untuk melanjutkan iterasi ke-2 didapatkan dari B1 (hasil proses f) yang kemudian dipermutasikan lagi dengan tabel P-Box dan menghasilkan nilai PB1 yang kemudian di XOR-kan dengan L0.
- Setiap Vektor Ai disubstitusikan kedelapan buah S-Box(Substitution Box), dimana blok pertama disubstitusikan dengan S1, blok kedua dengan S2 dan seterusnya dan menghasilkan output vektor Bi 32 bit.

  Misal kita ambil contoh S1, kemudian konversi setiap angka didalam tabel S1 menjadi biner.
  
  Lalu blok dipisah menjadi 2 yaitu:
  
    a. Bit pertama dan terakhir menunjukkan urutan baris
    
    b. Bit diantara pertama dan terakhir menunjukkan urutan kolom
    
  Kemudian dibandingkan dengan memeriksa perpotongan antara keduanya
  
  Misal kita ambil sampel blok bit pertama dari A1  misal 101101
  
      Input biner	: 1	0	1	1	0	1
      
      Urutan baris	: 1					1	(baris ke-3)
      
      Urutan kolom	: 	0	1	1	0		(kolom ke-6)
      
   Berdasarkan baris dan kolom yang ditunjuk, didapatkan nilai 0001 dan begitu seterusnya untuk blok kedua sampai blok kedelapan kita bandingkan dengan S2 hingga S8.

- Memutasikan bit vektor Bi menggunakan tabel P-Box, kemudian dikelompokkan menjadi 4 blok dimana tiap-tiap blok memiliki 32 bit data. 

  Hasil P(Bi) kemudian di XOR kan dengan Li-1 untuk mendapatkan nilai Ri. Dimana nilai Li diperoleh dari Nilai Ri-1 untuk nilai 1 <= i  <= 16.
- Mempermutasikan untuk terakhir kali dengan tabel Invers Initial Permutasi(IP-1)
- Hasil DES menjadi IV yang baru untuk enkripsi blok selanjutnya. Lalu hasil DES di XOR kan dengan plain text untuk menghasilkan chiper text.

# Testing
Client dan server dapat saling berkirim pesan seperti gambar berikut

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/d.png)

Pesan dari sender akan di enkrpisi terlebih dahulu sebelum dikirim ke receiver, dan receiver menerima pesan yang telah di dekripsi

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/c.png)

# Referensi : 
http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html
https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Initialization_vector_.28IV.29
http://rohmancahtkj.blogspot.co.id/2013/07/sniffer-adalah-program-yang-membaca-dan.html
https://id.wikipedia.org/wiki/Klien-server

