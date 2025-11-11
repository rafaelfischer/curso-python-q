"""
Grupo 3.2
Exercício: 1
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
	Imprimir Números Pares em Intervalo: Crie um algoritmo que use um loop para percorrer os números de 1 a 20 e imprima apenas os números pares.
"""
# Loop de 1 a 20
for numero in range(1, 21):
    # Verifica se é par
    if numero % 2 == 0:
        print(numero)
