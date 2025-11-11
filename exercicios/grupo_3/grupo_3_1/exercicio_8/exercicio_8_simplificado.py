"""
Grupo 3.2
Exercício: 8   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Listar Números Múltiplos Duplos: De 1 a 100, use um loop para listar todos os números que são divisíveis por 4 E também por 6.
"""

# Loop de 1 a 100
for numero in range(1, 101):
    # Verifica se é múltiplo de 4 e 6
    if numero % 4 == 0 and numero % 6 == 0:
        # Mostra o número
        print(numero)
