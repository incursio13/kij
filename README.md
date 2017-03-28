# Implementasi Algoritma DES Dengan Mode Operasi OBF

Kelompok F09

- Andreas Galang Anugrah (5114100153)
- Riyadlatin Nufus (5114100151)
## Pendahuluan
Pada era globalisasi sekarang ini, keamanan dan kerahasian data pada jaringan komputer menjadi isu yang sangat penting dan terus berkembang. Kemajuan teknologi informasi tidak hanya menimbulkan dampak positif, melainkan juga dampak negatif. Kejahatan-kejahatan baru bermunculan, yang semula menggunakan teknik biasa, sekarang menggunakan metode dan teknik yang semakin canggih.

Berdasarkan kondisi tersebut, pengiriman data dan penyimpanan data melalui media elektronik memerlukan suatu proses yang dapat menjamin keamanan dan keutuhan dari data yang dikirimkan tersebut. Data tersebut harus tetap rahasia selama pengiriman dan harus tetap utuh pada saat penerimaan di tujuan. Untuk memenuhi hal tersebut, dilakukan proses penyandian (enkripsi dan dekripsi) terhadap data yang akan dikirimkan. 

Enkripsi dilakukan pada saat pengiriman dengan cara mengubah data asli menjadi data rahasia sedangkan dekripsi dilakukan pada saat penerimaan dengan cara mengubah data rahasia menjadi data asli. Jadi data yang dikirimkan selama proses pengiriman adalah data rahasia, sehingga data asli tidak dapat diketahui oleh pihak yang tidak berkepentingan. Data asli hanya dapat diketahui oleh penerima dengan menggunakan kunci rahasia.

Terdapat banyak algoritma untuk mengimplementasikan teknik enkripsi, salah satunya adalah DES (Data Encryption Standard), dan kali ini kita menggunakan mode operasi OBF (Output Feedback).


## Dasar Teori
**A. DES (Data Encryption Standard)**

DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci internal (internal key) atau upa-kunci (subkey). Kunci internal dibangkitkan dari kunci eksternal (external key) yang panjangnya 64 bit. 

**B.	OBF (Output Feedback)**

Pada mode OFB, data dienkripsikan dalam unit yang lebih kecil daripada ukuran blok. Unit yang dienkripsikan dapat berupa bit per bit, 2 bit, 3 bit, dan seterusnya. Bila unit yang dienkripsikan satu karakter setiap kalinya, maka mode OFB-nya disebut OFB 8-bit. Secara umum OFB n-bit mengenkripsi plainteks sebanyak n bit setiap kalinya, yang mana n = m (m = ukuran blok). Mode OFB membutuhkan sebuah antrian (queue) yang berukuran sama dengan ukuran blok masukan.

## Implementasi

