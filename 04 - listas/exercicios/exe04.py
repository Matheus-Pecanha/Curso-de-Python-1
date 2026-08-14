# Peça ao usuario para cadastrar numeros em uma lista
# Conte quantos impares e pares tem nessa lista

lista_numerica = []
qtd_numeros = int(input('Digite a quantidade de números que deseja cadastrar: '))
soma_par = 0
soma_impar = 0
for i in range (qtd_numeros):
        numeros = int(input('Digite os números: '))
        lista_numerica.append(numeros)

        if (i % 2 == 0):
                soma_par = soma_par + 1
                

        else:
               soma_impar = soma_impar + 1    

print(f'Possuem {soma_par} numeros pares nessa lista')
print(f'Possuem {soma_impar} numeros impares nessa lista')   