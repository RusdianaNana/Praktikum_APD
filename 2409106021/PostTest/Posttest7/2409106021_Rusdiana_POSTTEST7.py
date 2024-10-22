# manajemen Film Dibioskop
# regis terlebih dahulu jika pengunjung
#login jika anda pegawai username:Pegawai, password:inipegawai
import os
daftar_film_list = {
     'Lembayung' : '2 minggu',
     'Sumala' : '1 minggu',
     'Joker' : '1 minggu',
     'Laura'  :'3 minggu'
    }
users = { }
role = None
admin_username = "pegawai"
admin_password  = "inipegawai"

#FUNGSI REGISTRASI DAN LOGIN
def input_login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if not username or not password:
        print("Username dan password tidak boleh kosong")
        return input_login()
    return username, password
def input_registrasi():
    username = input("Masukkan username baru: ")
    password = input("Masukkan password baru: ")
    if not username or not password:
        print("Username dan password tidak boleh kosong")
        return input_registrasi
    return username, password

def registrasi_user():
    username, password = input_registrasi()
    if  username in users:
        print("Registrasi gagal! Username sudah ada")
    else:
        users[username] = password
        print ("Registrasi berhasil! Anda dapat login sekarang")

def verifikasi_login_admin(username, password):
    return username == admin_username and password == admin_password
def verifikasi_login_user(username, password):
    return username  in users and users[username] == password
def tampilkan_pesan_login(role, valid):
    if valid:
        print(f"Login berhasil! Selamat datang {username}")
    else:
        print("Username atau password yang dimasukkan salah, atau silahkan registrasi terlebih dahulu")
    return role


#FUNGSI MENU PEGAWAI
def menambah():
    item_name = input("Masukkan nama film: ")
    item_durasi = input("Masukkan durasi penyewaan: ")
    daftar_film_list[item_name] = item_durasi
    print(f"daftar '{item_name}' dengan durasi {item_durasi} berhasil ditambahkan.")
    input("\nKlik enter untuk kembali ke menu...")
    
def tampilkan():
    if not daftar_film_list:
        print("Daftar Film Tidak Tersedia.")
        input("\nKlik enter untuk kembali ke menu...")
    else:
    # os.system('cls || clear')
        print("=== Daftar Film ===")
        for index, (film, durasi) in enumerate(daftar_film_list.items(), start=1):
            print(f"{index}. {film} - {durasi}")
        # input("\nKlik enter untuk kembali ke menu...")

def mengubah():
    tampilkan()
    global  daftar_film_list
    if not daftar_film_list:
        print("Daftar Film Tidak Tersedia.")
        input("\nKlik enter untuk kembali ke menu...")
    
    while  True:
        try:
            item_index = int(input("Masukkan nomor Filem yang ingin diubah: ")) - 1
            if 0 <= item_index < len(daftar_film_list):
                new_name = input("Masukkan nama Film baru: ")
                new_durasi = input("Masukkan durasi penyewaan: ")
                daftar_film_list = list(daftar_film_list.items())
                daftar_film_list[item_index]=(new_name,new_durasi)
                daftar_film_list = dict(daftar_film_list)
                print(f"Film nomor {item_index + 1} berhasil diperbarui.")
                input("\nKlik enter untuk kembali ke menu...")
                return
            else:
                print("\nFilm tidak ditemukan.")
                input("\nKlik enter untuk kembali ke menu...")
                return mengubah()
        except ValueError:
            print("Anda harus memasukkan angka.")
            return mengubah()
            

def menghapus():
    tampilkan()
    global  daftar_film_list
    if not daftar_film_list:
        print("Daftar Film Tidak Tersedia.")
        return
    while  True:
        try:
             # os.system('cls || clear')
            item_index = int(input("Masukkan nomor Film yang ingin dihapus: ")) - 1
            if 0 <= item_index < len(daftar_film_list):
                daftar_film_list = list(daftar_film_list.items())
                removed_item = daftar_film_list.pop(item_index)
                daftar_film_list = dict(daftar_film_list)
                print(f"Film {item_index +1} berhasil dihapus.")
                input("\nKlik enter untuk kembali ke menu...")
                return
            else:
                print("\nFilm tidak ditemukan.")
                input("\nKlik enter untuk kembali ke menu...")
                return menghapus()
        except  ValueError:
            print("Anda harus memasukkan angka.")
            return menghapus()

