# Criando um programa de banco
# saldo = 10
# saque = float(input('Digite o valor que deseja sacar: '))
# resultado = saldo - saque
# resultado2 = resultado - saque

# while saldo > 0:
#     print('Saldo insuficiente')
#     saque = float(input('Digite o valor que deseja sacar: '))
#     if saque > saldo:
#         saldo -= saque
#         print(f'Seu saldo atual é de R${resultado}, o seu saldo é de R${saldo}')
#     continue

# else:
#     print('Programa finalizado')



saldo_inicial = 500
print(f'Saldo: R$ {saldo_inicial}')

while saldo_inicial > 0:
    valor_saque = int(input('Digite o valor que deseja sacar: '))
    if valor_saque <= saldo_inicial:
        saldo_inicial -= valor_saque
        print(f'Saldo atual: R${saldo_inicial}')
        continue

    if valor_saque == 0:
        break

    if valor_saque > saldo_inicial:
        print('Saldo indisponivel')
        continue
    



else:
    print('Saldo insuficiente')

    









     
         
   



