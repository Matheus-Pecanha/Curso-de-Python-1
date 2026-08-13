# Comece com a lista vazia
# Com for adicione produtos em uma lista usando input() e append()
# E com outro for mostre os produtos cadastrados
lista_produtos = []
qtd_produtos = int(input('Quantos produtos você deseja cadastrar: '))

for i in range(qtd_produtos):
    produtos = input('Qual produto você deseja cadastrar: ')
    lista_produtos.append(produtos)


print('===== Os produtos cadastrados são =====')
for i in lista_produtos:
    print(f'Seus produtos são: {i}')

