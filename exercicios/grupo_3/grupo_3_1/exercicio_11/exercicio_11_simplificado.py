"""
Grupo 3.2
Exercício: 11
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Classificação de Alunos Múltipla: Peça a nota final de 4 alunos (de 0 a 100). 
    Use um loop para cada aluno e um conjunto de condicionais (SE-SENÃO SE) para classificá-los como:
        "Aprovado" (nota >= 70)
        "Recuperação" (nota >= 50 E nota < 70)
        "Reprovado" (nota < 50)"
"""

# loop para 4 alunos
for aluno in range(1, 5):
    # pede a nota
    nota = float(input(f"Digite a nota do aluno {aluno} (0-100): "))
    
    # classifica
    if nota >= 70:
        situacao = "Aprovado"
    elif nota >= 50:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
    
    # mostra resultado
    print(f"Aluno {aluno}: {situacao}")
