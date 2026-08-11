# Programa de estoque adicionando item por item

contador = 0

while contador < 10:
    adicionando_itens = int(input('Digite a quantidade de itens que deseja adicionar: '))
        
    if adicionando_itens <= 0:
         print('Quantidade invalida')
         continue

    if contador + adicionando_itens > 10:

        print(f'Quantidade inserida excedeu o limite')

        break     
           
    contador = contador + adicionando_itens
    print(f'Total acumulado foi de {contador}')


       
      
