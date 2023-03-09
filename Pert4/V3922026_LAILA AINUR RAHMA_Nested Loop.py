# LAILA AINUR RAHMA (V3922026/TI D)

n = int(input("Masukkan panjang deret angka:")) # input panjang angka deret fibbonaci yang akan diprint

fibo = [0, 1] # inisialisasi list fibo dengan 2 angka awal yaitu 0 dan 1

for i in range(2,n): # melakukan perulangan for sebanyak (n-2) kali, dimulai dari i=2
        while len(fibo) <= n: # melakukan perulangan while selama jumlah elemen dalam list fibo masih kurang dari atau sama dengan n
                    print(fibo) # mencetak isi list fibo pada setiap iterasi
                    angka1 = fibo[-2] # mengambil 2 elemen terakhir pada list fibo
                    angka2 = fibo[-1]
                    angka_next = angka1 + angka2 # menjumlahkan 2 elemen terakhir pada list fibo
                    fibo.append(angka_next) # menambahkan hasil penjumlahan ke dalam list fibo
        i+=1 # menambahkan nilai i dengan 1 setiap perulangan

# perulangan diatas akan mencetak list fibo setiap perulangan terjadi sehingga akan tercetak list fibo yang anggotanya terus bertambah seiring terjadinya perulangan







