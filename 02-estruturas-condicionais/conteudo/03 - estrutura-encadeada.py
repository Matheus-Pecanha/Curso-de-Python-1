# Permite varias condições
# nota = float(input('Digite sua nota: '))

# if nota >= 7:
#     print('Aprovado')

# elif nota >= 5:
#     print('Recuperação') 

# else:
#     print('Reprovado')


# print('--------- EXEMPLO ---------')

# idade = int(input('Digite sua idade: '))

# # menor que 12 - criança
# # menor que 18 - adolescente
# # menor que 60 - adulto
# # melhor idade           

# if idade < 12:
#     print('Você é uma criança')

# elif idade < 18:
#     print('Você é um adolescente')

# elif idade < 60:
#     print('Você é um adulto')

# else:
#     print('Melhor idade')

print(' ========== EXEMPLO 2 ==========')

usuario = input('Possui cadastro? (S/N): ')
senha = input('Senha correta? (S/N): ')

if  usuario == 'S' and senha == 'S':
    print('Acesso liberado')

else:
    print('Acesso negado')    