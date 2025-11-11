# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Desenho de Quadrado: Peça um número ao usuário e desenhe um quadrado de asteriscos (*) com esse número de linhas e colunas. Exemplo (lado 4):
#							****
#							*  *
#							*  *
#							****


def desenhar_quadrado(lado: int) -> None:
    """Desenha um quadrado oco de asteriscos com o lado informado."""
    if lado <= 0:
        print("O lado deve ser um número positivo.")
        return

    # Linha superior cheia
    print('*' * lado)

    # Linhas do meio com apenas as bordas
    for _ in range(lado - 2):
        print('*' + ' ' * (lado - 2) + '*')

    # Linha inferior cheia (se lado > 1)
    if lado > 1:
        print('*' * lado)


def obter_lado_do_usuario() -> int:
    """Pede e valida o número inteiro positivo do usuário."""
    while True:
        try:
            valor = int(input("Digite o tamanho do lado do quadrado: "))
            if valor > 0:
                return valor
            print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    lado = obter_lado_do_usuario()
    desenhar_quadrado(lado)
