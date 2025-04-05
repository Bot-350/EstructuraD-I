# EJERCICIO 11
# Adivinar un numero con limite de intentos

import random

random_n = random.randint(1,100)

intentos = 1
print(random_n)

print('Adivina un numeoro del 1 al 100\n' \
    'tienes 5 intentos\n')

while intentos < 6:
    print(f'Intentos {intentos}')
        
    n = int(input('Escribe: '))
    intentos += 1

    if n < random_n:
        print('Mas\n')
    elif n > random_n:
        print('Menos\n')
    else:
        break
    
if n == random_n:
    print('Adivinaste el numero')
else:
    print(f'El numero era {random_n}')
