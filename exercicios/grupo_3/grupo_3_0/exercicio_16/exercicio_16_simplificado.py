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

# lista para guardar os produtos
produtos = []

# variáveis para o produto mais caro
mais_caro_nome = ""
mais_caro_fabricante = ""
mais_caro_preco = 0

# loop de cadastro
while True:
    # entrada de dados
    nome = input("Nome do produto: ")
    fabricante = input("Fabricante: ")
    preco = float(input("Preço: R$"))

    # guarda produto na lista
    produtos.append((nome, fabricante, preco))

    # verifica se é o mais caro até agora
    if preco > mais_caro_preco:
        mais_caro_nome = nome
        mais_caro_fabricante = fabricante
        mais_caro_preco = preco

    # pergunta se continua
    continua = input("Deseja cadastrar outro? (s/n): ").lower()
    if continua != 's':
        break

# exibe todos os produtos cadastrados
print("\nProdutos cadastrados:")
for nome, fabricante, preco in produtos:
    print(f"- {nome} ({fabricante}) - R${preco:.2f}")

# exibe o mais caro
print(f"\nProduto mais caro:")
print(f"- {mais_caro_nome} ({mais_caro_fabricante}) - R${mais_caro_preco:.2f}")
