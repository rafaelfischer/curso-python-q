# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Desenho de Quadrado: Peça um número ao usuário e desenhe um quadrado de asteriscos (*) com esse número de linhas e colunas. Exemplo (lado 4):
#							****
#							****
#							****
#							****

def desenha_quadrado(lado: int) -> None:
    """Desenha um quadrado de asteriscos com o lado informado."""
    linha = '*' * lado  # Cria uma linha completa de asteriscos
    for _ in range(lado):  # Repete a linha 'lado' vezes
        print(linha)


def main() -> None:
    """Pede o tamanho do lado e chama a função de desenho."""
    try:
        lado = int(input("Digite o tamanho do lado do quadrado: "))
        if lado <= 0:
            print("O lado deve ser um número positivo.")
            return
        desenha_quadrado(lado)
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")


if __name__ == "__main__":
    main()
