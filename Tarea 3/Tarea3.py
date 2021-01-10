def checkfloat():
    while True:
        try:
            num = input()
            float(num)
        except ValueError:
            print("Ingrese solo numeros")
            continue

        if not str(num).__contains__('.'):
            print("No se acepta numeros enteros")
            continue

        return float(num)
        
# 1. presentacion del grupo
def presentacion():
    
    print ("""
            UNIVERSIDAD TECNOLÓGICA DE PANAMÁ FACULTAD DE INGENIERÍA DE SISTEMAS COMPUTACIONALES 
                                DEPARTAMENTO DE COMPUTACIÓN Y SIMULACIÓN DE SISTEMAS 
                                                  LABORATORIO 1 
                                                FC-FISC-1-8-2016
            Integrante: Raby, Sahori    8-964-644
                        Villalaz, Luis  8-925-2287
                        Feng, Kevin     3-748-410
                        Zheng, Wymming   8-966-1043
                        Iglesia, Angel  8-958-1
    """)
#Problema 1
def p1():
    
    print("""
                ------ problema 1 ------
    """)

    numero1 = float(input("Introduzca primer numero : "))
    numero2 = float(input("Introduzca segundo numero con : "))
    numero3 = float(input("Introduzca tercer numero con : "))

    suma = numero1 + numero2 + numero3
    promedio = suma/3
    resta = numero1 - numero2 - numero3
    multi = numero1 * numero2 * numero3

    print(f'La suma de{numero1} + {numero2} + {numero3} = {suma}')
    print(f'La resta de {numero1} - {numero2} - {numero3} = {resta}')
    print(f'la multiplicacion de {numero1} - {numero2} - {numero3} = {multi}')
    print(f'El promedio de {numero1}, {numero2} y {numero3} = {promedio}')

#Problema 2
def p2():
    print("""
                ------ problema 2 ------
    """)

    print("En este programa buscaremos la velocidad final. ")
    vo = float(input("Introduzca la velocidad inicial: "))
    t = float(input("Introduzca el tiempo: "))
    g = 9.8
    vf = vo +(g*t) 

    print("\t\t------ Calculando... ------")
    print("la velocidad final es: {}".format(vf))

#Problema 3


#Problema 4
print("""
                ------ problema 4 ------
    """)
def p4():
    pass
    mayor = int(input("Numero que desea imprimir pares "))
    menor = int(input("Numero menor que el anterior "))
    if mayor > menor:
        z = mayor + 51
        if mayor%2 == 0:
            mayor += 2
            while mayor<z:
                print(f"{mayor} ", end=' ')
                mayor += 2
        else:
            mayor += 1
            while mayor<z:
                print(f"{mayor} ", end=' ')
                mayor += 2
        print(f" ")
        if menor%2 == 0:
            while menor>0:
                print(f"{menor} ", end=' ')
                menor -= 2
        else:
            menor -= 1
            while menor>0:
                print(f"{menor} ", end=' ')
                menor -= 2

#Problema 5
print("""
                ------ problema 5 ------
    """)
def p5():
    print("\t\tEste programa sirve para calcular la raiz cubica y cuadrada de un numero")
    s = 1
    while s!=0:
        num = int(input("\nA continuacion, ingrese un numero: "))

        cuadrada = num**(1/2)
        cubica = num**(1/3)

        print(f"\nLa raiz cuadrada de {num} es: {cuadrada}")
        print(f"\nLa raiz cubica de {num} es: {cubica}")
        s=int(input("\t\n\nDesea Calcular otras raices? Presione: \n 0. SALIR \n 1. CONTINUAR \n "))
        while s!= 1 and s!= 0:
            s=int(input("ERROR. Seleccion no encontrada. Presione: \n 0. SALIR \n 1. CONTINUAR \n "))

#Problema 6
print("""
                ------ problema 6 ------
    """)
def p6():
    pass
    lim = int(input("Inserte cantidad de valores para la piramide "))
    i = 1
    n = 1
    v = 0
    for i in range (1,lim+1):
        if v < n:
            print(f"{i}", end=' ')
            v += 1
            if v >= n: 
                print(f"")
                n += 1
                v = 0
while True:
    print(""""
        Menu
    1.   Presentacion
    2.   Problema 1
    3.   Problema 2
    4.   Pronlema 3
    5.   Problema 4
    6.   Pronlema 5
    7.   Problema 6
    0.     Salir  
    """)

    opcion = int(input("Introduzca un numero del menu: "))

    if opcion == 1:
        presentacion()

    elif opcion == 2:
        p1()

    elif opcion == 3:
        p2()   

    elif opcion == 4:
        p3()

    elif opcion == 5:
        p4()

    elif opcion == 6: 
        p5()

    elif opcion == 7:
        p6()
    
    elif opcion == 0:
        break

    else:
        print("------La opcion seleccionado no se encuentra dentro del menu, seleccione nuevamente-----")