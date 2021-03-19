#O RM de um aluno da FIAP é composto por 5 dígitos. Sua tarefa é escrever um algoritmo que
#recebe um RM e retorna a somatória de todos os dígitos do RM. Por exemplo, suponha que
#o aluno tenha o RM 56395, seu algoritmo deverá imprimir como saída 28 = 5 + 6 + 3 + 9 + 5 .
#Dica: realize várias divisões e restos de divisões por 10 .

rm = int(input("Digite  numero do seu RM: "))
#85595
n1 = rm // 10000
rm %= 10000
n2 = rm // 1000
rm %= 1000
n3= rm // 100
rm %= 100
n4 = rm // 10
rm %= 10
n5 = rm // 1
rm %= 1
resSomaRm = n1 + n2 + n3 + n4 + n5
print("A soma dos números do seu RM fica igual a: ", resSomaRm)