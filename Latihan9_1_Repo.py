# Nama: Faza Tammy Amanullah
# NIM: 2607237
# Kelas: 1C

# Fungsi Fibonacci
def fibonacci(n):
    sekuens = []
    for i in range(n):
        if i < 2:
            sekuens.append(i)
        else:
            sekuens.append(sekuens[i - 1] + sekuens[i - 2])
    return sekuens

fibo = int(input("Masukkan jumlah bilangan Fibonacci yang diinginkan: "))
print(fibonacci(fibo))

#Volume Tabung
def volume_tabung(r, t):
    pi = 3.14
    volume = pi * (r ** 2) * t
    return volume

r = float(input("Masukkan jari-jari tabung: "))
t = float(input("Masukkan tinggi tabung: "))
print(volume_tabung(r, t))

#Menghitung fungsi nilai total dan nilai rata-rata
def nilai_total(*nilai):
    total = sum(nilai)
    rata_rata = total / len(nilai) if nilai else 0
    return total, rata_rata

nilai = [12, 15, 20, 25, 30]