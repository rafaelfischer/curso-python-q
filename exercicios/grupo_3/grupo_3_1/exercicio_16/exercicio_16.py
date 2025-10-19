# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: (DESAFIO DA SEMANA 3)
#                           Implemente um programa que cadastre produtos com Nome, Fabricante e Preço.
#                           Após cada cadastro, pergunte se deseja continuar.
#                           Ao final, o programa deve exibir todos os produtos cadastrados e destacar o produto mais caro.
#                           Objetivos didáticos:
#                           - Uso de loops com controle por resposta
#                           - Comparação de valores dentro do loop
#                           - Identificação de máximo valor
#                           Exemplo de saída esperada:
#                           Produtos cadastrados:
#                           - Caneta (Bic) - R$2.50
#                           - Caderno (Tilibra) - R$15.00
#                           - Mochila (Nike) - R$120.00
#                           Produto mais caro:
#                           - Mochila (Nike) - R$120.00

def cadastrar_produto():
    """Coleta dados de um produto e retorna tupla (nome, fabricante, preço)."""
    nome = input("Nome do produto: ").strip()
    fabricante = input("Fabricante: ").strip()
    while True:
        try:
            preco = float(input("Preço (R$): ").replace(",", "."))
            if preco < 0:
                print("Preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Digite um valor numérico válido.")
    return nome, fabricante, preco


def deseja_continuar():
    """Pergunta se o usuário quer cadastrar mais produtos."""
    while True:
        escolha = input("Cadastrar outro produto? (s/n): ").strip().lower()
        if escolha in ("s", "sim"):
            return True
        if escolha in ("n", "não", "nao"):
            return False
        print("Responda com 's' ou 'n'.")


def exibir_produtos(produtos):
    """Lista todos os produtos cadastrados."""
    print("\nProdutos cadastrados:")
    for nome, fabricante, preco in produtos:
        print(f"- {nome} ({fabricante}) - R${preco:.2f}")


def encontrar_mais_caro(produtos):
    """Retorna o produto com maior preço."""
    if not produtos:
        return None
    return max(produtos, key=lambda p: p[2])


def main():
    """Loop principal de cadastro e exibição dos resultados."""
    produtos = []

    while True:
        print("\n--- Cadastro de Produto ---")
        produto = cadastrar_produto()
        produtos.append(produto)

        if not deseja_continuar():
            break

    exibir_produtos(produtos)

    mais_caro = encontrar_mais_caro(produtos)
    if mais_caro:
        nome, fabricante, preco = mais_caro
        print(f"\nProduto mais caro:")
        print(f"- {nome} ({fabricante}) - R${preco:.2f}")


if __name__ == "__main__":
    main()
