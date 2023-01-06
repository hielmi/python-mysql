import koneksi
from getData import showData
import os

def updateData():
    try:
        os.system('cls')
        showData()
        kode = input("Pilih data yang akan dirubah [kode] : ")
        print("Pilih atribut yang dirubah :")
        print("1. Nama Barang")
        print("2. Satuan")
        print("3. Harga")
        print("4. Jumlah")
        while True: 
            inputA = input("Your input : ")
            data = None
            if( inputA == "1"):
                sql = """UPDATE barang SET nama_barang=%s WHERE kode =%s"""
                data = input("Masukan data baru : ")
                break
            elif (inputA == "2"):
                sql = """UPDATE barang SET satuan=%s WHERE kode =%s"""
                data = input("Masukan data baru : ")
                break
            elif (inputA == "3"):
                sql = """UPDATE barang SET harga=%s WHERE kode =%s"""
                data = int(input("Masukan data baru : "))
                break
            elif (inputA == "4"):
                sql = """UPDATE barang SET jumlah=%s WHERE kode =%s"""
                data = int(input("Masukan data baru : "))
                break
            else :
                input("Your input wrong...")

        cursor = koneksi.mydb.cursor()
        cursor.execute(sql, (data,kode))
        koneksi.mydb.commit()
        input("Update barang success...")

    except koneksi.Error as e:
        print(f"Gagal delete data : {e}")
        input("press any key to return to the menu..")