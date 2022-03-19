#Calculate 3 input numbers as coefficients at quadratic equations to get the roots!
#Equation: ax^2+bx+c

# math agar nanti bisa menggunakan math.sqrt
import math

# input nilai a, b, dan c
a = float(input("Masukkan nilai a :"))
b = float(input("Masukkan nilai b :"))
c = float(input("Masukkan nilai c :"))

# menggunakan rumus ABC
# simbol ** artinya pangkat dua
# math.sqrt = akar
group1 = -1 * b
group2 = math.sqrt((b ** 2) - 4 * a * c)
group3 = 2 * a

# x1 untuk -
x1 = (group1 - group2) / group3
# x2 untuk +
x2 = (group1 + group2) / group3

print(x1,",", x2)