# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que exiba de 0 a 100, somente os números ímpares e não divísiveis por 5, e exiba o resultado.

# Percorre de 0 a 100
for numero in range(0, 101):
    # Verifica se é ímpar e não divisível por 5
    if numero % 2 != 0 and numero % 5 != 0:
        print(numero)
