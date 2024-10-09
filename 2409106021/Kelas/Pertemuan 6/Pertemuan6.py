# # # daftar_Buku = {
# # #     "Buku1" : "Harry Poter",
# # #     "Buku2" : "Percy jackson",
# # #     "Buku3" : "Twilght"
# # # }

# # # #print(daftar_Buku["Buku2"])
# # # print(daftar_Buku)

# # # games = dict(sekiro = "Action", pokemon = "Adventure", Valorant = "FPS")
# # # #cara membuat dictionry
# # # Biodata = {
# # #     "Nama" : "Aldy Ramadhan Syahputra",
# # #     "NIM" : 2109106079,
# # #     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# # #     "Mahasiswa_Aktif" :True,
# # #     "Social Media" : {
# # #         "Instagram" : "@aldyrmdhns_",
# # #         "Discord" : "\'Izanami#6848"
# # #         }
# # #     }

# # # for i in biodata:
# # #     print(i)
# # # for i, j in biodata.items():
# # #     print(f"Key = {i} dan value = {j}")
    
# # # #gak ada akan eror
# # # print(Biodata["KRS"][1])
# # # #gak ada akan non
# # # print(Biodata.get("Nama"))
# # # print(Biodata.get("Alamat"))
# # # #kalau manggil Q yang gak ada bisa nambahkan kalimat yang mau kita tambahkan
# # # print(Biodata.get("Alamat", "Kosong_Bang"))

# # # Film = {
# # #     "Avenger Endgame" : "Action",
# # #     "Sherlock Holmes" : "Mystery",
# # #     "The Conjuring" : "Horror"
# # #     }

# # # #Menghapus cara 1
# # # print(Film)
# # # del film["The Conjuring"]
# # # print(Film)
# # # #Menghapus cara 2 dengan menggunakan Pop
# # # print(Film)
# # # hapus = Film.pop("The Conjuring")
# # # print(Film)

# # # #clear membersihkan total
# # # print(Film)
# # # Film.clear()
# # # print(Film)

# # # print["Zombieland"] = "Comedy" #kurung siku
# # # film.update({"Hour" : "Thriller"})
# # # print(Film)

# # Biodata = {
# #     "Nama" : "Aldy Ramadhan Syahputra",
# #     "NIM" : 2109106079,
# #     "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# #     "Mahasiswa_Aktif" :True,
# #     "Social Media" : {
# #         "Instagram" : "@aldyrmdhns_",
# #         "Discord" : "\'Izanami#6848"
# #         }
# #     }

# # Print("Jumlah data dalam dict Biodata = ", len(Biodata))
# # pinjamdict = Biodata.copy()
# # print(pinjamdict)

# # key = "Apel", "Mangga", "Jeruk"
# # value = 1

# # buah = dict.fromkeys(key, value)
# # print(buah)

# # Film = {
# #     "Avenger Endgame" : "Action",
# #     "Sherlock Holmes" : "Mystery",
# #     "The Conjuring" : "Horror"
# # }
# # print(Film)
# # print("Film : ", Film.setdefault("Oldbook", "Horor"))
# # print(Film)


# # for i in film.values():
# #     print(i, end=" ")

# # Musik = {
# #     "The Chainsmoker" : ["All we Know", "TheParis"],
# #     "Alan Walker" : ["Alone", "Lily"],
# #     "Neffex" : ["Best of Me", "Memories"]
    
# # }
# # for i, j in Musik.items():
# #     print(f"Musik milik {i} adalah : ")
# #     for song in j:
# #         print(song)
# #     print("")
    
# # mahasiswa = {
# #     101 : {"Nama" : "Aldy", "Umur" : 19},
# #     111 : {"Nama" : "Abdul", "Umur" : 18}
# # }
# # print(f"sebelum : {mahasiswa}")
# # mahasiswa[101]["angkatan"] = 2023
# # print(f"sesudah : {mahasiswa}")

# # print(f"sebelum : {mahasiswa}")
# # del mahasiswa[111]["umur"]
# # print(f"sesudah : {mahasiswa}")

# # for i, j in mahasiswa.items():
# #     print(f"ID : {i}")
# #     for i_a, in j.items():
# #         print(f"{i_a} : {j_a}")


# #Studi Kasus
# Nama_Hewan ={
#     "Hewan1" : "Jerapah",
#     "Hewan2" : "Kucing",
#     "Hewan3" : "Kambing",
#     "Hewan4" : "Kadal",
#     "Hewan5" : "Buaya"
# } 
# #Panggil 
# print(Nama_Hewan["Hewan1"])

# #Ubah
# print(f"sebelum : {Nama_Hewan}")
# Nama_Hewan["Hewan3"] = "Jerapah"
# Nama_Hewan.update({"Hewan5" : "gajah"})
# print(f"sesudah : {Nama_Hewan}")

while True:
    print("1. Tambah")
    print("2. Tampilkan")
    print("3. Exit")
    pilihan = int(input("1/2/3) :"))
    
    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ") 
    
   