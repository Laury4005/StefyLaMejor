# Crea una función llamada saludar que imprima un saludo.
#funcion: es un bloque de código reutilizable en diferentes espacios de tu proyecto.
def saludar(nom):
    print("Hablame "+nom)

opc = int(input(""))
if opc == 1:
    nom = input("Nom ")
    saludar(nom)