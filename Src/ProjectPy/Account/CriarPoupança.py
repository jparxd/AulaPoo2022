from Src.ProjectPy.Account.Account import Conta
from Src.ProjectPy.Account.AccountSavings import ContaPoupança


class CriarPoupança:
    if __name__ == '__main__':
        conta = Conta('21.342-7')
        conta = ContaPoupança(conta)
        conta.creditar(500.87)
        conta.debitar(45.00)
        print(conta.get_saldo())
        conta.render_juros(0.01)
        print(conta.get_saldo())
