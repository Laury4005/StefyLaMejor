# 01. Tarea: Crea una variable llamada 'mensaje' y asígnale el valor "Hola, Python!"

mensaje = "Hola, Python!"
print(mensaje)
print("------------------")
print("------------------")
# 02. Tarea: Crea una lista con nombres de ritmos musicales y muestra el tercer elemento.

listas = ["Rock", "Jazz", "Clásica", "Reggae", "Perreito"]
print(listas[2])
print("------------------")
print("------------------")

# 03. Tarea: Calcula el área de un rectángulo con base 5 y altura 3.

base = 5
altura = 3
area = base * altura
print("Área del rectángulo:\n",area) 
print("------------------")
print("------------------")

# 04. Tarea: Implementa un programa que determine si un número es par o impar.

numero = 97
decision = ""
if(numero % 2 == 0): print("Número par")
else: print("Numero impar")
print("------------------")
print("------------------")

# 05. Tarea: Intenta usar una palabra reservada como nombre de variable y observa qué sucede.

# print =
# if =
# for =
# and =
# else = 
# elif =

print("------------------")
print("------------------")

# 06. Tarea: Calcula el resultado de la siguiente expresión matemática: (10 + 5) * 2 / 3

result =  (10 + 5) * 2 / 3
print("Resultado de la expresión matemática:\n",result)
print("------------------")
print("------------------")

# 07. Tarea: Crea una lista de números y muestra la suma de todos los elementos.

num_list = [1,2,3,4,5,6,7,8,8,9,9,9,9,9,9,4]
result = sum(num_list)
print(result)
print("------------------")
print("------------------")

# 08. Tarea: Solicita al usuario ingresar un número e indica si es positivo, negativo o cero.

# num = int(input("Número:"))
num = 0
if num > 0:
    print("Número positivo")
elif num < 0:
    print("Número negativo")
else:
    print("Cero")
print("------------------")
print("------------------")

# 09. Tarea: Crea una cadena e imprime cada caracter en una línea. (sin usar ciclos)

cadena = "Mi primer código en python"
for caracteres in cadena:
    print(caracteres)
print("------------------")
print("------------------")

# 10. Tarea: Define una función que calcule el área de un círculo dado su radio.
import math

# radio = float(input("Radio: ")) 
radio = 19
area = math.pi * (radio**2)
print(round(area))
print("------------------")
print("------------------")

# 11. Tarea: Crea un diccionario con nombres de personas y sus edades. Imprime la edad de una persona específica.

personas = {
    "Laury": {
        "edad"   : 31
    },
    "Stefy": {
        "edad"   : 32
    },
    "Milú": {
        "edad"   : 6
    }    
}

# nom = input("Nombre: ")
nom = "Milú"
print("Edad: ",personas[nom]["edad"])
print("------------------")
print("------------------")

# 12. Tarea: Utiliza el módulo 'random' para generar un número aleatorio entre 1 y 10.
import random
rdn = random.randint(1,10)
print(rdn)
print("------------------")
print("------------------")

# 13. Tarea: Calcula la suma, resta, multiplicación y división de dos números sin usar condicionales ni bucles.

#num1 = int(input("Número 1: "))
#num2 = int(input("Número 2: "))
num1 = 4
num2 = 9

suma = num1+num2
resta = num1-num2
mult = num1*num2
div = num1/2

print(suma)
print(resta)
print(mult)
print(div)
print("------------------")
print("------------------")

# 14. Tarea: Crea dos listas y concaténalas sin usar condicionales ni bucles.

list1 = [1,2,3,4]
list2 = ["Uno", "Dos", "Tres"]
list3 = list1 + list2

print(list3)
print("------------------")
print("------------------")

# 15. Tarea: Crea dos cadenas e imprime la concatenación sin usar condicionales ni bucles.

cad1 = "Stefy"
cad2 = "La mejor!!!!"
cad3 = cad1 + " " + cad2

print(cad3)
print("------------------")
print("------------------")

# 16. Tarea: Crea una lista y añade un elemento sin usar condicionales ni bucles.

list1 = [1,2,3]
list1.append("Milúsita")
print(list1)
print("------------------")
print("------------------")

# 17. Tarea: Crea dos diccionarios y únelos sin usar condicionales ni bucles.
personas1 = {
    "Laury": {
        "edad"   : 31
    },
    "Stefy": {
        "edad"   : 32
    },
    "Milú": {
        "edad"   : 6
    }    
}

colores = {
    "Verde": {
        "intensidad"   : "claro"
    },
    "Purpura": {
        "intensidad"   : "claro"
    },
    "Rojo": {
        "intensidad"   : "fuerte"
    }    
}

