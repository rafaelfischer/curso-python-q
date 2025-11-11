"""
Grupo 3.2
Exercício: 3   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Números Pares: Escreva um algoritmo que imprima apenas os números pares de 2 a 20.
"""
# Loop de 2 até 20 (inclusive)
for numero in range(2, 21):
    # Verifica se é par
    if numero % 2 == 0:
        print(numero)
