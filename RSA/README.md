# Implementasi Algoritma RSA pada Enkripsi Dekripsi Pesan

Kelompok F09

- Riyadlatin Nufus (5114100151)
- Andreas Galang Anugrah (5114100153)
## Pendahuluan
Pada era globalisasi sekarang ini, keamanan dan kerahasiaan data pada jaringan komputer menjadi isu yang sangat penting dan terus berkembang. Kemajuan teknologi informasi tidak hanya menimbulkan dampak positif, melainkan juga dampak negatif. Kejahatan-kejahatan baru bermunculan, yang semula menggunakan teknik biasa, sekarang menggunakan metode dan teknik yang semakin canggih.

Berdasarkan kondisi tersebut, pengiriman data dan penyimpanan data melalui media elektronik memerlukan suatu proses yang dapat menjamin keamanan dan keutuhan dari data yang dikirimkan tersebut. Data tersebut harus tetap rahasia selama pengiriman dan harus tetap utuh pada saat penerimaan di tujuan. Untuk memenuhi hal tersebut, dilakukan proses penyandian (enkripsi dan dekripsi) terhadap data yang akan dikirimkan. 

Enkripsi dilakukan pada saat pengiriman dengan cara mengubah data asli menjadi data rahasia sedangkan dekripsi dilakukan pada saat penerimaan dengan cara mengubah data rahasia menjadi data asli. Jadi data yang dikirimkan selama proses pengiriman adalah data rahasia, sehingga data asli tidak dapat diketahui oleh pihak yang tidak berkepentingan. Data asli hanya dapat diketahui oleh penerima dengan menggunakan kunci rahasia.

Terdapat banyak algoritma untuk mengimplementasikan teknik enkripsi dekripsi, salah satunya adalah RSA, dimana kunci yang digunakan untuk mengenkripsi berbeda dengan yang digunakan untuk mendekripsi. Kunci yang digunakan untuk mengenkripsi disebut dengan kunci public, dan yang digunakan untuk mendekripsi disebut dengan kunci privat, sehingga dengan begitu maka  pengiriman pesan akan lebih aman.

## Dasar Teori
**A. RSA**

RSA adalah salah satu algoritma kriptografi yang menggunakan konsep kriptografi kunci publik. RSA membutuhkan tiga langkah dalam prosesnya, yaitu pembangkitan kunci, enkripsi, dan dekripsi. Proses enkripsi dan dekripsi merupakan proses yang hampir sama. Jika bilangan acak yang dibangkitkan kuat, maka akan lebih sulit untuk melakukan cracking terhadap pesan. Parameter kuat tidaknya suatu kunci terdapat pada besarnya bilangan acak yang digunakan.

**B.  Digital Signature**

Digital Signature adalah bentuk tiruan tanda tangan konvensional ke dalam bentuk digital. Tetapi bukan file scan tanda tangan dikertas. Sebutan digital signature ini sebenarnya konsep. Dalam dunia nyata, tanda tangan digital itu bentuknya adalah rangkaian byte-byte yang jika diperiksa bisa digunakan untuk memeriksa apakah suatu dokumen digital, juga termasuk email, benar berasal dari orang tertentu atau tidak.

**C.  Client Server**

Client Server adalah suatu bentuk arsitektur dimana client adalah perangkat yang menerima yang akan menampilkan dan menjalankan aplikasi (software komputer) dan server adalah perangkat yang menyediakan dan bertindak sebagai pengelola aplikasi, data, dan keamanannya.

**D. Sniffer**

Sniffer adalah membaca dan menganalisa setiap protokol yang melewati mesin di mana program tersebut diinstal. Secara default, sebuah komputer dalam jaringan (workstation) hanya mendengarkan dan merespon paket-paket yang dikirimkan kepada mereka. Namun demikian, kartu jaringan (network card) dapat diset oleh beberapa program tertentu, sehingga dapat memonitor dan menangkap semua lalu lintas jaringan yang lewat tanpa peduli kepada siapa paket tersebut dikirimkan. Aktifitasnya biasa disebut dengan sniffing.

Setelah host attacker menjadi host yang berada di tengah-tengah dari dua host yang saling berkomunikasi, kemudian attacker melakukan analisa traffic dengan menjalankan program ethereal. Dengan menganalisa traffic TCP yang sudah tercapture, attacker dapat mengetahui apa saja yang dilakukan oleh host client terhadap host server.

## Implementasi
**A. Pembuatan kunci publik dan privat**
- Memilih 2 buah bilangan prima p dan q.

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/1.PNG)

- Menghitung nilai n = p * q.

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/2.PNG)

- Menghitung nilai m = (p-1) * (q-1). 

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/3.PNG)

- Mencari nilai e , dimana e merupakan relatif prima dari m. 

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/4.PNG)

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/4a.PNG)

- Mencari nilai d , yang memenuhi persamaan ed ≡ 1 mod m atau d = e-1 mod m. 

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/5a.PNG)

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/5b.PNG)

- Kunci public (e , n) dan kunci private (d , n). 

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/6.PNG)

**B. Pengiriman pesan**
- Sebelum pengirim mengirimkan pesan, pengirim terlebih dahulu membuat digital signature dengan cara mengambil nilai hash dari pesan/data. Fungsi hash yang dipakai yaitu MD5, lalu mengenkrip nilai hash tersebut dengan algoritma enkripsi RSA. Hasil enkripsi hash dengan private key pengirim inilah yang disebut digital signature.

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/b1.PNG)

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/b2.PNG)

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/b3.PNG)

- Pengirim mengenkripsi pesan dengan kunci publik dan mengirimkannya. Adapun fungsi dekripsi adalah C = M^e mod n

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/b4.PNG)

- Penerima melakukan verifikasi digital signature terlebih dahulu, verifikasi dilakukan dengan mendekrip digital signature pesan tersebut dengan public key pengirim kemudian dicocokkan dengan nilai hash bagian pesan/data. Jika hasilnya sama berarti digital signature dianggap valid.

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/bb1.PNG)

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/bb2.PNG)

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/bb3.PNG)

- Penerima menerima pesan dan mendekripnya dengan kunci privat nya. Adapun fungsi dekripsi adalah M = C^d mod n

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/bb4.PNG)

# Testing
Client dan server dapat saling berkirim pesan seperti gambar berikut

Client mengirim pesan kepada server

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/client.PNG)

Server menerima pesan dan membalas pesan client

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/server.PNG)

# Referensi : 
http://ezine.echo.or.id/ezine19/e19.004.txt
http://sonyvinda.blogspot.co.id/2010/04/enkripsi-menggunakan-algoritma-rsa.html
https://id.wikipedia.org/wiki/RSA#Padding_schemes
http://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
http://octarapribadi.blogspot.co.id/2016/02/enkripsi-dan-dekripsi-menggunakan-rsa.html
