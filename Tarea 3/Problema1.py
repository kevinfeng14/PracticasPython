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
