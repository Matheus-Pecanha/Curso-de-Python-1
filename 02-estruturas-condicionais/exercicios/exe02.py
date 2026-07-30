# Programa que recebe valores dos triangulos e os identifica

# Triangulo equilatero - os 3 lados iguais
# Triangulo isoceles - 2 lados iguais
# Triangulo escaleno - todos os lados diferentes

lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))


triangulo_equilatero = (lado1 == lado2 == lado3)
triangulo_isoceles = (lado1 == lado2 != lado3) or (lado1 != lado2 == lado3) or (lado1 == lado3 != lado2)
triangulo_escaleno = (lado1 + lado2 > lado3) and (lado1 < lado2 + lado3) and (lado1 + lado3 < lado2)

if triangulo_equilatero:
    print(f'Com base nas medidas o triangulo equilatero foi desenhado')

elif triangulo_isoceles:
    print(f'Com base nas medidas o triangulo isoceles foi desenhado')

elif triangulo_escaleno:
    print(f'Com base nas medidas o triangulo escaleno foi desenhado')

else:
    print('Os valores informados não formam um triângulo.')

