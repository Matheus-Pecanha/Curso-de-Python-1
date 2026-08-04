# Pergunte ao usuario 5 numeros e diga se o numero é positivo ou negativo
# Exemplo: 1 positivo, -2 negativo

# for i in range(5):
#     numero = int(input('Digite um numero: '))

#     if numero > 0:
#         print(f'O numero {numero} que você digitou é positivo')

#     elif numero < 0:
#         print(f'O numero {numero} que você digitou é negativo')

#     else:
#         print(f'O numero é igual a 0')        



lista = [20,50,88,95,74,62,31]
soma = 0

for i in range (len(lista)):
    soma = soma + lista[i]

print(f'Soma total do carrinho de compra foi de {soma}')
