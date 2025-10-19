# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Cálculo de Fatorial: Peça um número N ao usuário e calcule o seu fatorial (N! = N * (N-1) * ... * 1).


def calcular_fatorial(numero: int) -> int:
    """
    Calcula o fatorial de um número inteiro positivo.
    """
    if numero < 0:
        raise ValueError("O número deve ser não negativo.")
    if numero in (0, 1):
        return 1

    resultado = 1
    for i in range(2, numero + 1):
        resultado *= i
    return resultado


def obter_entrada_usuario() -> int:
    """
    Solicita um número inteiro ao usuário e valida a entrada.
    """
    while True:
        try:
            entrada = int(input("Digite um número inteiro não negativo: "))
            if entrada < 0:
                print("Por favor, insira um número não negativo.")
                continue
            return entrada
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def main():
    """
    Função principal que coordena a execução do programa.
    """
    numero_usuario = obter_entrada_usuario()
    fatorial = calcular_fatorial(numero_usuario)
    print(f"O fatorial de {numero_usuario} é {fatorial}.")


if __name__ == "__main__":
    main()
