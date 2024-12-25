Enemy War UAS

Enemy War adalah game sederhana berbasis Python menggunakan library Pygame. Game ini merupakan proyek Ujian Akhir Semester (UAS) dengan konsep Object-Oriented Programming (OOP). Dalam game ini, pemain harus melawan musuh di setiap level hingga mencapai kemenangan.

A. Fitur

Pemain:

1. Bisa bergerak ke atas, bawah, kiri, dan kanan menggunakan tombol W, A, S, D.

2. Memiliki Health Points (HP).
   Musuh:
3. Bergerak mendekati pemain secara otomatis.

4. Memiliki HP yang bertambah sesuai level.
   Leveling:
5. Pemain naik level setelah mengalahkan musuh.

6. Game terdiri dari beberapa level dengan kesulitan yang meningkat.
   Obstacle:
   Obstacle seperti pohon, rumah, dan batu yang menghalangi gerakan pemain dan musuh.
   Game Over dan Win Screen:
7. Game berakhir jika HP pemain habis.

8. Pemain menang setelah menyelesaikan semua level.
   B. Cara Menjalankan Game

Persyaratan:

1. Python 3.x

2. Library Pygame
   Instalasi Pygame: Jalankan perintah berikut untuk menginstal Pygame:

pip install pygame

Clone Repository: Clone proyek ini ke komputer Anda: git clone https://github.com/mardlian030405/Enemy-War-UAS.git

Jalankan Game:

Pindah ke direktori proyek dan jalankan file utama:
cd Enemy-War-UAS
python main.py
Struktur Direktori

Enemy-War-UAS/ ├── assets/ # Folder berisi gambar untuk pemain, musuh, dan obstacle │ ├── player.png │ ├── enemy_level_1.png │ ├── enemy_level_2.png │ ├── pohon.png │ ├── rumah.png │ ├── batu.png ├── main.py # File utama untuk menjalankan game └── README.md # Dokumentasi proyek

C. Kontrol

    W: Bergerak ke atas

    A: Bergerak ke kiri

    S: Bergerak ke bawah

    D: Bergerak ke kanan