# EJERCICIO 1
# Determinar si un numero es positivo, negativo o cero

n = int(input('Ingrese un numero: '))

if n == 0:
    print('Tu numero es 0')
elif n > 0:
    print('Tu numero es par')
elif n < 0:
    print('Tu numero es negativo')
else:
    print('Ingrese un numero valido')