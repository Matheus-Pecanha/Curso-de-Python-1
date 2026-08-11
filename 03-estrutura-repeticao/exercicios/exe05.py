# Jogo da adivinhação
numero_secreto = 14
tentativas = 5


while tentativas >= 1:
    chute = int(input('Chute um número: '))
    tentativas -= 1
    if chute < numero_secreto:
        
        print(f'O número secreto é maior que o valor informado pelo usuário, você tem {tentativas} tentativas')

    if chute > numero_secreto:
        
        print(f'O número secreto é menor que o valor informado pelo usuário, você tem {tentativas} tentativas')

    if chute == numero_secreto:
        print(f'Você acertou o número secreto!!! Parabéns')
        break    
    
else:
    print(f'Game Over! Suas tentativas acabaram.')    