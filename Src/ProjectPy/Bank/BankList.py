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
        conta = self.procurar_conta(numero)
        if conta:
            conta.creditar(valor)
        else:
            print('conta inexistente')

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.debitar(valor)
        else:
            print('conta inexistente')

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            conta.get_saldo()
        else:
            print('conta inexistente')

    def transferir(self, origem, destino, valor):
        pass
