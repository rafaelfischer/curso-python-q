# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que some de 0 a 100 os números pares, e exiba o resultado.

# Inicializa acumulador para soma dos pares
soma_pares = 0

# Percorre números de 0 a 100
for numero in range(0, 101):
    # Verifica se é par
    if numero % 2 == 0:
        soma_pares += numero  # Soma o par

# Exibe resultado
print("Soma dos pares de 0 a 100:", soma_pares)
