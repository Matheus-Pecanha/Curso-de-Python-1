# # Exemplo
def menu():
    print('1 - Falar com atendente')
    print('2 - Trocar de música')
    print('3 - Mudar de plano')
    print('4 - Para sair')
    
# while True:
#     menu()
    
#     opcao = int(input('Digite uma opcao acima: '))
    
#     if opcao == 1:
#         print('Falando com atendente...')
#     elif opcao == 2
#         print('Trocando de música...')
#     elif opcao == 3
#         print('Mudando de plano...')
#     else:
#         print('Saindo...')
#         break

        
def op(opcao):
    if opcao == 1:
        print('Falando com atendente...')
        return True
        
            
    elif opcao == 2:
        print('Trocando de músca...')
        return True
            
        
    elif opcao == 3:
        print('Mudando de plano...')
        return True
        
        
    else:
        print('Encerrando o programa...')
        return False
    
while True:
    menu()
    
    opcao = int(input('Digite uma opcao acima: '))
    
    teste = op(opcao)
    if teste == False:
        break
    
