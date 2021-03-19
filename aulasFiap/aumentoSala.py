#Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual aumento.
# Você deverá escrever um algoritmo que recebe 2 números reais representando
#os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que
# que ele obteve

salario = float(input("Didite o seu salário atual: "))
percetual = float(input("Didite o percentual do aumento do salário: "))

resPercentual = salario * (percetual / 100)
salarioNovo = resPercentual + salario

print("O aumento do seu salario em reais foi de R$",resPercentual," ficando com salário de R$",salarioNovo)