class SIException(Exception):
    def __init__(self, saldo, numero, message='Saldo Insuficiente!'):
        self.saldo = saldo
        self.numero = numero
        self.message = message
        super().__init__(self.message)

    def numeroconta(self):
        return self.numero

    def saldoconta(self):
        return self.saldo
