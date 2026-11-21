opc = int(input(""))
if opc == 1:
    # # Ejercicio: Solicita al usuario un número e imprime si es positivo.
    # Estructura de SELECCIÓN
    num = int(input("Num "))
    if(num > 0):
        print("par")
    elif(num == 0):
        print("neutro")
    else:
        print("impar")
elif opc == 2:
    # Ejercicio: Solicita al usuario dos números e imprime el mayor de ellos.
    num1 = int(input("Num "))
    num2 = int(input("Num "))

    if num1 > num2:
        print("num1 mayor")
    elif num2 > num1:
        print("num2 mayor")
    else:
        print("iguales")
elif opc == 3:
    # Ejercicio: Solicita al usuario un día de la semana e imprime si es laborable, fin de semana o inválido.
    num = int(input("Num día de la semana "))
    if num >= 1 and num <= 5:
        print("laborable")
    elif num <= 7:
        print("fin de semana")
    else:
        print("inválido")
elif opc == 4:
    cont = 1
    # Ejercicio: Imprime los números del 1 al 5 utilizando un bucle while.
    while(cont <= 5):
        print(cont)
        cont+=1
elif opc == 5:
    # Ejercicio: Imprime los cuadrados de los números del 1 al 3 utilizando un bucle for.
    for i in range(3):
        i +=1
        print(i**2)
elif opc == 6:
    # Ejercicio: Solicita al usuario su edad e imprime si es niño, adolescente, adulto o anciano.
    edad = int(input("edad "))
    if edad < 12 and edad >= 0:
        print("Niño")
    elif edad > 11 and edad <= 18:
        print("adolescente")
    elif edad > 18 and edad <= 60:
        print("adulto")
    elif edad > 59:
        print("anciano")
    else:
        print("aborto")
elif opc == 7:
    # Ejercicio: Imprime los números del 1 al 10, pero termina el bucle si encuentra el número 5.
    num=1
    while(num <= 10):
        if num == 5:
            num = 10
            print("PAILA!! 5")
        else:
            print(num)
        num +=1
elif opc == 99:
    # Ejercicio: Utiliza el módulo math para calcular la hipotenusa de un triángulo rectángulo.
    import math as m

    a = int(input("a "))
    b = int(input("b "))

    h= m.hypot(a,b)
    print(h)