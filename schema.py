import koneksi
try:
    #script sql membuat tabel barang
    sql = """CREATE TABLE if not exists BARANG(
        kode char(5) NOT NULL ,
        nama_barang varchar(50),
        satuan VARCHAR(20),
        harga INT(11),
        jumlah INT(11),
        PRIMARY KEY(kode));"""
    cursor = koneksi.mydb.cursor()
    cursor.execute(sql)
    print("Membuat tabel barang berhasil")

    sql = """CREATE TABLE if not exists pelanggan(
        id int(11) NOT NULL COMMENT 'id pelanggan',
        nama varchar(50) DEFAULT NULL COMMENT 'nama pelanggan',
        alamat VARCHAR(75) DEFAULT NULL COMMENT 'alamat',
        jenis_kel char(1) DEFAULT NULL COMMENT 'jenis kelamin L=Laki2,P=Perempuan',
        tanggal_lahir DATE DEFAULT NULL COMMENT 'tanggal lahir',
        PRIMARY KEY(id));"""

    cursor = koneksi.mydb.cursor()
    cursor.execute(sql)
    print("Membuat tabel barang berhasil")
    

    sql = """CREATE TABLE if not exists jual(
        id int(11) NOT NULL AUTO_INCREMENT COMMENT 'no urut/no transaksi (otomatis)',
        pelanggan_id int(11) DEFAULT NULL COMMENT 'relasi dengan tabel pelanggan',
        total int(11) DEFAULT 0 COMMENT 'total ilai transaksi',
        tanggal date DEFAULT NULL COMMENT 'tanggal transaksi',
        PRIMARY KEY(id));"""


    cursor = koneksi.mydb.cursor()
    cursor.execute(sql)
    print("Membuat tabel barang berhasil") 

    sql =  """CREATE TABLE if not exists detil_jual(
        id int(11) NOT NULL AUTO_INCREMENT COMMENT 'no urut (otomatis)',
        jual_id int(11) DEFAULT NULL COMMENT 'no urut jual, relasi dengan tabel jual',
        kode int(11) DEFAULT NULL COMMENT 'kode barang',
        jumlah int(11) DEFAULT NULL COMMENT 'jumlah yang dibeli',
        harga_sekarang int(11) DEFAULT NULL COMMENT 'harga saat ini',
        tanggal date DEFAULT NULL COMMENT 'tanggal transaksi',
        PRIMARY KEY(id));"""

    cursor = koneksi.mydb.cursor()
    cursor.execute(sql)
    print("Membuat tabel barang berhasil")

except koneksi.Error as e:
    print("Terjadi kesalahan ", e)
    
finally: 
    if koneksi.mydb.is_connected():
        cursor.close()
        koneksi.mydb.close()
        print("Koneksi ke MySql telah ditutup")