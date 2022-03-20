x = float(input("Masukkan panjang sisi 1: "))
y = float(input("Masukkan panjang sisi 2: "))
z = float(input("Masukkan panjang sisi 3: "))

if x==y==z:
	print("Equilateral")
elif x==y or x==z or y==z:
   print("Isosceles")
else:
   print("Arbitrary")