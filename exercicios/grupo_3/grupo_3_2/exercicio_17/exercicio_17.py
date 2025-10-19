# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Verificador de Número Primo: Solicite um número inteiro ao usuário e verifique se ele é um número primo (ou seja, divisível apenas por 1 e por ele mesmo).

def eh_primo(numero: int) -> bool:
    """Verifica se um número é primo."""
    if numero < 2:                 # Números menores que 2 não são primos
        return False
    if numero == 2:                # 2 é o único par primo
        return True
    if numero % 2 == 0:            # Elimina pares maiores que 2
        return False

    # Testa divisores ímpares até a raiz quadrada
    for divisor in range(3, int(numero ** 0.5) + 1, 2):
        if numero % divisor == 0:
            return False
    return True


def obter_numero_do_usuario() -> int:
    """Solicita e valida entrada do usuário."""
    while True:
        try:
            return int(input("Digite um número inteiro: "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")


def main():
    """Função principal do programa."""
    numero = obter_numero_do_usuario()

    if eh_primo(numero):
        print(f"{numero} é um número primo.")
    else:
        print(f"{numero} não é um número primo.")


if __name__ == "__main__":
    main()
