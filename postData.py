import koneksi

def postData():
    try:
        while True:
            print("= Tambah Data Barang =")
            kode = input("Masukan kode barang : ")
            nama_barang = input("Masukan nama barang : ")
            satuan = input("Masukan Satuan : ")
            harga =  int(input("Masukan Harga : "))
            jumlah = int(input("Masukan Jumlah : "))
            
            #prepared sql
            sql = """INSERT INTO barang(kode, nama_barang, satuan, harga,jumlah)
            VALUES(%s, %s,%s, %s,%s)"""

            cursor = koneksi.mydb.cursor()
            cursor.execute(sql, (kode, nama_barang, satuan, harga, jumlah))
            koneksi.mydb.commit()
            print(f"Berhasil menyimpan {nama_barang}")
            inputA = input("Tambah data lagi ? [y/n] : ")
            if (inputA == "n" or inputA == "N"):
                input("press any key to return to the menu..")
                break
    except koneksi.Error as e:
        print(f"Gagal inser data : {e}")
        input("press any key to return to the menu..")