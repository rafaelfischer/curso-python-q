# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: (DESAFIO DA SEMANA 1)
#                           Crie um programa que permita ao usuário cadastrar produtos com os seguintes dados:
#                           • Nome do produto
#                           • Fabricante
#                           • Preço
#
#                           Após o cadastro de cada produto, o programa deve perguntar se o usuário deseja cadastrar outro.
#                           O processo deve continuar até que o usuário decida parar (válvula de escape).
#                           Ao final, o programa deve exibir todo o catálogo de produtos cadastrados, mostrando os dados de cada um.
# 
#                           Objetivos didáticos:
#                           • Uso de vetores/arrays para armazenar múltiplos registros
#                           • Manipulação de strings e números
#                           • Controle de fluxo com loops e condição de parada
#                           • Exibição estruturada de dados
# 
#                           Exemplo de saída esperada:
#                           Produtos cadastrados:
#
#                           1. Nome: Caneta Azul
#                           Fabricante: Bic
#                           Preço: R$2.50
#
#                           2. Nome: Caderno Universitário
#                           Fabricante: Tilibra
#                           Preço: R$15.00
#
#                           3. Nome: Mochila Escolar
#                           Fabricante: Nike
#                           Preço: R$120.00

# lista para guardar todos os produtos
produtos = []

# loop infinito para cadastrar
while True:
    # pede os dados
    nome = input("Nome do produto: ")
    fabricante = input("Fabricante: ")
    preco = float(input("Preço: R$"))

    # guarda o produto na lista
    produtos.append([nome, fabricante, preco])

    # pergunta se quer continuar
    continuar = input("Cadastrar outro? (s/n): ").lower()
    if continuar != 's':
        break

# mostra o catálogo
print("\nProdutos cadastrados:\n")
for indice, produto in enumerate(produtos, 1):
    print(f"{indice}. Nome: {produto[0]}")
    print(f"   Fabricante: {produto[1]}")
    print(f"   Preço: R${produto[2]:.2f}\n")
