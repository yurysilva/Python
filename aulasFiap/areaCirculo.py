#Escreva um algoritmo que calcula a área e o perímetro do círculo, use 3.141592 como valor
#de π .
#A = π . r2
# P = 2 π . r
raio = float(input("Digite o número do raio a ser calculado:"))
opcao = int(input("Digite 1 ser quiser calcular a area e 2 se quiser calcular o perimetro: "))

pi = 3.141592
area = pi * (raio ** 2)
perime = (pi * 2) * raio

if opcao == 1:
    print("A area é igua a: ", area)
else:
    print("O perimetro é igua a: ", perime)