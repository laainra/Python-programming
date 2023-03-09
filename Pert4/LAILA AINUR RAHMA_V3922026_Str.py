nama = "Laila Ainur Rahma" # Membuat variabel dengan nama 'nama' yang berisi nama saya

# Hitung jumlah huruf
print(f'Jumlah huruf dalam nama adalah {len(nama)}') #menggunakan len() untuk menghitung jumlah karakter dalam variabel nama

# Huruf vokal

hurufVokal = "aeiou" # membuat variabel string yang berisi huruf vokal
jmlVokal = 0 # menginisialisasi nilai awal untuk jumlah huruf vokal yang akan dihitung
for huruf in nama: # menggunakan perulangan for untuk setiap karakter dari variabel nama dibungkus dengan variabel huruf
    if huruf.lower() in hurufVokal: # membuat pengkondisian jika nilai pada variabel huruf (dibuat huruf kecil/ lowercaase semua) ada dalam variabel hurufVokal
        jmlVokal += 1   # maka nilai dalam jmlVokal di increment/ ditambah 1

print(f'Jumlah huruf vokal dalam string adalah {jmlVokal}') # mencetak nilai akhir dari variabel jmlVokal (jumlah seluruh huruf vokal)

# Huruf Konsonan

hurufVokal = "aeiou " # membuat variabel string yang berisi huruf vokal
jmlKons = 0 # menginisialisasi nilai awal untuk jumlah huruf konsonan yang akan dihitung
for huruf in nama: # menggunakan perulangan for untuk setiap karakter dari variabel nama dibungkus dengan variabel huruf
    if huruf.lower() not in hurufVokal: # membuat pengkondisian jika nilai pada variabel huruf (dibuat huruf kecil/ lowercaase semua) tidak ada dalam variabel hurufVokal
        jmlKons += 1  # maka nilai dalam jmlKons di increment/ ditambah 1

print(f'Jumlah huruf konsonan dalam string adalah {jmlKons}')  # mencetak nilai akhir dari variabel jmlKons (jumlah seluruh huruf konsonan)