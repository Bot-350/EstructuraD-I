# EJERCICIO 9
# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla,
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de
# ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje
#informando de ello

precio_fruta = {'manzana': 2.5,
            'banana': 1.8,
            'naranja': 1.5,
            'pera': 3.0,
            'uva': 4.5 }

fruta = input("Que fruta quieres comprar: ").lower()
kilos = float(input('Cuantos kilos?: '))

if fruta in precio_fruta:
    precio = precio_fruta[fruta] * kilos
    print(f'Total a pagar: {precio:.2f} Bs')
else:
    print('No tenemos fruta')
