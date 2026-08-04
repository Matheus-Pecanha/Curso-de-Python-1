# Programa de estoque adicionando item por item

contador = 0
print(f'Quantidade de itens: {contador}')

while contador <= 10:
    adicionar_item = int(input('Digite a quantidade de itens que deseja adicionar: '))
    contador += adicionar_item

    if adicionar_item >= contador:
        contador =+ adicionar_item
        print(f'A quantidade atual de itens é de {adicionar_item}')

