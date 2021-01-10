fila1 = int (input("Ingrese la cantidad de filas de la matriz 1: "))
columna1 = int (input("Ingrese la cantidad de columnas de la matriz 1: "))
fila2 = int (input("Ingrese la cantidad de filas de la matriz 2: "))
columna2 = int (input("Ingrese la cantidad de columnas de la matriz 2: "))
m1 = []
m2 = []
m = []

def matrices ():
    for i in range (fila1):
        m1.append([0] * columna1)
    for j in range (fila1):
        for k in range (columna1):
            m1[j][k] =  int (input ("Matriz1: Fila {%d}, columna {%d}: " % (j+1, k+1)))

    for i in range (fila2):
        m2.append([0] * columna2)
    for j in range (fila2):
        for k in range (columna2):
            m2[j][k] =  int (input ("Matriz 2: Fila {%d}, columna {%d}: " % (j+1, k+1)))



print (matrices())
print ("Matriz 1: \n")
for fila1 in m1:
    print (" ")
    for elemento in fila1:
        print ("{%d}" % (elemento), end = " ")

print ("\n\nMatriz 2: \n")
for fila2 in m2:
    print (" ")
    for elemento in fila2:
        print ("{%d}" % (elemento), end = " ")


def multiplicacion ():
    for k in range (len(fila1)):
        m.append ([0] * columna2)
        for i in range (columna2):
            m[k][i] = 0

    for i in range (len(fila1)):
        for j in range (columna1):
            for k in range (columna2):
                m[i][k] = m[i][k] + (m1[i][j] * m2 [j][k])

print ("\n\nMatriz Multiplicada: \n")
print (multiplicacion())
for fila1 in m:
    print (" ")
    for elemento in fila1:
        print ("{%d}" % (elemento), end = " ")