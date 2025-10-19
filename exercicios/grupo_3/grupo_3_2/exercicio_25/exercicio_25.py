# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Investimento Simples (Juros Compostos): Um usuário investe um valor inicial, com uma taxa de juros anual. Peça o valor inicial, a taxa de juros (em porcentagem) e o número de anos. Calcule e exiba o montante final para cada ano.

def calcular_juros_compostos(valor_inicial, taxa_anual, anos):
    """
    Calcula o montante final para cada ano com juros compostos.
    Retorna uma lista com o valor acumulado ano a ano.
    """
    valores_por_ano = []
    montante = valor_inicial
    for ano in range(1, anos + 1):
        montante *= (1 + taxa_anual / 100)
        valores_por_ano.append(round(montante, 2))
    return valores_por_ano


def obter_entrada_float(mensagem):
    """Solicita e valida entrada numérica do usuário."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def main():
    # Entrada de dados
    valor_inicial = obter_entrada_float("Digite o valor inicial investido (R$): ")
    taxa_juros = obter_entrada_float("Digite a taxa de juros anual (%): ")
    num_anos = int(obter_entrada_float("Digite o número de anos: "))

    # Cálculo
    resultados = calcular_juros_compostos(valor_inicial, taxa_juros, num_anos)

    # Saída
    print("\nProjeção do investimento (juros compostos):")
    for ano, valor in enumerate(resultados, start=1):
        print(f"Ano {ano}: R$ {valor:,.2f}")


if __name__ == "__main__":
    main()
