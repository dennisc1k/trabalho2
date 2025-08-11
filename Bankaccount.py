class BankAccount:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    def deposit(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def withdraw(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")

    def display_details(self):
        print(f"Titular: {self.titular}")
        print(f"Saldo: R${self.saldo:.2f}")
