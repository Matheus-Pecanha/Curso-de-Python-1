# Para criar uma função com retorno
def soma (a,b):
    return a + b

# Função com retorno, podemos colocar dentro de uma variavel
total = soma(10,20)
print(f'O total da soma foi de: {total}')   

# Saudação
def saudacao(nome):
    return f'Olá, seja bem vindo(a) {nome}'

mensagem = saudacao('Matheus')
print(mensagem)