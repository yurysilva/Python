ano_atual = int(input("Digite a quantidade de anos atuais:"))
mes_atual = int(input("Digite a quantidade de meses atuais: "))
pergunta = str(input("Marque s se quer calcular futuro e n se quer calcular passado: "))
ano_calcular = int(input("Digite quantidade de ano a ser calculada: "))
mes_calcular = int(input("Digite a quantidade de meses a calcular: "))

#fazer a soma dos anos com meses
if pergunta == "s" or pergunta == "S":
    mes_para_ano = (mes_atual + mes_calcular) // 12
    mes = (mes_atual + mes_calcular) % 12
    ano_total = ano_calcular + ano_atual + mes_para_ano

    print("No futuro serão no total {} anos e {} meses" .format(ano_total, mes))



#fazer a subtração dos anos com meses
elif pergunta == "n" or pergunta == "N":
    mes_para_ano = mes_calcular // 12

    if mes_atual > mes_calcular:
        mes = (mes_atual - mes_calcular) % 12
        if ano_atual > ano_calcular:
            ano_total = (ano_atual - ano_calcular) - mes_para_ano
        else:
            ano_total = (ano_calcular - ano_atual) - mes_para_ano
    else:
        mes = (mes_calcular - mes_atual) % 12
        if ano_atual > ano_calcular:
            ano_total = (ano_atual - ano_calcular) - mes_para_ano
        else:
            ano_total = (ano_calcular - ano_atual) - mes_para_ano

    if ano_total >= 0 and mes >= 0:
        print("No passado estava com {} anos e {} meses" .format(ano_total, mes))
    else:
        print("Passado o limite menor que zero, por favor digite outro valor")