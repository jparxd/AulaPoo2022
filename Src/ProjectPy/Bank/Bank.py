from Src.ProjectPy.Exception.CIException import CIException
from Src.ProjectPy.Exception.SIException import SIException


class Banco:
    def __init__(self):
        self.contas = [None] * 100
        self.indice = 0

    def cadastrar(self, conta):
        self.contas[self.indice] = conta
        self.indice += 1

    def procurar_conta(self, numero):
        i = 0
        achou = False
        while achou is False and i < self.indice:
            if self.contas[i].get_numero() == numero:
                achou = True
            else:
                i += 1
        if achou is True:
            return self.contas[i]
        else:
            return None

    def creditar(self, numero, valor):
        try:
            conta = self.procurar_conta(numero)
            conta.creditar(valor)
        except CIException(numero) as errorci:
            print(errorci)

    def debitar(self, numero, valor):
        try:
            conta = self.procurar_conta(numero)
            conta.debitar(valor)
        except CIException(numero) as errorci:
            print(errorci)
        except SIException(conta.get_saldo(), conta.get_numero()) as errorsi:
            print(errorsi)

    def saldo(self, numero):
        try:
            conta = self.procurar_conta(numero)
            conta.get_saldo()
        except CIException(numero) as errorci:
            print(errorci)

    def transferir(self, origem, destino, valor):
        pass
