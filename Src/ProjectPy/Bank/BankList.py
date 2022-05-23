from Src.ProjectPy.Exception.CIException import CIException
from Src.ProjectPy.Exception.SIException import SIException


class BankList:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta):
        self.contas.append(conta)

    def procurar_conta(self, numero):
        achou = False

        for elemento in self.contas:
            if elemento.get_numero() == numero:
                achou = True
                return elemento
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
