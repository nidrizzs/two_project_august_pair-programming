import sys
import os

# Ajusta o caminho para o Python achar o pacote 'banco'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from banco.operacoes import criar_conta, depositar, sacar, exibir_extrato

def menu():
    print("\n--- BANCO PYTHON ---")
    print("1. Criar Conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Ver Extrato")
    print("0. Sair")
    return input("Escolha uma opção: ")

def rodar_sistema():
    conta = None

    while True:
        opcao = menu()

        if opcao == "1":
            titular = input("Digite o nome do titular: ")
            numero = input("Digite o número da conta: ")
            saldo_iniciar = float(input("Digite o saldo inicial (ou 0): "))
            conta = criar_conta(titular, numero, saldo_iniciar)
            print("✅ Conta criada com sucesso!")

        elif opcao == "2":
            if conta is None:
                print("❌ Crie uma conta primeiro!")
            else:
                valor = float(input("Digite o valor do depósito: R$ "))
                depositar(conta, valor)

        elif opcao == "3":
            if conta is None:
                print("❌ Crie uma conta primeiro!")
            else:
                valor = float(input("Digite o valor do saque: R$ "))
                sacar(conta, valor)

        elif opcao == "4":
            if conta is None:
                print("❌ Crie uma conta primeiro!")
            else:
                exibir_extrato(conta)

        elif opcao == "0":
            print("Saindo do sistema... Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    rodar_sistema()