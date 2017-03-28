# Implementasi Algoritma DES Dengan Mode Operasi OFB

Kelompok F09

- Andreas Galang Anugrah (5114100153)
- Riyadlatin Nufus (5114100151)
## Pendahuluan
Pada era globalisasi sekarang ini, keamanan dan kerahasiaan data pada jaringan komputer menjadi isu yang sangat penting dan terus berkembang. Kemajuan teknologi informasi tidak hanya menimbulkan dampak positif, melainkan juga dampak negatif. Kejahatan-kejahatan baru bermunculan, yang semula menggunakan teknik biasa, sekarang menggunakan metode dan teknik yang semakin canggih.

Berdasarkan kondisi tersebut, pengiriman data dan penyimpanan data melalui media elektronik memerlukan suatu proses yang dapat menjamin keamanan dan keutuhan dari data yang dikirimkan tersebut. Data tersebut harus tetap rahasia selama pengiriman dan harus tetap utuh pada saat penerimaan di tujuan. Untuk memenuhi hal tersebut, dilakukan proses penyandian (enkripsi dan dekripsi) terhadap data yang akan dikirimkan. 

Enkripsi dilakukan pada saat pengiriman dengan cara mengubah data asli menjadi data rahasia sedangkan dekripsi dilakukan pada saat penerimaan dengan cara mengubah data rahasia menjadi data asli. Jadi data yang dikirimkan selama proses pengiriman adalah data rahasia, sehingga data asli tidak dapat diketahui oleh pihak yang tidak berkepentingan. Data asli hanya dapat diketahui oleh penerima dengan menggunakan kunci rahasia.

Terdapat banyak algoritma untuk mengimplementasikan teknik enkripsi, salah satunya adalah DES (Data Encryption Standard), dan kali ini kita menggunakan mode operasi OFB (Output FeedBack).


## Dasar Teori
**A. DES (Data Encryption Standard)**

DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci internal (internal key) atau upa-kunci (subkey). Kunci internal dibangkitkan dari kunci eksternal (external key) yang panjangnya 64 bit. 

**B.	OFB (Output FeedBack)**

Pada mode OFB, data dienkripsikan dalam unit yang lebih kecil daripada ukuran blok. Unit yang dienkripsikan dapat berupa bit per bit, 2 bit, 3 bit, dan seterusnya. Bila unit yang dienkripsikan satu karakter setiap kalinya, maka mode OFB-nya disebut OFB 8-bit. Secara umum OFB n-bit mengenkripsi plainteks sebanyak n bit setiap kalinya, yang mana n = m (m = ukuran blok). Mode OFB membutuhkan sebuah antrian (queue) yang berukuran sama dengan ukuran blok masukan.

## Implementasi
Adapun langkah-langkah implementasi algoritma DES dengan mode OFB adalah sebagai berikut :
- Mengubah plaintext dan key kedalam bentuk biner
- Melakukan Initial Permutation (IP) pada bit plaintext menggunakan tabel IP

  Contoh :

      Input biner           : 1	0	1	0	1

      Urutan bit plaintext  : [0]	[1]	[2]	[3]	[4]

      Urutan bit IP         : [4]	[0]	[3]	[1}	[2]

      Hasil                 : 1	1	0	0	1
- Mengenerate kunci yang akan digunakan untuk mengenkripsi plaintext dengan menggunakan tabel permutasi kompresi PC-1, pada langkah ini terjadi kompresi dengan membuang 1 bit masing-masing blok kunci dari 64 bit menjadi 56 bit. Kemudian pecah hasilnya menjadi dua bagian, yaitu C0 dan D0.
- Melakukan pergeseran kiri (Left Shift) pada C0 dan D0, sebanyak jumlah pergeseran(kali putaran) yang telah ditentukan pada tabel.Selanjutnya, setiap hasil putaran digabungkan kembali menjadi CiDi dan diinput kedalam tabel Permutation Compression 2 (PC-2) dan data CiDi 56 bit dikompres menjadi CiDi 48 bit.
- Mengekspansi data Ri-1 32 bit menjadi Ri 48 bit sebanyak 16 kali putaran dengan nilai perputaran 1<= i <=16 menggunakan Tabel Ekspansi (E). 

  Selanjutnya, hasil dari ekspansi tersebut (Ri) di XOR kan dengan Ki sehingga menghasilkan nilai Ai .
- Setiap Vektor Ai disubstitusikan kedelapan buah S-Box(Substitution Box), dimana blok pertama disubstitusikan dengan S1, blok kedua dengan S2 dan seterusnya dan menghasilkan output vektor Bi 32 bit.
- Memutasikan bit vektor Bi menggunakan tabel P-Box, kemudian dikelompokkan menjadi 4 blok dimana tiap-tiap blok memiliki 32 bit data. 

  Hasil P(Bi) kemudian di XOR kan dengan Li-1 untuk mendapatkan nilai Ri. Dimana nilai Li diperoleh dari Nilai Ri-1 untuk nilai 1 <= i  <= 16.
- Mempermutasikan untuk terakhir kali dengan tabel Invers Initial Permutasi(IP-1)
- Hasil DES menjadi IV yang baru untuk enkripsi blok selanjutnya. Lalu hasil DES di XOR kan dengan plain text untuk menghasilkan chiper text.


