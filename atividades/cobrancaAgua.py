#perguntar o consumo médio e e consumo do mês atual
consumo_media = int(input("Digite a média de consumo do último ano: "))
consumo_mes = int(input("Digite o consumo do mes: "))

#saber se vai ter desconto ou multa
if consumo_media > consumo_mes:#Desconto
    if consumo_mes <= 20:
        consumo_mes *= 2
        consumo_total = consumo_mes - (consumo_mes * 0.2)
    elif consumo_mes > 20 and consumo_mes <= 35:
        consumo_mes *= 3.5
        consumo_total = consumo_mes - (consumo_mes * 0.2)
    elif consumo_mes > 35 and consumo_mes <= 50:
        consumo_mes *= 5.5
        consumo_total = consumo_mes - (consumo_mes * 0.2)
    else:
        consumo_mes *= 7
        consumo_total = consumo_mes - (consumo_mes * 0.2)
    print("Sua conta ficou R${} reais aplicando o desconto de 20 por cento fica R${} reais." .format(consumo_mes, consumo_total))

elif consumo_media < (consumo_mes * 0.01) + consumo_mes:#multa
    if consumo_mes <= 20:
        consumo_mes *= 2
        consumo_total = consumo_mes + (consumo_mes * 0.3)
    elif consumo_mes > 20 and consumo_mes <= 35:
        consumo_mes *= 3.5
        consumo_total = consumo_mes + (consumo_mes * 0.3)
    elif consumo_mes > 35 and consumo_mes <= 50:
        consumo_mes *= 5.5
        consumo_total = consumo_mes + (consumo_mes * 0.3)
    else:
        consumo_mes *= 7
        consumo_total = consumo_mes + (consumo_mes * 0.3)
    print("Sua conta ficou R${} reais aplicando a multa de 30 por cento fica R${} reais." .format(consumo_mes, consumo_total))
else:#valor normal
    if consumo_mes <= 20:
        consumo_mes *= 2
        consumo_total = consumo_mes
    elif consumo_mes > 20 and consumo_mes <= 35:
        consumo_mes *= 3.5
        consumo_total = consumo_mes
    elif consumo_mes > 35 and consumo_mes <= 50:
        consumo_mes *= 5.5
        consumo_total = consumo_mes
    else:
        consumo_mes *= 7
        consumo_total = consumo_mes
    print("Sua conta ficou R${} reais." .format(consumo_total))