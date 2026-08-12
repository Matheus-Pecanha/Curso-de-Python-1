# Calcule a media das notas e mostre no print
notas = [5.5, 8, 9.2, 5]
soma_notas = 0
nota1 = notas[0]
nota2 = notas[1]
nota3 = notas[2]
nota4 = notas[3]
quantidade_notas = len(notas)

# media = (nota1 + nota2 + nota3 + nota4) / quantidade_notas
# print(f'A media é {media}')

# Soma das notas
 
for i in notas:
    soma_notas = soma_notas + i

media = soma_notas / quantidade_notas

if media >= 7:
    print('Aprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')    
else:
    print(f'Reprovado')   

print(f'A soma total das notas foi {soma_notas} e a média é {media:.2f}')
 