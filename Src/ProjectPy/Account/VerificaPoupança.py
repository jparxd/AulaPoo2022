from Src.ProjectPy.Account.Account import Conta
from Src.ProjectPy.Account.AccountSavings import ContaPoupança


class VerificaPoupança:
    if __name__ == '__main__':
        opçao = int(input('Escolha: [1] para Conta e [2] para Poupança: '))
        if opçao == 1:
            conta = Conta('21.342-7')
        else:
            conta = ContaPoupança('21.342-7')

    conta.creditar(500.87)
    conta.debitar(45.00)

    if isinstance(conta, ContaPoupança):
        conta.render_juros(0.1)
        print('Saldo com juros: {}'.format(conta.get_saldo()))
