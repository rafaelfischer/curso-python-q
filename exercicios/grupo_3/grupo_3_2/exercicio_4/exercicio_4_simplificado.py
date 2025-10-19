# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Números Ímpares: Elabore um programa que mostre apenas os números ímpares de 1 a 19.

# loop de 1 a 19
for numero in range(1, 20):
    # verifica se é ímpar
    if numero % 2 != 0:
        print(numero)
