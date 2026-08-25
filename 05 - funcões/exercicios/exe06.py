saldo = 1000
def consultar_saldo(saldo):
    print(f'Seu saldo atual é: R${saldo}')

def mostrar_menu():
    print('==== Banco Python ====')
    print('1 - Consultar saldo')
    print('2 - Retirar dinheiro')
    print('3 - Depositar dinheiro')
    print('4 - Sair')

def retirada(saldo):
    valor_retirada = float(input('Digite o valor que deseja retirar: '))
    
    if valor_retirada > saldo:
        print('Saldo insuficiente para realizar a retirada!')
        return saldo
    
    novo_saldo = saldo - valor_retirada
    print(f'Saque realizado com sucesso! Salto atual: R$ {novo_saldo}')
    return novo_saldo

def depositar(saldo):
    valor_deposito = float(input('Digite o valor que deseja depositar: '))
    saldo += valor_deposito
    print(f'Deposito realizado com sucesso! Saldo atual: R$ {saldo}')
    return saldo

def consultar_saldo(saldo):
    return f'Seu saldo atual é: R$ {saldo}'




while True:

    mostrar_menu()

    opcao_escolha = int(input('Escolha uma opção: '))
     
    if opcao_escolha == 1:
        print(consultar_saldo(saldo))

    elif opcao_escolha == 2:
        saldo = retirada(saldo)

    elif opcao_escolha == 3:
        saldo = depositar(saldo)

    elif opcao_escolha == 4:
        print('Saindo do programa!')
        break    

    else:
        print('Opção inválida')