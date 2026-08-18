# Crie uma funcao par ou impar que receba um numero
# e retorne se o numero é par ou impar
# pergunte ao usuario um numero

numero = int(input('Digite um número: '))


def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'par'
    else:
        return 'impar'

print(par_ou_impar(numero))