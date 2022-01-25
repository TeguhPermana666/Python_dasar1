from sklearn.preprocessing import StandardScaler

data=[[12000000,33],[35000000,45],[4000000,23],[6500000,26],[9000000,29]]
scaler=StandardScaler()
scaler=scaler.fit(data)
#fit ini adalah sebuah method yang digunakan untuk meng-trainer data, latihan tergantung dari class yg memanggilnya
"""
Selanjutnya kita buat object scaler dan panggil fungsi fit dari scaler pada data. 
Fungsi fit memiliki fungsi untuk menghitung rata-rata 
dan deviasi standar dari setiap kolom atribut untuk kemudian dipakai pada fungsi transform.
"""
data=scaler.transform(data)
"""
Terakhir, kita panggil fungsi transform untuk mengaplikasikan standard scaler pada data.
Untuk melihat hasil dari standard scaler kita tinggal memanggil objek scaler yang telah dibuat.
"""

print(data)
