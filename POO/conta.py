#Trabalhando com orientação d eobjetos no python

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite

    def extrato(self):
        print(f'O seu saldo atual é de {self.saldo} reais')

    def deposito(self, depositar):
        self.saldo += depositar
        if self.saldo > self.limite:
            print("Você ultrapassou o limite, por favor coloque um valor menor")
            self.saldo -= depositar
    
    def saque(self, sacar):
        self.saldo -= sacar
