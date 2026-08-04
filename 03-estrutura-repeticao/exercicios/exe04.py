# Programa de estoque adicionando item por item

contador = 0
print(f'Quantidade de itens: {contador}')

while contador < 10:
    adicionando_itens = int(input('Digite a quantidade de itens que deseja adicionar: '))
        
    if adicionando_itens >= contador:
        contador += adicionando_itens
        print(f'A quantidade atual de itens é de {contador}')

    if adicionando_itens >= 10:
        break    

    
       
        

else:
    print('Você ultrapassou o limite máxio de itens')    
