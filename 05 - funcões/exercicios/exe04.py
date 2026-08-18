# Crie um programa que tenha uma função SuperSomador(), que vai receber dois 
# numeros como parametro e depois vai retornar a soma de todos os valores no 
# intervalo entre os valores recebidos.
#Ex: 

#SuperSomador(1,6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
#SuperSomador(15,19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite um número: '))


def SuperSomador(numero1,numero2):
    soma = 0
    for i in range(numero1,numero2+1):
        soma += i
        
    return soma 

print(f'O valor total das somas é: {SuperSomador(numero1,numero2)}')
