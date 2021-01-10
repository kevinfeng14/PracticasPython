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