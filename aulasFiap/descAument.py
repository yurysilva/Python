#Dados o preço de um produto e um percentual de desconto, escreva um algoritmo que calcula
#e mostra o valor do desconto e o novo preço do produto dado o percentual. E se, ao invés
#de um desconto, fosse um aumento. O que muda no seu algoritmo?
produto = input("Digite o nome de produto: ")
valor = float(input("Digite o valor do produto: "))
desconto = int(input("Qual a porcentagem de desconto: "))
aumento = int(input("Qual a porcentagem do aumento: "))
resultPorcen = 0
resulTotal = 0
if desconto > 0 and aumento > 0:
    print("As informações de desconto e aumento não podem ser preenchidas juntas, por favor, escolha apenas uma das opações")
if desconto > 0 :
    resultPorcen = valor * (desconto / 100)
    resulTotal = valor - resultPorcen
    print("A quantidada do valor de ",valor," com desconto de ", resultPorcen," Fica com o valor total de ",resulTotal)
if aumento > 0:
    resultPorcen = valor * (aumento / 100)
    resulTotal = valor + resultPorcen
    print("A quantidada do valor de, ", valor, " com aumento de ", resultPorcen," Fica com o valor total de ",resulTotal)