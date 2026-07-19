# criando programa interativo
nome = input('Qual seu nome: ')
idade = input('Qual sua idade: ')
cidade = input('Qual sua cidade: ')
altura = input('Qual sua altura: ')
carteira = True

print('---Dados do Usuário---')
print('Nome: ',nome)
print('Idade: ', idade, 'anos')
print('Cidade: ', cidade)
print('Altura: ', altura ,'metros')
print('Carteira: True')





# Criando programa para informações de produto

produto = input('Qual o nome do seu produto: ')
preço = input('Digite o preço: R$')
quantidade = input('Digite a quantidade disponivel: ')
categoria = input('Digite a categoria: ')
Produto = False

print('---Produto Cadastrado---')
print('Produto: ', produto)
print('Preço: R$', preço)
print('Quantidade: ', quantidade)
print('Categoria: ', categoria)
print('Produto: ', Produto)



# Criando programa de calculo de produtos
produto1 = input('Quantidade do primeiro produto: ')
produto11 = input('Valor do primeiro produto: ')

produto2 = input('Quantidade do segundo produto: ')
produto22 = input('Valor do segundo produto: ')

soma = produto1 + produto2
som = produto11 + produto22
 
print('--- Resumo da Compra ---')
print('Quantidade total de produtos:', soma)
print('Valor total da compra: R$', som)


# Criando média de notas
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3) / 3

print('---Resultado---')
print('Nota final: ', media)

# Criando programa para comparar idade

idade = int(input('Digite sua idade: '))
b = 18
idade1 = (idade >= b)
idade2 = (idade < b)
idade3 = (idade == b)

print('A pessoa possui 18 anos ou mais: ', idade1)
print('A pessoa é menor de idade: ', idade2)
print('A idade é igual a 20 anos: ', idade3)

# Comparando preços

produto1 = int(input('Digite o preço do primeiro produto: '))
produto2 = int(input('Digite o preço do segundo produto: '))

comparacao1 = (produto1 < produto2)
comparacao2 = (produto2 > produto1)
comparacao3 = (produto1 == produto2)

print('O primeiro produto é menor que o segundo: ', comparacao1)
print('O segundo produto é maior que  primeiro: ', comparacao2)
print('Os produtos possuem o mesmo preço: ', comparacao3)

# Criando sistema para verificaçao

cadastro = True
senha = True

resultado = (cadastro == True) and (senha == True)

input('O usuário possui cadastro?: ')
input('Senha está correta?: ')

print('Resultado da validação: ', resultado)

# Criando desconto para cliente VIP

cliente = False
compra = 500

resultado = (cliente == False) or (compra > 500)

input('Cliente é vip?: ')
input('Valor da compra: ')
print('Cliente participa da promoção?: ', resultado)

# Criando sistema para verificar saldo de conta

conta = False
conta = not conta

input('A conta está bloqueada?: ')
print('A conta está liberada: ', conta)