#Trabalhando com orientação d eobjetos no python

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print(f'O seu saldo atual é de {self.__saldo} reais')

    def deposito(self, depositar):
        self.__saldo += depositar
        if self.__saldo > self.__limite:
            print("Você ultrapassou o limite, por favor coloque um valor menor")
            self.__saldo -= depositar
    
    def saque(self, sacar):
        self.__saldo -= sacar

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def get_numero(self):
        return self.__numero
    
    def set_limite(self, limite):
        self.__limite = limite