dic_f = personas1 | colores
for p in dic_f:
    print(dic_f[p],"\n")
print("------------------")
print("------------------")

# 18. Tarea: Crea dos conjuntos y encuentra la unión sin usar condicionales ni bucles.

conj1 = {1,2,3,400}
conj2 = {"S", "T", "E", "F", "Y"}
form1 = conj1 | conj2
form2 = conj1.union(conj2)
print(form1 , "\n", 
      form1)
print("------------------")
print("------------------")

# 19. Tarea: Obtén la fecha y hora actual sin usar condicionales ni bucles.

from datetime import datetime 

now = datetime.now()
print(now)
print("------------------")
print("------------------")

# 20. Tarea: Calcula la longitud de una cadena sin usar condicionales ni bucles.

# cad = input("Cadena: ")
cad = "hola"
longitud = len(cad)
print(longitud)
print("------------------")
print("------------------")

# 21. Tarea: Convierte una cadena a mayúsculas y otra a minúsculas sin usar condicionales ni bucles

#cad = input("Cadena: ")
cad = "Stefy"
cad_may = cad.upper()
cad_min = cad.lower()

print("Mayúsculas: ",cad_may, "\nMinúsculas: ", cad_min)
print("------------------")
print("------------------")

# 22. Tarea: Reemplaza una subcadena en una cadena principal sin usar condicionales ni bucles.

cadena = "Hola mundo"
#subcadena = input("Subcadena: ")
#reemplazo = input("Reemplazo: ")
subcadena = "mundo"
reemplazo = "Milú"

result = cadena.replace(subcadena, reemplazo)
print(result)
print("------------------")
print("------------------")

#23. Tarea: Divide una cadena en palabras sin usar condicionales ni bucles.
# cadena = input("Cadena: ")
cad = "pastel de chocolate"
result = cadena.split(" ")
print(result)
print("------------------")
print("------------------")

#24. Tarea: Concatena tres cadenas diferentes sin usar condicionales ni bucles.
#cad1 = input("Cadena 1: ")
#cad2 = input("Cadena 2: ")
#cad3 = input("Cadena 3: ")
cad1 = "uno"
cad2 = "uno"
cad3 = "cinco"
result = cad1 + " " + cad2 + " " + cad3
print(result)
print("------------------")
print("------------------")

#25. Tarea: Crea dos listas y extiende la primera con los elementos de la segunda sin usar condicionales ni bucles.
list1 = [1,2,3,4,199]
list2 = ["amarillo", "azul", "rojo"]
list1 += list2
print(list1)
print("------------------")
print("------------------")

#26. Tarea: Elimina un elemento específico de una lista sin usar condicionales ni bucles.
list1 = [1,2,3,4,199]
# list1.remove(199)
list1.pop(1)
print(list1)
print("------------------")
print("------------------")

#27. Tarea: Encuentra el índice de un elemento en una lista sin usar condicionales ni bucles.
list1 = [1,2,3,4,199]
ind = list1.index(199)
print(ind)
print("------------------")
print("------------------")

#28. Tarea: Ordena una lista de números de forma ascendente sin usar condicionales ni bucles.
list1 = [1,2,3,4,199,5,0]
list1.sort()
list_ord = list1
print(list_ord)
print("------------------")
print("------------------")

#29. Tarea: Cuenta cuántas veces aparece un elemento en una lista sin usar condicionales ni bucles.
list1 = [1,2,3,4,199,5,0,1,1,2]
#cant_rep = list1.count(int(input("Elemento: ")))
cant_rep = 0
print(cant_rep)
print("------------------")
print("------------------")
#30. Tarea: Calcula 2 elevado a la 5ta potencia sin usar condicionales ni bucles.
potencia = 2**5
print(potencia)
print("------------------")
print("------------------")

#31. Tarea: Realiza la división entera de 17 entre 3 sin usar condicionales ni bucles.
div = 17 // 3
print("División entera: ",div)
print("------------------")
print("------------------")

#32. Tarea: Calcula el resto de la división de 20 entre 7 sin usar condicionales ni bucles.
mod = 20 % 7
print("Residuo: ",mod)
print("------------------")
print("------------------")
#33. Tarea: Redondea el número 3.14159 a dos decimales sin usar condicionales ni bucles.
num = 3.14159
num = round(num, 2)
print(num)
print("------------------")
print("------------------")

#34. Tarea: Realiza la operación (4 + 3) * (2 - 1) sin usar condicionales ni bucles.
op = (4 + 3) * (2 - 1)
print(op)