def keluar():
    print("Keluar dari menu pegawai.")
    role = None

while True:
    # # os.system('cls || clear')
    print("\n--- Menu ---")
    print("1. Registrasi")
    print("2. Login")
    print("3. Exit")
    menu = (input("\nPilih menu (1/2/3): "))
    if menu == "1":
        registrasi_user()
        input("\nklik enter untuk login")
    elif menu == "2":
        username,  password = input_login()
        if verifikasi_login_admin(username, password):
            role ="pegawai"
            tampilkan_pesan_login(role, True)
            input("\nklik enter untuk masuk ke menu CRUD")
        
        elif verifikasi_login_user(username, password):
            role = "pengunjung"
            tampilkan_pesan_login(role, True)
            input("\nKlik enter untuk masuk ke menu pengunjung...")
        else:
            tampilkan_pesan_login("", False)
            input("\nKlik enter untuk kembali ke menu...")
    elif menu == "3":
            print("="*50)
            print("Ada telah keluar dari program".center(45))
            print("\nTerima kasih telah menggunakan layanan dari kami".center(40))
            print("Sampai jumpa lagi".center(45))
            print("="*50)
            break
    else:
        print("\nPilihan tidak valid.")
        input("\nKlik enter untuk melanjutkan...")

# Menu CRUD

    while role == "pegawai":
            print(
            """
            ===================================
            |            MENU FILM            |
            ===================================
            |    1. TAMBAH DAFTAR FILM        |
            |    2. TAMPILKAN DAFTAR FILM     | 
            |    3. UBAH DAFTAR FILM          |
            |    4. HAPUS DAFTAR FILM         |
            |    5. KELUAR                    |
            ===================================
            """
            )
            menu = input("Pilih opsi: ")
            if menu == '1':
                menambah()
                
            elif menu == '2':
                tampilkan()
                    
            elif menu == '3':
                mengubah()   
                
            elif menu == '4':
                menghapus()
 
            elif menu == '5':
                keluar()
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
                input("\nKlik enter untuk mencoba lagi...")

    while role == "pengunjung":
       # os.system('cls || clear')
        print(
"""
===================================
|              MENU               |
===================================
|   1. TAMPILKAN DAFTAR FILM      |
|   2. PENYEWAAN LISENSI          |
|   3. KELUAR                     |  
===================================
"""
)

        menu = input("Pilih opsi: ")
        if menu == '1':
                tampilkan()
                input("\nKlik enter untuk kembali ke menu...")
        elif menu == '2':
        # Loop untuk menu penyewaan
            sudah_menyewa = False  # Reset status penyewaan
            while not sudah_menyewa:
                # os.system('cls || clear')
                print("=== DAFTAR FILM UNTUK PENYEWAAN ===")
                for index, (film, durasi) in enumerate(daftar_film_list.items(), start=1):
                    print(f"{index}. {film} - {durasi}")
                item_index = int(input("Masukkan nomor film yang akan disewa (atau 0 untuk kembali ke menu utama): ")) - 1
                if item_index == -1:  # Jika pengguna memilih untuk kembali
                    break
                
                if 0 <= item_index < len(daftar_film_list):
                    film_yang_disewa = list(daftar_film_list.keys())[item_index]
                    durasi_film_disewa = list(daftar_film_list.values())[item_index]
                    print(f"\nAnda telah menyewa film: {film_yang_disewa}:{durasi_film_disewa}")
                    sudah_menyewa = True  # Tandai bahwa pengguna sudah menyewa
                    input("\nKlik enter untuk kembali ke menu utama...")
                else:
                    print("Pilihan tidak valid. Silakan coba lagi.")
                    input("\nKlik enter untuk kembali ke menu penyewaan...")
            else:
                continue
        elif menu == '3':
            role = None
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("\nKlik enter untuk kembali ke menu...")