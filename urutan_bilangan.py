print ('Masukkan 4 bilangan yang diinginkan!')
a=int(input('bilangan1 = '))
b=int(input('bilangan2 = '))
c=int(input('bilangan3 = '))
d=int(input('bilangan4 = '))

if a>b:
	a,b=b,a
if c>d:
	c,d=d,c
if a>c:
	a,c=c,a
if b>d:
	b,d=d,b
if b>c:
	b,c=c,b

print (a,b,c,d)