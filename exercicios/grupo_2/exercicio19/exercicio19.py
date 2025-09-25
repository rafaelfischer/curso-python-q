# Objetivo do programa: Conceito por Nota
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

def atribuir_conceito(nota):
    if 90 <= nota <= 100:
        return 'A'
    elif 80 <= nota <= 89:
        return 'B'
    elif 70 <= nota <= 79:
        return 'C'
    elif 60 <= nota <= 69:
        return 'D'
    elif 0 <= nota < 60:
        return 'F'
    else:
        return 'Nota inválida'

print('Atribuição de Conceito')
print('---------------------')

nota = int(input('Escolha um valor entre 0 e 100: '))
print(f'Conceito para nota {nota}: {atribuir_conceito(nota)}')