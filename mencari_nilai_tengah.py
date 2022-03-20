# Find the middle number among 3 different numbers!

bil1=int(input("Masukkan bilangan pertama: "))  #14
bil2=int(input("Masukkan bilangan kedua  : "))  #10
bil3=int(input("Masukkan bilangan ketiga : "))  #28

if bil1>bil2:
    if bil1<bil3:
        print(bil1)
    elif bil2>bil3:
        print(bil2)
    else:
        print(bil3)
else:
    if bil1>bil3:
        print(bil1)
    elif bil2<bil3:
        print(bil2)
    else:
        print(bil3)