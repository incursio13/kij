# Implementasi Diffie-Hellman Key Exchange pada DES

Kelompok F09

- Riyadlatin Nufus (5114100151)
- Andreas Galang Anugrah (5114100153)
## Pendahuluan
Pada era globalisasi sekarang ini, keamanan dan kerahasiaan data pada jaringan komputer menjadi isu yang sangat penting dan terus berkembang. Kemajuan teknologi informasi tidak hanya menimbulkan dampak positif, melainkan juga dampak negatif. Kejahatan-kejahatan baru bermunculan, yang semula menggunakan teknik biasa, sekarang menggunakan metode dan teknik yang semakin canggih.

Berdasarkan kondisi tersebut, pengiriman data dan penyimpanan data melalui media elektronik memerlukan suatu proses yang dapat menjamin keamanan dan keutuhan dari data yang dikirimkan tersebut. Data tersebut harus tetap rahasia selama pengiriman dan harus tetap utuh pada saat penerimaan di tujuan. Untuk memenuhi hal tersebut, dilakukan proses penyandian (enkripsi dan dekripsi) terhadap data yang akan dikirimkan. 

Enkripsi dilakukan pada saat pengiriman dengan cara mengubah data asli menjadi data rahasia sedangkan dekripsi dilakukan pada saat penerimaan dengan cara mengubah data rahasia menjadi data asli. Jadi data yang dikirimkan selama proses pengiriman adalah data rahasia, sehingga data asli tidak dapat diketahui oleh pihak yang tidak berkepentingan. Data asli hanya dapat diketahui oleh penerima dengan menggunakan kunci rahasia.

Terdapat banyak algoritma untuk mengimplementasikan teknik enkripsi, salah satunya adalah DES (Data Encryption Standard), dan kali ini kita menggunakan mode operasi OFB (Output FeedBack), dimana key yang digunakan yaitu key baru yang dibuat, artinya tidak menggunakan kunci yang dibagikan sebelumnya.


## Dasar Teori
**A. Diffie-Hellman**

Diffie-Hellman key exchange adalah metode dimana subyek menukar kunci rahasia melalui media yang tidak amantanpa mengekspos kunci. Metode ini diperlihatkan oleh Dr. W. Diffie dan Dr. M. E. Hellman pada tahun 1976 pada papernya “New Directions in Cryptography”. Metode ini memungkinkan dua pengguna untuk bertukar kunci rahasia melalui media yang tidak aman tanpa kunci tambahan.

Algoritma  ini  tidak  berdasarkan  pada  proses  enkripsi dan  dekripsi,  melainkan  lebih  kepada  proses  matematika yang  dilakukan  untuk  menghasilkan  kunci  rahasia  yang dapat  disebarkan  secara  bebas  tanpa  harus  khawatir karena  kunci  rahasia  tersebut  hanya  dapat  didekripsi hanya  oleh  pengirim  dan  penerima  pesan.  Dasar  dari algoritma  ini  adalah  matematika  dasar  dari  aljabar eksponen dan aritmatika modulus.

**B.  Client Server**

Client Server adalah suatu bentuk arsitektur dimana client adalah perangkat yang menerima yang akan menampilkan dan menjalankan aplikasi (software komputer) dan server adalah perangkat yang menyediakan dan bertindak sebagai pengelola aplikasi, data, dan keamanannya.

**C. DES (Data Encryption Standard)**

DES termasuk ke dalam sistem kriptografi simetri dan tergolong jenis cipher blok. DES beroperasi pada ukuran blok 64 bit. DES mengenkripsikan 64 bit plainteks menjadi 64 bit cipherteks dengan menggunakan 56 bit kunci internal (internal key) atau upa-kunci (subkey). Kunci internal dibangkitkan dari kunci eksternal (external key) yang panjangnya 64 bit. 
![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/global.jpg)

**D.  OFB (Output FeedBack)**

Pada mode OFB, data dienkripsikan dalam unit yang lebih kecil daripada ukuran blok. Unit yang dienkripsikan dapat berupa bit per bit, 2 bit, 3 bit, dan seterusnya. Bila unit yang dienkripsikan satu karakter setiap kalinya, maka mode OFB-nya disebut OFB 8-bit. Secara umum OFB n-bit mengenkripsi plainteks sebanyak n bit setiap kalinya, yang mana n = m (m = ukuran blok). Mode OFB membutuhkan sebuah antrian (queue) yang berukuran sama dengan ukuran blok masukan.

## Implementasi
Adapun langkah implementasi Diffie-Hellman key exchange pada DES adalah sebagai berikut:
- Memilih  bilangan prima  yang  besar, q
  dan  bilangan integer  yang  tidak  melebihi  dari  nilai  q, a dimana kedua bilangan tersebut diketahui secara publik.
      
      def primesfrom3to(self):
              n=5000
              assert n>=2
              sieve = np.ones(n/2, dtype=np.bool)
              for i in xrange(3,int(n**0.5)+1,2):
                  if sieve[i/2]:
                      sieve[i*i/2::i] = False
              z= np.r_[2, 2*np.nonzero(sieve)[0][1::]+1] 
              temp = random.randint(95,len(z))
              self.q= z[temp]
              
        self.a = 3
        self.primesfrom3to()
        self.client.send(str(self.a)) 
        self.client.send(str(self.q))
        
- Server memilih sebuah  bilangan  acak, Xa dimana bilangan ini tidak boleh diketahui oleh orang lain.
     
      self.XA = random.randint(1,self.q-1)

- Client memilih sebuah  bilangan  acak, Xb dimana bilangan ini tidak boleh diketahui oleh orang lain.

      XB = random.randint(1,q-1)

- Pengirim menghitung  Ya = a^Xa mod  q.  Bilangan  Ya ini dapat diketahui secara publik.

      self.YA = pow(self.a,self.XA)%self.q
      self.client.send(str(self.YA))

- Penerima menghitung  Yb = a^Xb mod  q.  Bilangan  Yb ini dapat diketahui secara publik.

      YB = pow(a,XB)%q

- Lakukan pertukaran bilangan Ya dan  Yb  terhadap client dan server.
- Kemudian Server menghitung key = Yb^Xa mod q.

      self.key = str(pow(self.YB,self.XA) % self.q)

- Client menghitung key = Ya^Xb mod q.
         
      key = str(pow(YA,XB)%q)
      
- Sehingga client dan server mendapatkan nilai key yang sama.

# Testing
Client dan server dapat saling berkirim pesan seperti gambar berikut

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/d.png)

Pesan dari sender akan di enkrpisi terlebih dahulu sebelum dikirim ke receiver, dan receiver menerima pesan yang telah di dekripsi

![alt_tag](https://github.com/incursio13/kij/blob/master/Doc/c.png)

# Referensi : 
http://octarapribadi.blogspot.co.id/2012/10/contoh-enkripsi-dengan-algoritma-des.html
https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Initialization_vector_.28IV.29
https://id.wikipedia.org/wiki/Klien-server
http://kuliah-hhn.blogspot.co.id/2012/05/cara-kerja-protokol-pertukaran-kunci.html

