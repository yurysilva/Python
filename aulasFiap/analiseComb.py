#Uma pessoa tem em seu guarda roupa x camisas, y calças e z pares de sapato. Escreva
#um algoritmo que calcula de quantas maneiras diferentes ele pode se vestir. Seu algoritmo
#deverá ler o número de camisas, o número de calças e o número de pares de sapato.

camisa = int(input("digite a quantidade de camisas que você possui: "))
calcas = int(input("digite a quantidade de calças que você possui: "))
parSapato = int(input("digite a quantidade de pares de sapatos que você possui: "))

combinacoes = camisa * calcas * parSapato

print("A quantidade de formas diferntes que você pode facer combinações é de: ", combinacoes)