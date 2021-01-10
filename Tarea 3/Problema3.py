print("""
            ------ problema 3 ------
""")

practicaTotal = 0

for i in range(1, 6):
    practica = float(input("Introduzca la nota del practica {} : ".format(i)))

    practicaTotal = practica + practicaTotal

parcial = float(input("Introduzca la nota de examen parcial: "))
final = float(input("Introduzca la nota del examen final: "))

promedio = ((practicaTotal/6)*0.35) + (parcial*0.325) + (final * 0.325)

print(f'El estudiante tiene un promedio de \nPracticas : {practicaTotal}\nExamen Parcial : {parcial}\nExamen Final : {final}\nResultado Promedio Final : {promedio}')