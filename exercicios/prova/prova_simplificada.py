# Autor: Rafael Fischer 
# Data de Criação: 17/10/2025 
# Descrição da Solicitação: Crie uma loja virtual com as seguintes funcionalidades:
#							- Cadastro de clientes
#							- Exibição de produtos
#							- Adição de produtos à cesta
#							- Visualização da cesta
#							- Finalização da compra
#							- Sair da loja

#							- menu com opções
#							    - 1 - cadastro o cliente
#							    - 2 - mostrar produtos
#							    - 3 - incluir produto na cesta
#							    - 4 - mostrar produtos da cesta
#							    - 5 - finalizar comprar
#							    - 6 - sair da loja
#							
#							- tem o cadastro do cliente: input e output de dados
#							- guarda a informação do cliente
#							- mostra os produtos
#							- o cliente escolhe o produto através de um código de 1 ate 4, e adiciona em uma cesta (array)
#							- o sistema mostra a cesta
#							- no final somente mostra o total de produtos na cesta, com a lista e o total e mostra a mensagem "Compra finalizada com sucesso"
# lista de produtos disponíveis
produtos = {
    1: {"nome": "Notebook", "preco": 2500.00},
    2: {"nome": "Mouse", "preco": 50.00},
    3: {"nome": "Teclado", "preco": 150.00},
    4: {"nome": "Monitor", "preco": 800.00}
}

# variáveis principais
cliente = {}
cesta_de_compras = []
programa_continuar = True

# loop principal do programa
while programa_continuar:
    # exibe o menu
    print("\n=== LOJA VIRTUAL ===")
    print("1 - Cadastrar cliente")
    print("2 - Mostrar produtos")
    print("3 - Adicionar produto à cesta")
    print("4 - Mostrar cesta")
    print("5 - Finalizar compra")
    print("6 - Sair da loja")

    # escolha do usuário
    opcao_escolhida = input("Escolha uma opção: ")

    # cadastro do cliente
    if opcao_escolhida == "1":
        cliente["nome"] = input("Nome do cliente: ")
        cliente["email"] = input("E-mail do cliente: ")
        print("Cliente cadastrado com sucesso!")

    # mostrar produtos
    elif opcao_escolhida == "2":
        print("\nProdutos disponíveis:")
        for codigo_produto, produto in produtos.items():
            print(f"{codigo_produto} - {produto['nome']} - R$ {produto['preco']:.2f}")

    # adicionar produto à cesta
    elif opcao_escolhida == "3":
        print("\nProdutos disponíveis:")
        for codigo_produto, produto in produtos.items():
            print(f"{codigo_produto} - {produto['nome']} - R$ {produto['preco']:.2f}")
        codigo_digitado = int(input("Digite o código do produto (1-4): "))
        if codigo_digitado in produtos:
            produto_escolhido = produtos[codigo_digitado]
            cesta_de_compras.append(produto_escolhido)
            print(f"{produto_escolhido['nome']} adicionado à cesta!")
        else:
            print("Código inválido.")

    # mostrar cesta
    elif opcao_escolhida == "4":
        if not cesta_de_compras:
            print("Cesta vazia.")
        else:
            print("\nCesta de compras:")
            for item_da_cesta in cesta_de_compras:
                print(f"- {item_da_cesta['nome']} - R$ {item_da_cesta['preco']:.2f}")

    # finalizar compra
    elif opcao_escolhida == "5":
        if not cesta_de_compras:
            print("Cesta vazia. Nada para finalizar.")
        else:
            total_da_compra = sum(item["preco"] for item in cesta_de_compras)
            print("\nResumo da compra:")
            for item_da_cesta in cesta_de_compras:
                print(f"- {item_da_cesta['nome']} - R$ {item_da_cesta['preco']:.2f}")
            print(f"Total: R$ {total_da_compra:.2f}")
            print("Compra finalizada com sucesso!")
            cesta_de_compras = []  # esvazia a cesta após finalizar

    # sair da loja
    elif opcao_escolhida == "6":
        print("Obrigado por usar a loja virtual. Até logo!")
        programa_continuar = False

    # opção inválida
    else:
        print("Opção inválida. Tente novamente.")
