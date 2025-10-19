# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: (DESAFIO DA SEMANA 2) Crie um programa que permita cadastrar produtos com os seguintes dados: Nome, Fabricante e Preço.
#                           Após o cadastro de cada produto, pergunte ao usuário se deseja cadastrar outro. O processo deve continuar até que o usuário decida parar.
#                           Ao final, o programa deve pedir um valor limite e exibir apenas os produtos cujo preço seja menor ou igual a esse valor.
#
#                           Objetivos didáticos:
#                           - Uso de loops com condição de parada
#                           - Manipulação de estruturas de dados (arrays ou structs)
#                           - Aplicação de filtros após o loop
#
#                           Exemplo de saída esperada:
#                               Produto: Caneta
#                               Fabricante: Bic
#                               Preço: 2.50
#
#                               Produto: Caderno
#                               Fabricante: Tilibra
#                               Preço: 15.00
#
#                               Digite o valor limite: 10.00
#
#                                Produtos com preço até R$10.00:
#                               - Caneta (Bic) - R$2.50

# lista para guardar produtos
produtos = []

# loop para cadastrar produtos
while True:
    # entrada de dados
    nome = input("Produto: ").strip()
    fabricante = input("Fabricante: ").strip()
    preco = float(input("Preço: R$"))

    # adiciona produto na lista
    produtos.append({"nome": nome, "fabricante": fabricante, "preco": preco})

    # pergunta se quer continuar
    continuar = input("Cadastrar outro? (s/n): ").strip().lower()
    if continuar != "s":
        break

# pede valor limite
valor_limite = float(input("\nDigite o valor limite: R$"))

# filtra e exibe produtos dentro do limite
print(f"\nProdutos com preço até R${valor_limite:.2f}:")
for p in produtos:
    if p["preco"] <= valor_limite:
        print(f"- {p['nome']} ({p['fabricante']}) - R${p['preco']:.2f}")
