# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que pergunte um número. Exiba os números de 0 até o número digitado, separados por um espaço, exibindo o resultado.

# Pergunta o número ao usuário
numero_digitado = int(input("Digite um número: "))

# Exibe os números de 0 até o número digitado, separados por espaço
for numero_atual in range(numero_digitado + 1):
    print(numero_atual, end=" ")

# Pula linha ao final para deixar o terminal limpo
print()
