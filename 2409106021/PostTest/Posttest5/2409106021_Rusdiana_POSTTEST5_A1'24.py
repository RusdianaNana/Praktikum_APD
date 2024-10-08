# manajemen Film Dibioskop
# regis terlebih dahulu jika pengunjung
#login jika anda pegawai username:Pegawai, password:inipegawai
import os
daftar_film_list = [
    {'name': 'Lembayung', 'durasi': '2 minggu'},
    {'name': 'Sumala', 'durasi': '1 minggu'},
    {'name': 'Joker', 'durasi': '1 minggu'},
    {'name' : 'Laura', 'durasi' :'3 minggu'} 
    ]
users = [] 

while True:
    # # os.system('cls || clear')
    print("\n--- Menu ---")
    print("1. Registrasi")
    print("2. Login")
    menu = (input("\nPilih menu (1/2): "))
    if menu == "1":
         username = input("Masukkan username: ")
         password = input("Masukkan password: ")
         if any(user[0] == username for user in users):
             print("Username sudah terdaftar.")
             input("\nKlik enter untuk kembali ke menu...")
         else:
            users.append([username, password])
            print("Registrasi berhasil!, silahkan login")
            input("\nKlik enter untuk kembali ke menu...")
    elif menu == "2":
         username = input("Masukkan username: ")
         password = input("Masukkan password: ")
         user = next((u for u in users if u[0] == username and u[1] == password), None)
         if username == "pegawai" and password == "inipegawai":
              role = "pegawai"
              print("Selamat datang pegawai")
              input("\nKlik enter untuk masuk ke menu CRUD...")
              break
         elif user:
             role = "pengunjung"
             print(f"\nSelamat datang, {username}!")
             input("\nKlik enter untuk masuk ke menu pengunjung...")
             break
         else:
            print("Username atau password salah, silahkan registrasi terlebih dahulu.")
            input("\nKlik enter untuk kembali ke menu...")
    else:
        print("\nPilihan tidak valid.")
        input("\nKlik enter untuk melanjutkan...")


# Menu CRUD
while role:
    if role == "pegawai":
       # os.system('cls || clear')
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
==================================
"""
)
    elif role == "pengunjung":
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

    if role == "pegawai":
        if menu == '1':
            item_name = input("Masukkan nama film: ")
            item_durasi = input("Masukkan durasi penyewaan: ")
            daftar_film_list.append({'name': item_name, 'durasi': str(item_durasi)})
            print(f"daftar '{item_name}' dengan durasi {item_durasi} berhasil ditambahkan.")
            input("\nKlik enter untuk kembali ke menu...")
        elif menu == '2':
            if not daftar_film_list:
                print("Daftar Film Tidak Tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                # os.system('cls || clear')
                print("=== Daftar Film ===")
                for index, item in enumerate(daftar_film_list, start=1):
                    print(f"{index}. {item['name']} - {item['durasi']}")
                input("\nKlik enter untuk kembali ke menu...")
        elif menu == '3':
            if not daftar_film_list:
                print("Daftar Film Tidak Tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                # os.system('cls || clear')
                print("=== Daftar Film ===")
                for index, item in enumerate(daftar_film_list, start=1):
                    print(f"{index}. {item['name']} - {item['durasi']}")
                item_index = int(input("Masukkan nomor Filem yang ingin diubah: ")) - 1
                if 0 <= item_index < len(daftar_film_list):
                    new_name = input("Masukkan nama Film baru: ")
                    new_durasi = input("Masukkan durasi penyewaan: ")
                    daftar_film_list[item_index] = {'name': new_name, 'durasi': str(new_durasi)}
                    print(f"Film nomor {item_index + 1} berhasil diperbarui.")
                    input("\nKlik enter untuk kembali ke menu...")
                else:
                    print("\nFilm tidak ditemukan.")
                    input("\nKlik enter untuk kembali ke menu...")
        elif menu == '4':
            if not daftar_film_list:
                print("Daftar Film Tidak Tersedia.")
            else:
                # os.system('cls || clear')
                print("=== Daftar Film ===")
                for index, item in enumerate(daftar_film_list, start=1):
                    print(f"{index}. {item['name']} - {item['durasi']}")
                item_index = int(input("Masukkan nomor Film yang ingin dihapus: ")) - 1
                if 0 <= item_index < len(daftar_film_list):
                    removed_item = daftar_film_list.pop(item_index)
                    print(f"Film '{removed_item['name']}' berhasil dihapus.")
                    input("\nKlik enter untuk kembali ke menu...")
                else:
                    print("\nFilm tidak ditemukan.")
                    input("\nKlik enter untuk kembali ke menu...")
        elif menu == '5':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("\nKlik enter untuk mencoba lagi...")

    elif role == "pengunjung":
        if menu == '1':
            if not daftar_film_list:
                print("Daftar Film Tidak Tersedia.")
                input("\nKlik enter untuk kembali ke menu...")
            else:
                # os.system('cls || clear')
                print("=== Daftar Film ===")
                for index, item in enumerate(daftar_film_list, start=1):
                    print(f"{index}. {item['name']} - {item['durasi']}")
                input("\nKlik enter untuk kembali ke menu...")
        elif menu == '2':
                # os.system('cls || clear')
            print("=== Daftar Film ===")
            for index, item in enumerate(daftar_film_list, start=1):
                    print(f"{index}. {item['name']} - {item['durasi']}")
            item_index = int(input("Masukkan nomor film yang akan disewa (atau 0 untuk selesai): ")) - 1
            print(f"\nTotal penyewaan Anda adalah: {daftar_film_list[item_index]['durasi']}")
            input("\nKlik enter untuk kembali ke menu...")
        elif menu == '3':
            print("Keluar dari program.")
            print("\nTerima kasih telah menggunakan layanan dari kami")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")
            input("\nKlik enter untuk kembali ke menu...")


        
         
         
         
         
         
    
    
