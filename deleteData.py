import koneksi
from getData import showData

def deleteData(): 
    try: 
        showData()
        kodeBarang = input("Delte Barang [kode]:  ")
        sql = """DELETE FROM barang WHERE kode=%s"""
        cursor = koneksi.mydb.cursor()
        cursor.execute(sql, (kodeBarang,))
        koneksi.mydb.commit()
        input("Deleted barang success...")
    except koneksi.Error as e:
        print(f"Gagal delete data : {e}")
        input("press any key to return to the menu..")