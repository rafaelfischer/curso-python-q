# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que mostra os números de 0 a 100.

def mostrar_numeros_de_zero_a_cem():
    print("Números de 0 a 100:")
    # Itera de 0 a 100 e exibe cada número
    for numero_atual in range(101):
        print(numero_atual, end=" ") # Exibe o número seguido de um espaço
    print() # Adiciona uma nova linha no final para melhor formatação

# Chama a função para executar o programa
mostrar_numeros_de_zero_a_cem()