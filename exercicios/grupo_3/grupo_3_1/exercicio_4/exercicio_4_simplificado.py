"""
Grupo 3.2
Exercício: 4   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Encontrar Primeiro Número Especial: Percorra os números de 1 a 100. 
    Assim que encontrar o primeiro número que seja maior que 10 E divisível por 7, imprima-o e encerre o loop imediatamente.
"""

# Percorre de 1 a 100
for numero in range(1, 101):
    # Verifica se é maior que 10 e divisível por 7
    if numero > 10 and numero % 7 == 0:
        print(numero)  # Imprime o primeiro que atende
        break          # Encerra o loop imediatamente
