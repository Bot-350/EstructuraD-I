# EJERCICIO 4
# Contar cuantos numeros son mayores que 10

numeros = [5, 12, 8, 20, 3, 15, 7, 30]  

count = 0 

for i in numeros:
    if i > 10:
        count += 1

print(f"Hay {count} numeros mayores que 10.")
