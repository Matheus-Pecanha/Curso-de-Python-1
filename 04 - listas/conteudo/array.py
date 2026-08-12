# # Exemplo sem lista
# nome1 = 'Dudu'
# nome2 = 'Fabio'
# nome3 = 'Marcelo'
# nome4 = 'Bernardo'

# # Exemplo com lista
# nomes = ['Dudu','Fabio','Marcelo','Bernardo']

# # Acessando valor na lista (array)
# frutas = ['banana','uva','maça','manga']
# print(frutas[2]) # Maça
# print(frutas[1]) # Uva
# print(frutas) # todos os valores de uma vez

# # Sabendo quantos itens tem dentro do array
# tamanho_array_frutas = len(frutas)
# print(f'No array de frutas tem {tamanho_array_frutas} frutas')

# Passeando pelo array usando for
# carros = ['Fusca','Golf','Ferrari','Maverick','BMW','Kombi']

# for i in carros:
#     print(f'carros: {i}')

# Usando for para fazer soma

carrinho_compras = [150, 260, 100, 50, 60]
soma = 0

for i in carrinho_compras:
    soma = soma + i

print(f'A soma total dos produtos foi de R$ {soma},00')