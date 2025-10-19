# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Sequência de Fibonacci: Gere e imprima os primeiros N termos da sequência de Fibonacci, onde N é fornecido pelo usuário. (Ex: 0, 1, 1, 2, 3, 5, 8...)

def gerar_fibonacci(n):
    """
    Gera os primeiros N termos da sequência de Fibonacci.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    sequencia = [0, 1]
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    return sequencia


def main():
    # Solicita quantidade de termos ao usuário
    try:
        n = int(input("Quantos termos da sequência de Fibonacci deseja? "))
    except ValueError:
        print("Por favor, insira um número inteiro válido.")
        return

    # Gera e exibe a sequência
    fibonacci = gerar_fibonacci(n)
    print("Sequência de Fibonacci:")
    print(", ".join(map(str, fibonacci)))


if __name__ == "__main__":
    main()
