# EJERCICIO 4
# Escribir un programa que pida al usuario una palabra y muestre por pantalla el número
# de veces que contiene cada vocal.

def contar_vocales(palabra):
    a = 0 
    e = 0
    i = 0
    o = 0
    u = 0

    for letra in palabra:
        if letra == 'a': a += 1
        elif letra == 'e': e += 1
        elif letra == 'i': i += 1
        elif letra == 'o': o += 1
        elif letra == 'u': u += 1
    
    print(f'La palabra {palabra} tiene:')
    print(f'{a} vocales a \n{e} vocales e \n{i} vocales i')
    print(f'{o} vocales o \n{u} vocales u')

palabra = input('Escriba una palabra: ')
contar_vocales(palabra)
