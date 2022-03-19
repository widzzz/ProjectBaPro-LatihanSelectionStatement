# Determine whether a number is prime or not.

#Input dari user
bilangan = int(input("Masukkan angka : "))
 
# bilangan prima merupakan bilangan lebih dari 1
if bilangan > 1:
     # cari faktor bilangan tersebut
    for i in range(2,bilangan):
        if (bilangan % i) == 0:
            # program berhenti bila faktor ditemukan
            print(bilangan,"bukan bilangan prima")
            break

     # kode else dibawah dieksekusi bila for tidak terpenuhi
     # kode seperti ini hanya ada di python    
    else:
        print(bilangan,"merupakan bilangan prima")

 # bila bilangan <= 1 otomatis bukan bilangan prima
else:
   print(bilangan,"bukan bilangan prima")