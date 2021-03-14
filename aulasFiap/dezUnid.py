#Sua tarefa é desenvolver um algoritmo que recebe um número inteiro de 0 a 99 e imprime o
#dígito das dezenas e o dígito das unidades desse número. Dica: usando papel e lápis faça a
#divisão inteira do número por 10 mas não coloque vírgula e nem acrescente 0 na divisão.

num = int(input("Digite um número entre 0 e 99: "))

dez = num // 10
unid = num % 10

if num >= 0 and num <= 99:
    print("O número ", num, "tem ", dez, " dezenas e ", unid, " unidades")
else:
    print("tenta como o pedido por favor.")