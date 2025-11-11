# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Localizador de Divisores: Peça um número inteiro ao usuário e liste todos os seus divisores.


def obter_numero_inteiro() -> int:
    """Solicita ao usuário um número inteiro positivo."""
    while True:
        try:
            numero = int(input("Digite um número inteiro positivo: "))
            if numero <= 0:
                print("Por favor, insira um número maior que zero.")
                continue
            return numero
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def listar_divisores(numero: int) -> list[int]:
    """Retorna lista com todos os divisores positivos do número."""
    divisores = []
    for candidato in range(1, numero + 1):
        if numero % candidato == 0:
            divisores.append(candidato)
    return divisores


def exibir_divisores(divisores: list[int]) -> None:
    """Exibe os divisores de forma clara."""
    print("Divisores encontrados:", ", ".join(map(str, divisores)))


def main() -> None:
    """Função principal que orquestra o programa."""
    numero = obter_numero_inteiro()
    divisores = listar_divisores(numero)
    exibir_divisores(divisores)


if __name__ == "__main__":
    main()
