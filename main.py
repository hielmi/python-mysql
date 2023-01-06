import os
import postData
import getData
import deleteData
import updateData

def menus():
    print('== Selamat Datang ==')
    print("Silahkan pilih menu yang tersedia: ")
    print("1. Tambah Data")
    print("2. Update Data")
    print("3. Delete Data")
    print("4. Tampilkan Data")
    print("0. Exit")

if __name__ == "__main__":
    while True: 
        os.system('cls')
        menus()
        pilihan = input("Pilih : ")
        if (pilihan == "1"):
            postData.postData()
        elif (pilihan == "2"):
            updateData.updateData()
        elif (pilihan == "3"):
            deleteData.deleteData()
        elif (pilihan =="4"):
            getData.readAllData()
        elif (pilihan == "0"):
            input("Press any key to exit...")
            break
        else:
            input("Your input doesn't exists...")

print("..=Terimakasih=..")