"""
Grupo 3.2
Exercício: 10
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Aumento Salarial Condicional: Para 5 funcionários, peça o salário atual de cada um. 
    Use um loop para processá-los. 
    Se o salário for menor que R$1500, aplique um aumento de 15% e mostre o novo salário. 
    Caso contrário, mostre o salário original.
"""

def calcular_novo_salario(salario_atual: float) -> float:
    """Aplica 15% de aumento se salário < R$1500."""
    if salario_atual < 1500:
        return salario_atual * 1.15
    return salario_atual


def obter_salario_do_funcionario(indice: int) -> float:
    """Solicita e valida o salário do funcionário."""
    while True:
        try:
            salario = float(input(f"Digite o salário do {indice}º funcionário: R$"))
            if salario < 0:
                print("Salário não pode ser negativo. Tente novamente.")
                continue
            return salario
        except ValueError:
            print("Valor inválido. Digite apenas números.")


def main():
    """Processa 5 funcionários e exibe resultado do reajuste."""
    TOTAL_FUNCIONARIOS = 5
    LIMITE_SALARIO = 1500
    PERCENTUAL_AUMENTO = 15

    for i in range(1, TOTAL_FUNCIONARIOS + 1):
        salario = obter_salario_do_funcionario(i)
        novo_salario = calcular_novo_salario(salario)

        if salario < LIMITE_SALARIO:
            print(
                f"Funcionário {i}: salário reajustado de R${salario:.2f} "
                f"para R${novo_salario:.2f} ({PERCENTUAL_AUMENTO}% de aumento)."
            )
        else:
            print(f"Funcionário {i}: salário mantido em R${salario:.2f}.")


if __name__ == "__main__":
    main()
