import koneksi
from prettytable import from_db_cursor

def showData():
    cursor = koneksi.mydb.cursor()
    sql = '''SELECT * FROM barang'''
    cursor.execute(sql)
    #cetak 
    mytable = from_db_cursor(cursor)
    print(mytable)

def readAllData():
    while True: 
            showData()
            inputA = input("Back to menu ? [y/n] : ")
            if( inputA == "y" or inputA == "Y"):
                break

