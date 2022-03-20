bil = float(input("Masukkan bilangan : "))

if bil<10 and bil>=0 :
	print("unit")
elif bil<100 and bil>9:
	print("tens")
elif bil<1000 and bil>99:
	print("hundreds")
elif bil<1000000 and bil>999:
	print("thousands")
else:
    print("Out of area")