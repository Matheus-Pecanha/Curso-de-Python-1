# Crie um programa que solicite o peso, a altura e mostre o imc da pessoa

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
imc_r = round(imc,2)

# imc menor que 18,5 - abaixo do peso
# entre 18,5 e 24,9 - normal
# entre 25,0 e 29,9 - excesso de peso
# entre 30,0 e 34,9 - obesidade classe I
# entre 35,0 e 39,9 - obesidade classe II
# maior ou igual a 40,0 - obesidade classe III

if (imc < 18.5):
    print(f'Seu imc é {imc_r}, você está abaixo do peso normal')

elif (imc >= 18.5) and (imc <= 24.9):
    print(f'Seu imc é {imc_r}, você está no peso ideal')

elif (imc >= 25) and (imc <= 29.9):
    print(f'Seu imc é {imc_r}, você está com excesso de peso')

elif (imc >= 30.0) and (imc <= 34.9):
    print(f'Seu imc é {imc_r}, você está com obesidade classe I')

elif (imc >= 35.0) and (imc <= 39.0):
    print(f'Seu imc é {imc_r}, você está com obesidade classe II')

else:
    print(f'Seu imc é {imc_r}, você está com obesidade classe III')