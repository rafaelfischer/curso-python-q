# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Imprima os múltiplos de 3 entre 1 e 30, sem usar funções. Atenção, utilize um loop WHILE.

# Inicializa o contador
numero = 1

# Loop while de 1 a 30
while numero <= 30:
    # Verifica se é múltiplo de 3
    if numero % 3 == 0:
        # Imprime o múltiplo
        print(numero)
    # Incrementa o contador
    numero += 1
