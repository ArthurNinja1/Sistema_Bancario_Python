from pessoa import Pessoa

class Conta:
    def __init__(self, numero, titular):
        self.numero = numero
        self.titular = titular
        self.saldo = 0
        self.historico = []

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser positivo")
        self.saldo += valor


        self.historico.append(f"Depósito: +{valor:.2f} R$".replace(".", ","))

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser positivo")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor
        self.historico.append(f"Saque: -{valor:.2f} R$".replace(".", ","))

    

class Banco:
    def __init__(self):
        self.contas = {}
        self.proximo_numero = 1

    def criar_conta(self, nome, cpf, telefone, email):
        titular = Pessoa(nome, cpf, telefone, email)
        numero = self.proximo_numero
        conta = Conta(numero, titular)

        self.contas[numero] = conta
        self.proximo_numero += 1
        return numero

    def buscar_conta(self, numero):
        return self.contas.get(numero)


    def depositar(self, numero, valor):
        conta = self.buscar_conta(numero)

        if conta is None:
            raise ValueError("Conta não encontrada")
        conta.depositar(valor)

    def sacar(self, numero, valor):
        conta = self.buscar_conta(numero)

        if conta is None:
            raise ValueError("Conta não encontrada")
        conta.sacar(valor)




if __name__ == "__main__":
    banco = Banco()
    numero = banco.criar_conta("Maria Souza", "12345678901", "66999990000", "maria@email.com")

    banco.depositar(numero, 100)
    banco.sacar(numero, 30)

    conta = banco.buscar_conta(numero)
    print(conta.saldo)
    print(conta.historico)
    try:
        banco.sacar(numero, 1000)
    except ValueError as erro:
        print("Erro:", erro)