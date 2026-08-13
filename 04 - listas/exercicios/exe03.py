# Criando um programa que pede o numero ao cliente para criar uma lista com os numeros e os mesmos ao quadrado
quadrados = []
q = []
soma = 0

for i in range (5):
    numeros_inteiros = int(input('Digite um número: '))
    quadrados.append(numeros_inteiros)

print( '==== Quadrados =====)' )

for i in quadrados:
    print(i ** 2)
    q.append(i ** 2)


for i in q:
    soma = soma + i

print(f'A soma dos quadrados é {soma}')


