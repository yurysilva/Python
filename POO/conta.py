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
    
    def __pode_sacar(self, valor_de_saque):
        valor_a_sacar = self.__saldo + self.__limite
        return valor_de_saque <= valor_a_sacar

    def saque(self, sacar):
        if (self.__pode_sacar(sacar)):
            self.__saldo -= sacar
        else:
            print(f"O valor {sacar} passou o limite.")

    def transferir(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    
    def get_numero(self):
        return self.__numero

    @limite.setter
    def limite(self, limite):
        self.__limite = limite