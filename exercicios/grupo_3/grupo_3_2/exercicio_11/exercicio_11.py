"""
Grupo 3.2
Exercício: 11
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Classificação de Alunos Múltipla: Peça a nota final de 4 alunos (de 0 a 100). 
    Use um loop para cada aluno e um conjunto de condicionais (SE-SENÃO SE) para classificá-los como:
        "Aprovado" (nota >= 70)
        "Recuperação" (nota >= 50 E nota < 70)
        "Reprovado" (nota < 50)"
"""

def obter_nota(aluno_numero: int) -> int:
    """Solicita e valida a nota de um aluno."""
    while True:
        try:
            nota = int(input(f"Digite a nota do aluno {aluno_numero} (0-100): "))
            if 0 <= nota <= 100:
                return nota
            print("Nota inválida! Deve estar entre 0 e 100.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


def classificar_aluno(nota: int) -> str:
    """Classifica o aluno conforme a nota."""
    if nota >= 70:
        return "Aprovado"
    elif nota >= 50:
        return "Recuperação"
    else:
        return "Reprovado"


def main():
    """Loop principal: coleta 4 notas e exibe classificação."""
    for i in range(1, 5):
        nota = obter_nota(i)
        situacao = classificar_aluno(nota)
        print(f"Aluno {i}: {situacao}")


if __name__ == "__main__":
    main()
