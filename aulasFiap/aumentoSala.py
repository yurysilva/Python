#Neste mês, João recebeu um aumento no salário, porém ele não sabe calcular o percentual aumento.
# Você deverá escrever um algoritmo que recebe 2 números reais representando
#os salários antes e depois do aumento e deverá calcular e exibir o percentual de aumento que
# que ele obteve

salario = float(input("Didite o seu salário atual: "))
aumento = float(input("Didite o salário com aumento: "))

percentual_salario = aumento / salario - 1
print("Percentual do aumento", percentual_salario * 100, "%")
#print("", )