# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Imprima os números de 10 a 1 em ordem decrescente. Atenção, utilize um loop FOR.

def imprimir_numeros_decrescente():
    print("Números de 10 a 1 em ordem decrescente:")
    # Itera de 10 a 1 (inclusive) em ordem decrescente
    for numero_atual in range(10, 0, -1):
        print(numero_atual, end=" ") # Exibe o número seguido de um espaço
    print() # Adiciona uma nova linha no final para melhor formatação

# Chama a função para executar o programa
imprimir_numeros_decrescente()