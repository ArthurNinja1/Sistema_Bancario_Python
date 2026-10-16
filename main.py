from pessoa import Pessoa
from banco import Banco, Conta

def mostrar_menu():
    print("\n1 - Criar conta")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Ver extrato")
    print("5 - Sair")

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
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    pass
                case 0:
                    pass
                case _:
                    print("opcão invalida")
                    
        except ValueError as erro:
            print(f"erro: {erro}")