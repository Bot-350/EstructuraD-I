# EJERCICIO 10
# Menu para elegir una operacion matematica

def suma(n1, n2):
    return n1 + n2

def resta(n1, n2):
    return n1 - n2

def multi(n1, n2):
    return n1 * n2

def divi(n1, n2):
    return n1 / n2

def menu():
    print('Operaciones Matematicas')
    print('1. Suma\n' \
        '2. Resta\n' \
        '3. Multiplicacion\n' \
        '4. Division' \
        '5. Salir')

def main():
    menu()

    op = input('Elige una de las opciones: ')

    if op == '5':
        print('Saliste')
        exit()
        
    n1 = float(input("Ingresa el primer numero: "))
    n2 = float(input("Ingresa el segundo numero: "))

    if op == '1':
        print(f'El resultado es {suma(n1,n2)}')
    elif op == '2':
        print(f'El resultado es {resta(n1,n2)}')
    elif op == '3':
        print(f'El resultado es {multi(n1,n2)}')
    elif op == '4':
        print(f'El resultado es {divi(n1,n2)}')
    
main()