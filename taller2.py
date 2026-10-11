#10 ejercicios nuevos
#35. Tarea: Crea una cadena "Programar en Python" y obtén solamente la palabra "Python" usando índices o slicing.
cad = "Programar en Python"
cad1= cad.index("Python")
cad = cad[cad1:]
print(cad)

#36. Tarea: Crea una lista [10, 20, 30, 40, 50] y obtén los últimos tres elementos sin usar condicionales ni bucles.
lista = [10, 20, 30, 40, 50]
print(lista[2:5])
#37. Tarea: Crea una lista [1, 2, 3] y agrega los elementos 4 y 5 usando un método de lista.
lista2 =[1, 2, 3]
lista2.append(4)
lista2.append(5)
print(lista2)
#38. Tarea: Crea una cadena "python es divertido" y reemplaza "divertido" por "genial".
cad2 = "python es divertido"
cad3= cad2.replace("divertido", "genial")
print(cad3)
#39. Tarea: Crea una cadena " Hola Python " y elimina los espacios que están al principio y al final.
cad4 = " Hola Python "
cad5 = cad4.strip()
print(cad5)
print(cad4)
#40. Tarea: Crea una lista [8, 3, 10, 1, 5] y ordénala de forma descendente.
lista3 =[8, 3, 10, 1, 5]
lista3.sort(reverse=True)
print(lista3)
#41. Tarea: Crea una lista [10, 20, 30, 40, 50] y calcula el valor máximo y el valor mínimo usando funciones de Python.
lista4 = [10, 20, 30, 40, 50]
print(min(lista4))
print(max(lista4))
#42. Tarea: Crea una lista [5, 10, 15, 20, 25] y calcula la suma y el promedio de sus elementos.
lista5 = [5, 10, 15, 20, 25]
print(sum(lista5))
print(sum(lista5)/len(lista5))
#43. Tarea: Crea un diccionario con los datos de una persona:

#persona = {
#    "nombre": "Carlos",
#    "edad": 25,
#    "ciudad": "Cali"
#}
#Obtén e imprime solamente el nombre y la ciudad.
person = {
    "nombre": "Laury",
    "edad": 31,
    "ciudad": "Cali"
}
print(person["nombre"])
print(person["ciudad"])
#44. Tarea: Crea dos conjuntos:
#
#conjunto1 = {1, 2, 3, 4, 5}
#conjunto2 = {4, 5, 6, 7, 8}
#Obtén la intersección de ambos conjuntos, es decir, los elementos que están presentes en los dos.
conj = {1,2,3,4,5}
conj1 = {4,5,6,7,8}
resul = conj & conj1
print(resul)