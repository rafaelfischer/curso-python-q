# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte quantos alunos há na turma. Para cada aluno, pergunte a nota e calcule a média da turma. Atenção, utilize um loop FOR.

# Pergunta quantidade de alunos
total_alunos = int(input("Quantos alunos há na turma? "))

# Soma das notas começa em 0
soma_notas = 0

# Loop para pedir a nota de cada aluno
for i in range(1, total_alunos + 1):
    nota = float(input(f"Nota do aluno {i}: "))
    soma_notas += nota

# Calcula média
media = soma_notas / total_alunos

# Mostra resultado
print(f"Média da turma: {media:.2f}")
