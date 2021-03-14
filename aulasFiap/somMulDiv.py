#Escreva um algoritmo em Python que recebe dois números inteiros e exibe: a soma desses
#dois números, a multiplicação, a divisão inteira e o resto da divisão inteira
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
mult = num1 * num2
divInt = num1 // num2
rest = num1 % num2

print("A soma dos dois números informados é igual a: ", soma)
print("A multiplicação dos dois números informados é igual a: ", mult)
print("A divisão iteira dos dois números informados é igual a: ", divInt)
print("O resto da divisão dos dois números informados é igual a: ", rest)