# EJERCICIO 5
# Calcular la suma de los numeros pares del 1 al 100

suma = 0

for n in range(1,101):
    if n % 2 == 0:
        suma+=n

print(f'La suma de los pares del 1 al 100 es {suma}')