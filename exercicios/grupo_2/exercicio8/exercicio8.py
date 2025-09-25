# Objetivo do programa: Pergunte a nota de um aluno (de 0 a 10). Diga se o aluno está reprovado (nota < 5),
# em recuperação (nota entre 5 e 6.9) ou aprovado (nota ≥ 7)
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Situação do Aluno')
print('----------------')

nota = float(input('Digite a nota do aluno (0 a 10): '))

if nota < 5:
    print('Aluno reprovado')
elif nota < 7:
    print('Aluno em recuperação')
else:
    print('Aluno aprovado')