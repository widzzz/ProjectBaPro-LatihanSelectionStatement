# Fungsi untuk cek bilangan prima
# Rekursif
def isPrime(n, i = 2):

    if (n <= 2):
        return True if(n == 2) else False
    if (n % i == 0):
        return False
    if (i * i > n):
        return True

    # Panggil kembali
    return isPrime(n, i + 1)
 
#Program utama
n = int(input("Input : "))
if (isPrime(n)):
    print("Bilangan Prima")
else:
    print("Bukan Bilangan Prima")