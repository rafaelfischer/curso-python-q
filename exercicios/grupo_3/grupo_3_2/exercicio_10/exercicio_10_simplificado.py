# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Menu de Opções: Crie um menu simples que exiba as opções "1. Iniciar", "2. Configurar", "3. Sair". O programa deve continuar exibindo o menu até que o usuário escolha a opção "3".

# loop infinito até o usuário pedir para sair
while True:
    # mostra as opções do menu
    print("\n1. Iniciar")
    print("2. Configurar")
    print("3. Sair")

    # lê a escolha do usuário
    opcao = input("Escolha uma opção: ")

    # decide o que fazer
    if opcao == "1":
        print("Iniciando...")
    elif opcao == "2":
        print("Abrindo configurações...")
    elif opcao == "3":
        print("Saindo...")
        break  # encerra o loop
    else:
        print("Opção inválida, tente novamente.")
