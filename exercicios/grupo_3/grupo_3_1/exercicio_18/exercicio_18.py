"""
Grupo 3.1
Exercício: 18
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Sequência de Fibonacci: Gere e imprima os primeiros N termos da sequência de Fibonacci, onde N é fornecido pelo usuário. (Ex: 0, 1, 1, 2, 3, 5, 8...)
"""

def gerar_fibonacci(n):
    """Gera os primeiros N termos da sequência de Fibonacci."""
    if n <= 0:
        return []

    # Inicializa a lista com os dois primeiros termos
    sequencia = [0, 1]

    # Caso o usuário queira apenas 1 termo
    if n == 1:
        return [0]

    # Gera os próximos termos até atingir N
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)

    return sequencia[:n]

def main():
    """Função principal para interagir com o usuário."""
    try:
        # Solicita o número de termos ao usuário
        n = int(input("Digite quantos termos da sequência de Fibonacci deseja exibir: "))

        # Validação simples
        if n <= 0:
            print("Por favor, insira um número positivo.")
            return

        # Gera a sequência
        fibonacci = gerar_fibonacci(n)

        # Exibe o resultado
        print("Sequência de Fibonacci:")
        print(", ".join(map(str, fibonacci)))

    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Executa o programa
if __name__ == "__main__":
    main()
