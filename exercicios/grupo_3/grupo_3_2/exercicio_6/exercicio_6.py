"""
Grupo 3.2
Exercício: 6   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Desconto Condicional em Produtos: Peça o preço de 3 produtos. 
    Use um loop para processar cada produto. 
    Para cada um, se o preço for maior que R$50, aplique um desconto de 10% e mostre o preço final com ou sem desconto.
"""

def obter_preco_produto(numero):
    """Solicita e retorna o preço de um produto com validação."""
    while True:
        try:
            preco = float(input(f"Digite o preço do produto {numero}: R$"))
            if preco < 0:
                print("Preço não pode ser negativo. Tente novamente.")
                continue
            return preco
        except ValueError:
            print("Valor inválido. Digite um número.")

def calcular_desconto(preco):
    """Aplica 10% de desconto se o preço for maior que R$50."""
    if preco > 50:
        return preco * 0.9  # 10% de desconto
    return preco

def exibir_resultado(preco_original, preco_final):
    """Exibe o preço final, indicando se houve desconto."""
    if preco_final < preco_original:
        print(f"Preço com desconto: R${preco_final:.2f}")
    else:
        print(f"Preço sem desconto: R${preco_final:.2f}")

def main():
    """Processa 3 produtos: lê preços, aplica desconto e exibe resultados."""
    for i in range(1, 4):
        preco = obter_preco_produto(i)
        preco_com_desconto = calcular_desconto(preco)
        exibir_resultado(preco, preco_com_desconto)

if __name__ == "__main__":
    main()
