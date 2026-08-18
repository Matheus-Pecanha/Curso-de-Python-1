# Forma ERRADA de repetir algo

# n1 = 1
# n2 = 2
# n3 = 3
# n4 = 4
# n5 = 5

# print(n1)
# print(n2)
# print(n3)
# print(n4)
# print(n5)

# # Forma CERTA de repetir algo
# print('====== REPETICAO COM FOR ======')

# for i in range(5):
#     print(f'Numero: {i}')

# print('=== Contar até 50 de 2 em 2 === ')

# for i in range(1,50,2):
#     print(f'Número {i}')

# print('==== Perguntar varias vezes algo ==== ')

# qtd_pessoas = int(input('Quantas pessoas você quer cadastrar? '))
# for i in range(qtd_pessoas):
#     nome = input('Qual seu nome? ')
#     print(f'Olá {nome}')


# Exemplo = tabuada do 9


# for i in range(1,11):
#     print(f'9 x {i} = {9*i}')

# Pergunta ao usuario a tabuada de um numero e até quanto?
tabuada = int(input('Qual tabuada você quer saber? '))
vezes = int(input('Até quantas vezes? '))

for i in range(vezes):
    print(f'{tabuada} * {i} = {tabuada * i}')