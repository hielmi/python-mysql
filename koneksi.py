import mysql.connector
from mysql.connector import Error
try:
    mydb = mysql.connector.connect(
        host= "localhost",
        user= "hielmi",
        password="hielmi123",
        database="db_jual"
    )

    #meminta koneksi
    if mydb.is_connected():
        db_Info = mydb.get_server_info()
        print(f"Koneksi ke MySQL Server versi: {db_Info}")
        cursor = mydb.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print(f"Anda telah koneksi ke Database : {record}")

    #cek jika error
except mydb.Error as e:
    print(f"Terjadi kesalahan {e}")
finally:
    if mydb.is_connected():
        cursor.close()
        print("Koneksi ke MySQL Telah ditutup")