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

def cadastrar_produto():
    """Coleta dados de um produto e retorna um dicionário."""
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
    return {"nome": nome, "fabricante": fabricante, "preco": preco}


def deseja_continuar():
    """Pergunta se o usuário quer cadastrar outro produto."""
    while True:
        opcao = input("\nCadastrar outro produto? (s/n): ").strip().lower()
        if opcao in ("s", "sim"):
            return True
        if opcao in ("n", "não", "nao"):
            return False
        print("Responda com 's' para sim ou 'n' para não.")


def exibir_catalogo(produtos):
    """Exibe todos os produtos cadastrados."""
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    print("\nProdutos cadastrados:\n")
    for idx, prod in enumerate(produtos, start=1):
        print(f"{idx}. Nome: {prod['nome']}")
        print(f"   Fabricante: {prod['fabricante']}")
        print(f"   Preço: R${prod['preco']:.2f}\n")


def main():
    """Função principal que coordena o fluxo do programa."""
    catalogo = []  # Lista para armazenar os produtos

    while True:
        print("\n--- Cadastro de Produto ---")
        produto = cadastrar_produto()
        catalogo.append(produto)

        if not deseja_continuar():
            break

    exibir_catalogo(catalogo)


if __name__ == "__main__":
    main()
