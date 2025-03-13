# EJERCICIO 6
# Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$',
# 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si
# la divisa no está en el diccionario.

divisa = {'euro':'€', 'dolar':'$', 'yen':'¥'}

div_usuario = input('Que divisa quiere ver? (Euro, Dolar, Yen)')

print(divisa.get(div_usuario, f"La divisa {divisa} no está en el diccionario"))
