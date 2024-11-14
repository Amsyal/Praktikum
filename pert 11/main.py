#  -----WEEKLY EXERCISE 1-----
from matematika import *

print(f"nilai dari pi adalah {pi}")

jari_jari = int(input("Masukkan nilai jari jari :"))
print(f"luas lingkaran : {l_lingkaran(jari_jari)}")

sisi = int(input("Masukkan panjang sisi: "))
print(f"luas persegi : {l_persegi(sisi)}")


#  -----WEEKLY EXERCISE 2-----

# menghitung akar
angka = int(input("Masukkan angka yang ingin diakarkan"))
akar_kuadrat = sqrt(angka)
print(f"nilai dari akar {angka} adalah {akar_kuadrat}")

# menghitung logaritma basis 10
log_angka = int(input("Masukkan angka :"))
logaritma = log10(log_angka)
print(f"nilai dari log {log_angka} adalah {logaritma}")

# menghitung nilai sin dari derajat
sudut_derajat = int(input("Masukkan besar sudut:"))
sudut_radian = radians(sudut_derajat)
sinus = sin(sudut_radian)
print(f"nilai sin dari {sudut_derajat} adalah {sinus}")

# menghitung nilai faktorial
angka_faktor = int(input("Masukkan angka yang ingin difaktorialkan:"))
faktorial = factorial(angka_faktor)
print(f"nilai dari {angka_faktor} faktorial adalah {faktorial}")

# membulatkan nilai ke bawah
angka_floor = float(input("Masukkan angka yang ingin dibulatkan ke bawah:"))
print(floor(angka_floor))

