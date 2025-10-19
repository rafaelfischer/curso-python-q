# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Contagem Regressiva Personalizada: Solicite um número inteiro ao usuário e faça uma contagem regressiva a partir desse número até 0, exibindo "FIM!" ao final.

def contagem_regressiva(inicio: int) -> None:
    # Conta de inicio até 0 e exibe "FIM!"
    for numero in range(inicio, -1, -1):
        print(numero)
    print("FIM!")


def obter_numero_do_usuario() -> int:
    # Pede número inteiro positivo ao usuário
    while True:
        try:
            valor = int(input("Digite um número inteiro positivo: "))
            if valor < 0:
                print("Por favor, digite um número não negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def main() -> None:
    # Função principal que orquestra o programa
    numero_inicial = obter_numero_do_usuario()
    contagem_regressiva(numero_inicial)


if __name__ == "__main__":
    main()
