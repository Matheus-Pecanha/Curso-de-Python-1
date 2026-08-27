# Importar o modulo csv
import csv

# # armazenar a planilha em uma variavel
planilha = "07 - projeto\produtos-python.csv"

# # criar funcao para LER a planilha 
def carregar_produtos():
    # criar o array vazio
    produtos = []

    with open(planilha, 'r', encoding="utf-8-sig") as arquivo:
        # Pegando a planilha e tranformando em um dicionario
        leitor = csv.DictReader(arquivo)

        for linha in leitor:
            linha['preco'] = float(linha['preco'])
            linha['quantidade'] = int(linha['quantidade'])

            # Adiciona essas linhas 
            produtos.append(linha)

    return produtos

# print(carregar_produtos())

# Função para mostrar produtos
def mostrar_produtos(produtos):
    # Titulo
    print("\n ==== PRODUTOS =====")

    for produto in produtos:
        print(
            f'{produto['produto']} | '
            f'{produto['categoria']} | '
            f'R$ {produto['preco']:.2} | '
            f'Estoque {produto['quantidade']} | '
            f'{produto['fornecedor']}'
        )

# Funcao para calcular média
def calcular_media(produtos):
    soma = 0

    for produto in produtos:
        soma += produto['preco']

    media = soma / len(produtos)

    print(f'\n A média de preços é de: R$ {media:.2f}')

# Funcão para filtrar valores acima de algum valor
def produtos_acima(produtos):

    valor = float(input('\nMostrar produtos acima de R$: '))
    encontrados = 0

    for produto in produtos:
        if produto ['preco'] > valor:
            print(
                f'{produto['produto']} - '
                f'R${produto['preco']:.2f} - '
            )

            encontrados += 1

    if encontrados == 0:
        print("Nenhum produto encontrado.")


# Função para filtrar valores abaixo de algum valor
def produtos_abaixo(produtos):

    valor2 = float(input('\nMostrar produtos abaixo de R$: '))
    encontrados2 = 0

    for produto in produtos:
        if produto ['preco'] < valor2:
            print(
                f'{produto['produto']} - '
                f'R${produto['preco']:.2f} - '
            )

            encontrados2 += 1

    if encontrados2 == 0:
        print('Nenhum produto encontrado')

# Funcão para pegar o produto mais caro
def produto_mais_caro(produtos):
    mais_caro = produtos[0]

    for produto in produtos:
        if produto['preco'] > mais_caro['preco']:
            mais_caro = produto

    print("==== PRODUTO MAIS CARO É =====")

    print(f'Produto: {mais_caro['produto']}')
    print(f'Preco: {mais_caro['preco']:.2f}')
    print(f'Categoria: {mais_caro['categoria']}')

def produto_mais_barato(produtos):
    mais_barato = produtos[0]

    for produto in produtos:
        if produto['preco'] < mais_barato['preco']:
            mais_barato = produto

    print("==== PRODUTO MAIS BARATO É ====")

    print(f'Produto: {mais_barato['produto']}')
    print(f'Preco: {mais_barato['preco']:.2f}')
    print(f'Categoria: {mais_barato['categoria']}')




produtos = carregar_produtos()

while True:

    opcao = int(input('Digite um opcao: '))

    if opcao == 1:
        mostrar_produtos(produtos)
    elif opcao == 2:
        calcular_media(produtos)
    elif opcao == 3:
        produtos_acima(produtos)
    elif opcao == 4:
        produtos_abaixo(produtos)
    elif opcao == 5:
        produto_mais_caro(produtos)
    elif opcao == 6:
        produto_mais_barato(produtos)