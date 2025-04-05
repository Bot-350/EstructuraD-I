# EJERCICIO 3
# Calcular la factorial de un numero

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Ingresa un numero: "))
print(f"El factorial de {n} es {factorial(n)}")
