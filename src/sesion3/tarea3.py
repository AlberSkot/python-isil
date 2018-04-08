numero = list(range(1,10,1))
print(numero)

for num in numero:
	print(num**2)

suma = 0
i = 0
for elemento in numero:
	suma += elemento
	i +=1
resultado = suma
print(resultado)
