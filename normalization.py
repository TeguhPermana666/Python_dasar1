from sklearn.preprocessing import MinMaxScaler

data=[[12000000,33],[35000000,45],[4000000,23],[6500000,26],[9000000,29]]
scaler=MinMaxScaler()#data train
scaler=scaler.fit(data)#data testing
#membuat sebuah object dari class minmaxscaler
#menghitung nilai minimum dan maksimum pada tiap kolom

"""
Pada cell selanjutnya kita buat sebuah objek MinMaxScaler dan panggil fungsi fit() dan 
mengisi argumen data seperti potongan kode di bawah. Fungsi fit() dari 
objek MinMaxSclaer adalah fungsi untuk menghitung nilai minimum dan maksimum pada tiap kolom.
"""
scaler=scaler.transform(data)
"""
Sampai pada fungsi fit() ini, komputer baru menghitung 
nilai minimum dan maksimum pada tiap kolom dan belum melakukan operasi scaler pada data. Terakhir 
kita panggil fungsi transform() yang akan mengaplikasikan scaler pada data
"""
print(scaler)