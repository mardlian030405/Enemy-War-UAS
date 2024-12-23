Enemy War UAS

Enemy War adalah game sederhana berbasis Python menggunakan library Pygame. Game ini merupakan proyek Ujian Akhir Semester (UAS) dengan konsep Object-Oriented Programming (OOP). Dalam game ini, pemain harus melawan musuh di setiap level hingga mencapai kemenangan.

A. Fitur

  1. Pemain:
  
    1) Bisa bergerak ke atas, bawah, kiri, dan kanan menggunakan tombol W, A, S, D.
  
    2) Memiliki Health Points (HP).
  
  2. Musuh:
  
    1) Bergerak mendekati pemain secara otomatis.
    
    2) Memiliki HP yang bertambah sesuai level.
  
  3. Leveling:
  
    1) Pemain naik level setelah mengalahkan musuh.
    
    2) Game terdiri dari beberapa level dengan kesulitan yang meningkat.
  
  4. Obstacle:
  
    Obstacle seperti pohon, rumah, dan batu yang menghalangi gerakan pemain dan musuh.
  
  5. Game Over dan Win Screen:
  
    1) Game berakhir jika HP pemain habis.
    
    2) Pemain menang setelah menyelesaikan semua level.

B. Cara Menjalankan Game

  1. Persyaratan:
  
    1) Python 3.x
    
    2) Library Pygame
  
  2. Instalasi Pygame:
     Jalankan perintah berikut untuk menginstal Pygame:
  
  3. pip install pygame
  
  4. Clone Repository:
     Clone proyek ini ke komputer Anda:
     git clone https://github.com/mardlian030405/Enemy-War-UAS.git
  
  5. Jalankan Game:
      1) Pindah ke direktori proyek dan jalankan file utama:
      2) cd Enemy-War-UAS
      3) python main.py

Struktur Direktori

Enemy-War-UAS/
├── assets/         # Folder berisi gambar untuk pemain, musuh, dan obstacle
│   ├── player.png
│   ├── enemy_level_1.png
│   ├── enemy_level_2.png
│   ├── pohon.png
│   ├── rumah.png
│   ├── batu.png
├── main.py         # File utama untuk menjalankan game
└── README.md       # Dokumentasi proyek

C. Kontrol

  W: Bergerak ke atas
  
  A: Bergerak ke kiri
  
  S: Bergerak ke bawah
  
  D: Bergerak ke kanan
