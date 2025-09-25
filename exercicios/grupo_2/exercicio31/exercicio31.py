"""
Objetivo do programa: Classificação de Triângulos: Dados três valores que representam os lados de um triângulo, determine:
                    - Se eles formam um triângulo (a soma de dois lados deve ser sempre maior que o terceiro lado).
                    - Se for um triângulo, classifique-o como "Equilátero" (todos os lados iguais), "Isósceles" (dois lados iguais) ou "Escaleno" (todos os lados diferentes).
Data da criação: 2025-09-25
Criado por: @rafaelfischer
"""

def is_triangulo(lado1, lado2, lado3):
    return (lado1 + lado2 > lado3) and (lado2 + lado3 > lado1) and (lado1 + lado3 > lado2)

def classificar_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 and lado2 == lado3:
        return "Equilátero"
    elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
        return "Isósceles"
    else:
        return "Escaleno"

try:
    lado1 = float(input("Digite o primeiro lado do triângulo: "))
    lado2 = float(input("Digite o segundo lado do triângulo: "))
    lado3 = float(input("Digite o terceiro lado do triângulo: "))

    if is_triangulo(lado1, lado2, lado3):
        tipo = classificar_triangulo(lado1, lado2, lado3)
        print(f"É um triângulo {tipo}")
    else:
        print("Não forma um triângulo")
except ValueError:
    print("Por favor, digite apenas números válidos.")

