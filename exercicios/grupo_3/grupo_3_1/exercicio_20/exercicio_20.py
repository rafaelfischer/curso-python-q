# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Desenho de Triângulo Retângulo: Peça um número N ao usuário e desenhe um triângulo retângulo de asteriscos (*) com N linhas. Exemplo (N=4):
#							*
#							**
#							***
#							****

def desenha_triangulo_retangulo(altura: int) -> None:
    """
    Desenha um triângulo retângulo de asteriscos com a altura informada.
    """
    for linha in range(1, altura + 1):
        # Cada linha tem 'linha' asteriscos
        print('*' * linha)


def main() -> None:
    """
    Pede altura ao usuário e desenha o triângulo.
    """
    try:
        altura = int(input('Digite a altura do triângulo: '))
        if altura <= 0:
            print('Altura deve ser maior que zero.')
        else:
            desenha_triangulo_retangulo(altura)
    except ValueError:
        print('Entrada inválida. Digite um número inteiro.')


if __name__ == '__main__':
    main()
