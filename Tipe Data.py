# Belajar dari nol

# variabel adalah tempat menyimpan data

a = 10
x = 5
panjang = 1000

# pemanggila pertama
print("Nilai a =", a)
print("Nilai x =", x)
print("Nilai panjang =", panjang)

# penamaan
nilay_y = 15 #dengan menggunakan underskor
"""kalau seperti ini 10juta itu tidak boleh
karna anggka tidak boleh di awal"""
juta10 = 10000000 #ini boleh
nilaiZ = 17.5 #ini boleh

# pemanggilan kedua
print("nilai a =", a)
a = 7
print("nilai a =", a)

# assignment indirect
b = a
print("Nilai b =", b)

# komen apalagi ini
# lanjut belajar tipe data

# tipe data angka (integer)
data_integer = 1
print("data :", data_integer, ", bertipe :", type(data_integer))

# tipe data float, angka dengan koma
data_float = 1.5
print("data_float : ",data_float, ", bertipe : ", type(data_float))

# tipe data string, kumpulan karangter
data_string = "tole"
print("data_string : ",data_string, ", bertipe : ", type(data_string))

# tipe data biner true / false (boolean)
data_boolean = False
print("data_boolean : ",data_boolean, ", bertipe : ", type(data_boolean))

#tipe data khusus
## bilangan kompleks
data_kompleks = complex(5,6)
print("data_kompleks : ", data_kompleks, ", bertipe : ", type(data_kompleks))

## Mengambil inputan dari user

data = input("Masukan nilai: ")
print("Nilai = ", data,", type = ", type(data))
