# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte um número. Some todos os números de 1 até esse número. Atenção, utilize um loop WHILE.

# pede número ao usuário
numero = int(input("Digite um número: "))

# garante número positivo para somar
if numero < 0:
    numero = -numero

# somador
soma = 0

# loop while: soma de 1 até número
while numero > 0:
    soma += numero  # adiciona número à soma
    numero -= 1     # diminui número em 1

# mostra resultado
print("A soma de todos os números de 1 até o número digitado é:", soma)