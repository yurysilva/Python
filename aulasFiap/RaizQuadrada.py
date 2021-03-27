import math

numero = float(input("Informe um número: "))

if numero >= 0:
    raiz = math.sqrt(numero)
    print("A raiz vale ", raiz)
else:
    print("Digite um número mais que zero por favor.")