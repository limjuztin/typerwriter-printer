# typerwriter-printer
projek sederhana pembuatan fungsi typerwriter pada python yang masih dikhususkan untuk windows
Proyek sederhana pembuatan fungsi *typewriter* pada Python yang masih dikhususkan untuk Windows.

Halo semuanya, ini saya **limjuztin** sebagai orang iseng yang sedang melatih pemrograman. Ini adalah proyek pertama saya di GitHub. Di sini saya membuat generalisasi fungsi untuk mencetak teks dengan gaya *typewriter* ala dialog game RPG—lengkap dengan kustomisasi kecepatan cetak dan fitur *skip* instan menggunakan tombol **Spasi** di keyboard.

## Tujuan Proyek
- Melatih dasar pemrograman Python secara praktis.
- Menggeneralisasi fungsi *typewriter* agar mudah dipakai ulang.
- Membantu pengguna lain yang ingin menerapkan efek *typewriter* pada proyek mereka.

## Library yang Digunakan
- `msvcrt` : Mendeteksi input tombol keyboard khusus di lingkungan Windows.
- `time` (`time.sleep`) : Menahan/menunda proses pencetakan selama jeda waktu tertentu.

## Alur Kerja Program
1. Pengguna memasukkan teks yang ingin ditampilkan.
2. Teks diteruskan ke dalam fungsi *typewriter*.
3. Fungsi memvalidasi apakah input benar-benar bertipe `str` (string) dan tidak kosong.
4. Pencetakan berjalan huruf demi huruf menggunakan perulangan `for` dengan jeda waktu yang sudah ditentukan.
5. Di setiap iterasi perulangan, program mengecek apakah ada tombol keyboard yang ditekan.
6. Jika tombol **Spasi** ditekan, sisa teks langsung dicetak sekaligus tanpa jeda.
7. Jika tombol **Spasi** tidak ditekan, pencetakan berlanjut berurutan hingga selesai.

## Catatan & Batasan
> **Catatan:** Implementasi saat ini masih berfokus pada sistem operasi **Windows** (karena memakai `msvcrt`).

- [x] Efek *typewriter* dasar dengan jeda yang dapat dikustomisasi
- [x] Fitur *skip* cepat menggunakan tombol **Spasi**
- [ ] Versi Bahasa Inggris (*English version*)
- [ ] Dukungan lintas platform (*Linux/macOS*)

Terima kasih sudah mampir. Jika ada bagian yang kurang tepat atau bisa ditingkatkan, silakan beri kritik dan saran.
