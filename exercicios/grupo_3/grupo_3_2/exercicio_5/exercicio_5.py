# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Tabuada de um Número: Peça ao usuário para digitar um número inteiro e, em seguida, imprima a tabuada desse número (de 1 a 10).

def obter_numero_inteiro() -> int:
    """Pede ao usuário um número inteiro e retorna o valor."""
    while True:
        try:
            numero = int(input("Digite um número inteiro: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def imprimir_tabuada(numero: int) -> None:
    """Imprime a tabuada do número informado de 1 a 10."""
    for multiplicador in range(1, 11):
        resultado = numero * multiplicador
        print(f"{numero} x {multiplicador} = {resultado}")


def main() -> None:
    """Função principal que coordena a execução do programa."""
    numero_usuario = obter_numero_inteiro()
    imprimir_tabuada(numero_usuario)


if __name__ == "__main__":
    main()
