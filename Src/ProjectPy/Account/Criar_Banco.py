from Src.ProjectPy.Bank.Bank import Banco


class criarbanco:
    if __name__ == "__main__":
        banco = Banco()
        banco.cadastrar('21.342-7')
        banco.creditar('21.342-7',400.00)
        print(banco.saldo('21.342-7'))
