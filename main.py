from pessoa import Pessoa
from banco import Banco, Conta

def mostrar_menu():
    print("\n1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("0 - Sair")

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except  ValueError:
            print("Digite um numero inteiro valido")


def ler_valor(mensagem):
    while True:
        try:
            texto = input(mensagem).replace(",",".")
            valor = float(texto)
            if valor <= 0:
                print("o valor não pode ser igual ou menor a zero")
                continue
            return valor
        except ValueError:
            print("Digite umm valor valido,  por exemplo: 100 ou 100,00")

def main():
    banco = Banco()

    while True:
        mostrar_menu()
        opcao = ler_inteiro("Escolha uma opção: ")

        try:
            match opcao:
                case 1:
                    nome = input("nome: ")
                    cpf = input("cpf: ")
                    telefone = input("telefone: ")
                    email = input("email: ")
                    numero = banco.criar_conta(nome,cpf,telefone, email)
                    print(f"Conta criada com o numero: {numero}")

                case 2:
                    numero = ler_inteiro("numero da conta: ")
                    valor = ler_valor("valor de deposito: ")
                    banco.depositar(numero, valor)
                    print("Deposito realizado")
                case 3:
                    numero = ler_inteiro("numero da conta: ")
                    valor = ler_valor("valor de saque: ")
                    banco.sacar(numero, valor)
                    print("Saque realizado")

                case 4:
                    numero = ler_inteiro("numero da conta: ")
                    conta = banco.buscar_conta(numero)
                    if conta is None:
                        raise ValueError("conta não encontrada")
                    print(f"Saldo: {conta.saldo:.2f} R$".replace(".",","))
                    for linha in conta.historico:
                        print(linha)
                case 0:
                    exit
                case _:
                    print("opcão invalida")

        except ValueError as erro:
            print(f"erro: {erro}")


main()