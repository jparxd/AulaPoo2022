from Src.ProjectPy.Account.Account import Conta


class ContaPoupança(Conta):
    def __init__(self, numero):
        super().__init__(numero)

    def render_juros(self, taxa):
        self.creditar(self.get_saldo()*taxa)
