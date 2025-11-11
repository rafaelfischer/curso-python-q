# Autor: Rafael Fischer 
# Data de Criação: 17/10/2025 
# Descrição da Solicitação: Crie uma loja virtual simplificada com as seguintes funcionalidades:
#							- Cadastro de clientes
#							- Exibição de produtos
#							- Adição de produtos à cesta
#							- Visualização da cesta
#							- Finalização da compra
#							- Sair da loja
#
#							O programa deve ser mais ou menos como o menu abaixo:
#							- menu com opções
#							    - 1 - cadastro o cliente
#							    - 2 - mostrar produtos
#							    - 3 - incluir produto na cesta
#							    - 4 - mostrar produtos da cesta
#							    - 5 - finalizar comprar
#							    - 6 - sair da loja
#							
#							E ter as seguintes funções:
#							- tem o cadastro do cliente: input e output de dados
#							- guarda a informação do cliente
#							- mostra os produtos
#							- o cliente escolhe o produto através de um código de 1 ate 4, e adiciona em uma cesta (array)
#							- o sistema mostra a cesta
#							- no final somente mostra o total de produtos na cesta, com a lista e o total e mostra a mensagem "Compra finalizada com sucesso"
# ---------- Variáveis globais ----------
cliente = {}          # Dicionário para armazenar dados do cliente
cesta_de_compras = []  # Lista para guardar produtos escolhidos
valor_total_da_compra = 0.0  # Soma dos valores dos produtos

# ---------- Catálogo de produtos ----------
catalogo_de_produtos = {
    1: {"nome": "Notebook", "preco": 2500.00},
    2: {"nome": "Mouse", "preco": 50.00},
    3: {"nome": "Teclado", "preco": 150.00},
    4: {"nome": "Monitor", "preco": 800.00}
}

# ---------- Funções ----------
def cadastrar_cliente():
    """Solicita dados do cliente e armazena no dicionário global."""
    global cliente

    print("\n--- Cadastro de Cliente ---")
    cliente["nome"] = input("Nome: ").strip()
    cliente["email"] = input("E-mail: ").strip()
    cliente["telefone"] = input("Telefone: ").strip()
    print("Cliente cadastrado com sucesso!\n")

def exibir_produtos():
    """Mostra os produtos disponíveis com código e preço."""
    print("\n--- Produtos Disponíveis ---")
    for codigo, informacao in catalogo_de_produtos.items():
        print(f"{codigo} - {informacao['nome']} - R$ {informacao['preco']:.2f}")
    print()

def adicionar_cesta():
    """Adiciona produto à cesta pelo código."""
    global cesta_de_compras, valor_total_da_compra
	
    exibir_produtos()
    try:
        codigo = int(input("Digite o código do produto (1-4): "))
        if codigo in catalogo_de_produtos:
            cesta_de_compras.append(catalogo_de_produtos[codigo])
            valor_total_da_compra += catalogo_de_produtos[codigo]["preco"]
            print(f"{catalogo_de_produtos[codigo]['nome']} adicionado à cesta!\n")
        else:
            print("Código inválido. Tente novamente.\n")
    except ValueError:
        print("Digite apenas números.\n")

def mostrar_cesta():
    """Exibe produtos na cesta e o total da compra."""
    if not cesta_de_compras:
        print("\nCesta vazia.\n")
        return

    print("\n--- Produtos na Cesta ---")
    for item in cesta_de_compras:
        print(f"- {item['nome']} - R$ {item['preco']:.2f}")
		
    global valor_total_da_compra
    print(f"Total: R$ {valor_total_da_compra:.2f}\n")

def finalizar_compra():
    """Mostra resumo da compra e encerra."""
    if not cesta_de_compras:
        print("\nCesta vazia. Nada para finalizar.\n")
        return
    mostrar_cesta()
    print("Compra finalizada com sucesso!\n")
    # Limpa cesta e total após finalização
    cesta_de_compras.clear()
	
    global valor_total_da_compra
    valor_total_da_compra = 0.0

def exibir_menu():
    """Apresenta opções do menu."""
    print("--- Menu ---")
    print("1 - Cadastrar cliente")
    print("2 - Mostrar produtos")
    print("3 - Incluir produto na cesta")
    print("4 - Mostrar produtos da cesta")
    print("5 - Finalizar compra")
    print("6 - Sair da loja")

# ---------- Loop principal ----------
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").strip()
    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        exibir_produtos()
    elif opcao == "3":
        adicionar_cesta()
    elif opcao == "4":
        mostrar_cesta()
    elif opcao == "5":
        finalizar_compra()
    elif opcao == "6":
        print("Obrigado! Volte sempre.")
        break
    else:
        print("Opção inválida. Tente novamente.\n")
