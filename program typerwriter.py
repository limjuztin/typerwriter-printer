import msvcrt#sebagai pendeteksi keyboard
import time #memasukan library time agar dapat menggunakan sleep(fungsinya untuk menunda proses berdasarkan waktu)
def typerwriter(teks:str,sleep=0.04):#fungsi untuk mencetak teks secara bergilir
    if not isinstance(teks,str) or not(teks.strip()):#mengecek jika teks yang ingin dicetak adalah teks dan tidak kosong
        return False
    skip=False
    for indeks,huruf in enumerate(teks):
        if msvcrt.kbhit():#memeriksa jika ada input keyboard saat pencetakan
            tombol=msvcrt.getch()#sebagai variabel yang menyimpan input keyboard
            if tombol== b" ":#jika pengguna menginput space  maka akan memicu skip
                skip=True
            if skip:
                print(teks[indeks:],end="")
                break
        print(huruf,end="")
        time.sleep(sleep)
    print()
    
typerwriter("halo semuanya ,saya developer baru? entahlah aku hanya iseng saja dalam melakukan ini, karena aku cuman mau latihan pemograman yang belum tahu kegunaanku nanti, ya setidaknya aku akan berusaha untuk bekerja sesuai dengan skill. kalau gk tinggal ngojek atau demo pemerintah awokawokawokaqwok.")
