# EJECICIO 8
# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información
# sobre una usuario (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.) que
# se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del
# diccionario.

usuario = {}

usuario["nombre"] = input("Nombre: ")
usuario["edad"] = input("Edad: ")
usuario["sexo"] = input("Sexo: ")
usuario["telefono"] = input("Teléfono: ")
usuario["email"] = input("Email: ")

print("\nDatos completos de la persona:")
print(usuario)

