# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Maior e Menor Número: Peça ao usuário para digitar uma sequência de números. O programa deve parar quando o usuário digitar 0. Ao final, exiba qual foi o maior e qual foi o menor número digitado (excluindo o 0).

def obter_numero_inteiro(mensagem: str) -> int:
    """Pede um número inteiro ao usuário até ele digitar algo válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Por favor, digite apenas números inteiros.")


def main():
    # Inicializa variáveis para guardar maior e menor
    maior = None
    menor = None

    print("Digite números inteiros. Digite 0 para encerrar.")

    while True:
        numero = obter_numero_inteiro("Número: ")

        # Sai do loop quando o usuário digitar 0
        if numero == 0:
            break

        # Atualiza maior e menor na primeira entrada ou quando necessário
        if maior is None or numero > maior:
            maior = numero
        if menor is None or numero < menor:
            menor = numero

    # Exibe resultados apenas se o usuário tiver digitado algo
    if maior is not None:
        print(f"Maior número digitado: {maior}")
        print(f"Menor número digitado: {menor}")
    else:
        print("Nenhum número foi digitado.")


if __name__ == "__main__":
    main()
