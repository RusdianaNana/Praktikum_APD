usn = input("buatlah username dengan nama panggilan anda :")
pw = int(input("buatlah password dengan 3 digit NIM terakhir anda :"))
batas_login = 3

while batas_login > 0:
    username = input("masukkan username anda :")
    password = int(input("masukkan password anda: "))
    if username == usn and password == pw:
        print ("proses login berhasil")
        break
    elif batas_login > 1:
        print("proses login gagal, silahkan coba lagi")
    else:
        print("login gagal, karena anda salah teros")
    batas_login -=1

        
if batas_login == 0:
    print("silahkan coba lagi lain waktu")
else:
    
    while True:
        print("Pilih Jenis Kelamin:")
        print("1. Pria")
        print("2. Wanita")

        pilihan_kelamin = input("Pilihan (1/2): ")
        if pilihan_kelamin == "1":
            jenis_kelamin = "pria"
        elif pilihan_kelamin == "2":
            jenis_kelamin = "wanita"
        else:
            print("Pilihan tidak valid.")

    # Input data pengguna
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi = float(input("Masukkan tinggi badan (cm): "))
        umur = int(input("Masukkan umur (tahun): "))

    # Memilih level kegiatan harian
        print("Level kegiatan Harian:")
        print("1. kegiatan Minimal (jarang bergerak)")
        print("2. kegiatan Sedang (olahraga 1-3 kali seminggu)")
        print("3. kegiatan Tinggi (olahraga 4-7 kali seminggu)")
        pilihan_kegiatan = input("Pilihan (1/2/3): ")
        
        if pilihan_kegiatan == "1":
            level_kegiatan = 1.25
        elif pilihan_kegiatan == "2":
            level_kegiatan = 1.36
        elif pilihan_kegiatan == "3":
            level_kegiatan = 1.72
        else:
            print("Pilihan tidak valid.")

    # Menghitung BMR dan TDEE
        if jenis_kelamin == "pria":
            bmr = (10 * berat) + (6.25 * tinggi) - (5 * umur) + 5
            tdee = (bmr * level_kegiatan)
        else:
            bmr = (10 * berat) + (6.25 * tinggi) - (5 * umur) - 161
            tdee = (bmr * level_kegiatan)
    
    # Menampilkan hasil
        print(f"\nBMR Anda: {bmr:.2f} kalori/hari")
        print(f"TDEE Anda: {tdee:.2f} kalori/hari")
        
        berhenti = input("apakah anda ingin memulai lagi? (iya/tidak): ")
        if berhenti == "tidak":
            print("Terima Kasih!")
            break