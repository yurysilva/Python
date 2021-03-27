#Perguntar salário atual
salario = float(input("Digite seu salário atual: "))

#calcular salário com INSS
if salario <= 1100:
    inss_075 = (salario * 0.075)
    aliquota = inss_075

elif salario > 1100 and salario <= 2203.48:
    inss_075 = 1100 * 0.075
    if salario - 1100 > 0:
        inss_09 = (salario - 1100) * 0.9
        aliquota = inss_075 + inss_09
    elif 1100 - salario > 0:
        inss_09 = (1100 - salario) * 0.9
        aliquota = inss_075 + inss_09

elif salario > 2203.48 and salario <= 3305.22:
    inss_075 = 1100 * 0.075
    inss_09 = (2203.48 - 1100) * 0.09
    if salario - 2203.48 > 0:
        inss_12 = (salario - 2203.48) * 0.12
        aliquota = inss_075 + inss_09 + inss_12
    elif 2203.48 - salario > 0:
        inss_12 = (2203.48 - salario) * 0.12
        aliquota = inss_075 + inss_09 + inss_12
else:
    inss_075 = 1100 * 0.075
    inss_09 = (2203.48 - 1100) * 0.09
    inss_12 = (3305.22 - 2203.48) * 0.12
    if salario - 3305.22 > 0:
        inss_14 = (salario - 3305.22) * 0.14
        aliquota = inss_075 + inss_09 + inss_12 + inss_14
    elif 3305.22 - salario > 0:
        inss_14 = (3305.22 - salario) * 0.14
        aliquota = inss_075 + inss_09 + inss_12 + inss_14

print("O seu salário de R$ {} reais ficou com o calculo da contribuição do INSS de R$ {} reais." .format(salario, aliquota))