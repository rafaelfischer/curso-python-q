# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Menu de Opções: Crie um menu simples que exiba as opções "1. Iniciar", "2. Configurar", "3. Sair". O programa deve continuar exibindo o menu até que o usuário escolha a opção "3".

def exibir_menu():
    """Mostra as opções disponíveis para o usuário."""
    print("\n=== MENU ===")
    print("1. Iniciar")
    print("2. Configurar")
    print("3. Sair")


def obter_opcao():
    """Solicita e valida a escolha do usuário."""
    while True:
        try:
            opcao = int(input("Escolha uma opção: "))
            if 1 <= opcao <= 3:
                return opcao
            print("Opção inválida. Digite 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Digite um número.")


def processar_opcao(opcao):
    """Executa a ação correspondente à opção escolhida."""
    if opcao == 1:
        print("Iniciando o sistema...")
    elif opcao == 2:
        print("Abrindo configurações...")
    elif opcao == 3:
        print("Encerrando...")


def main():
    """Loop principal do programa."""
    while True:
        exibir_menu()
        escolha = obter_opcao()
        processar_opcao(escolha)
        if escolha == 3:
            break


if __name__ == "__main__":
    main()
