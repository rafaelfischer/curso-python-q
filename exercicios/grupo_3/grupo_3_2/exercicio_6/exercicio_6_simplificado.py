"""
Grupo 3.2
Exercício: 6   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Desconto Condicional em Produtos: Peça o preço de 3 produtos. 
    Use um loop para processar cada produto. 
    Para cada um, se o preço for maior que R$50, aplique um desconto de 10% e mostre o preço final com ou sem desconto.
"""

# loop para 3 produtos
for i in range(1, 4):
    # pergunta o preço
    preco = float(input(f"Digite o preço do produto {i}: "))
    
    # verifica desconto
    if preco > 50:
        preco_final = preco * 0.9  # 10% desconto
        print(f"Preço com desconto: R${preco_final:.2f}")
    else:
        print(f"Preço sem desconto: R${preco:.2f}")
