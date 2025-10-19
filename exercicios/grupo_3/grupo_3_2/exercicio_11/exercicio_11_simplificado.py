# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Soma dos N Primeiros Números: Peça ao usuário um número N e calcule a soma de todos os números inteiros de 1 a N.

# pede número ao usuário
numero = int(input("Digite um número N: "))

# acumulador da soma
soma = 0

# percorre de 1 até N
for i in range(1, numero + 1):
    soma += i  # adiciona cada número

# mostra resultado
print("A soma de 1 a", numero, "é:", soma)
