x = int(input("Masukkan koordinat x :"))
y = int(input("Masukkan koordinat y :"))

if x > 0 and y > 0:
    print("1")
elif  x < 0 and y > 0:
	print("2")
elif x < 0 and y < 0:
	print("3")
elif x > 0 and y < 0:
	print("4")
else:
	print("Tidak dalam daerah kuadran")