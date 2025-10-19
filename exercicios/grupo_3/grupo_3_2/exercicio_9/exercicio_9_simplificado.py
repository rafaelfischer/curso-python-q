# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Múltiplos de 5: Imprima todos os múltiplos de 5 que estão entre 1 e 50 (inclusive).

# Percorre de 1 a 50
for numero in range(1, 51):
    # Verifica se é múltiplo de 5
    if numero % 5 == 0:
        print(numero)
