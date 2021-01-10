def multiplicacion(fila1, co1, fila2, co2):
    matriz1 = []
    matriz2 = []
    matriz3 = []
    # creacion de matriz 1
    for i in range(fila1):
        matriz1.append([0]*co1)

    # introducir datos al matriz 1
    for i in range(fila1):
        for j in range(co1):
            matriz1[i][j] = int(input(f"Introduzca los numero de la matriz 1 {i}{j}:  "))
    
    print("---Matriz 1---")
    for i in range(fila1):
        print(matriz1[i])

    # creacion de matriz 2
    for i in range(fila2):
        matriz2.append([0]*co2)

    # introducir datos al matriz 2
    for i in range(fila2):
        for j in range(co2):
            matriz2[i][j] = int(input(f"Introduzca los numero de la matriz 2 {i}{j}:  "))
    
    print("---Matriz 2---")
    for i in range(fila2):
        print(matriz2[i])

    

    #Resultado de matriz tamano
    for i in range(fila1):
        matriz3.append([0]*co2)


    #Multiplicacion de matrices
    for i in range(fila1):
        for j in range(co2):
            for k in range(co1):
                matriz3[i][j] += matriz1[i][k] * matriz2[k][j]

    print("El resultado de la multiplicacion del matriz es")
    for i in range(fila1):
        matrizResultado = []
        for j in range(co2):
            matrizResultado.append(matriz3[i][j])
        print (matrizResultado)




#main
print("***Bienvenido al sistema de multiplicacion de matrices***")
print("La fila se cuenta de manera horizontal y las columna verticalmente")

fila1 = int(input("Introduzca el tamano de la fila 1 del matriz 1: "))
co1 = int(input("Introduzca el tamano de la columna 1 del matriz 1: "))

fila2 = int(input("Introduzca el tamano de la fila 2 del matriz 2: "))
co2 = int(input("Introduzca el tamano de la columna 2 del matriz 2: "))

if (co1==fila2):
    multiplicacion(fila1, co1, fila2, co2)

else:
    print("Este matriz no se puede multiplicar")


