# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que imprima os números pares de 2 a 20 inclusive, ou seja, incluindo o 2 e o 20.

def imprimir_pares_de_dois_a_vinte():
    print("Números pares de 2 a 20:")
    # Itera de 2 a 20 (inclusive) com passo de 2 para pegar apenas os pares
    for numero_par in range(2, 21, 2):
        print(numero_par, end=" ") # Exibe o número par seguido de um espaço
    print() # Adiciona uma nova linha no final para melhor formatação

# Chama a função para executar o programa
imprimir_pares_de_dois_a_vinte()