class CheckingAccount(BankAccount):
    def __init__(self, titular, saldo=0, limite_cheque_especial=500):
        super().__init__(titular, saldo)
        self.limite_cheque_especial = limite_cheque_especial

    def withdraw(self, valor):
        limite_total = self.saldo + self.limite_cheque_especial
        if valor <= limite_total:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Erro: valor excede o limite disponível (saldo + cheque especial).")

    def display_details(self):
        super().display_details()
        print(f"Limite Cheque Especial: R${self.limite_cheque_especial:.2f}")
