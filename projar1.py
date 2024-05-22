
import math

jari_jari = float(input("Masukkan nilai jari-jari lingkaran: "))
luas = round(math.pi * jari_jari ** 2, 2)
keliling = round(2 * math.pi * jari_jari, 2)

print("Luas lingkaran dengan jari-jari", jari_jari, "adalah:", luas)
print("Keliling lingkaran dengan jari-jari", jari_jari, "adalah:", keliling)
