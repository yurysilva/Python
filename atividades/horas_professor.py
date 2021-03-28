#Pede as informações para o usuário
aulas_semanais = int(input("Digite a quantidade de aulas por semana: "))
hora_aula = float(input("Digite o valor da aula por hora: "))

#Serão feitos os calculos necessários para saber o valor total do salário mensal do professor
salario_base = aulas_semanais * 4.5 * hora_aula
hora_atividade = salario_base * 0.05
dsr = ((salario_base + hora_atividade)/6)
salario_mensal = salario_base + hora_atividade + dsr

#mostrar as informações para o usuário
print("O valor do salário base é de: ", salario_base)
print("Valor das Atividades no total: ", hora_atividade)
print("valor do descanso remunerado ", dsr)
print("Valor total com tudo incluso: ", salario_mensal)