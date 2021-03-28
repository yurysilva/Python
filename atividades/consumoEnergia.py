#saber qual o consumo mensal de energia
consumo_mes = int(input("Digite o seu consumo de KWh no mês: "))

#saber se precisa do acrecimo de 0,25 por KW
if consumo_mes > 50:
    acrescimo_kw = 14 + (consumo_mes * 0.25)
    if consumo_mes > 99 and acrescimo_kw < 201:
        consumo_icms = acrescimo_kw * 0.13
        consumo_total = acrescimo_kw + consumo_icms
    elif consumo_mes > 200:
        consumo_icms = acrescimo_kw * 0.33
        consumo_total = acrescimo_kw + consumo_icms
    else:
        consumo_icms = 0
        consumo_total = acrescimo_kw
else: 
        acrescimo_kw = 14
        consumo_icms = 0
        consumo_total = 14


print("O resultado do seu consumo do mês sendo RS{} do valor do consumo, RS{} de ICMS dando um total de R${}" .format(acrescimo_kw, consumo_icms, consumo_total))