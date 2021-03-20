entrada = int(input("Informe um número inteiro: "))

resto = entrada % 2

if resto == 0:
    print(entrada, " e par")
    print("Continuando as instruções do cloco if")
else:
    print(entrada, " e impar")
    print("continuo nesta indentação se esitem mais instruções")
