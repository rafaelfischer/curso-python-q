# Objetivo do programa: Pergunte um número de 1 a 7. Diga a qual dia da semana esse número é correspondente
# (1 = Domingo, 2 = Segunda, ..., 7 = Sábado). Atenção, utilize a estrutura match/case.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Dia da Semana')
print('------------')

numero = int(input('Digite um número (1-7): '))

match numero:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Número inválido')