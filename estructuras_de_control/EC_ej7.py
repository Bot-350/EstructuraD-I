# EJERCICIO 7
# Contar los multiplos de 3 entre 2 numeros

# Pedimos los dos números al usuario

n1 = int(input('Ingresa el primer numero: '))
n2 = int(input('Ingresa el segundo numero: '))

if n1 > n2:
    n1, n2 = n2, n1

count = 0
for i in range(n1, n2 + 1):
    if i % 3 == 0:
        count += 1

print(f'Hay {count} multiplos de 3')
