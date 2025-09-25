# Objetivo do programa: Pergunte uma letra (V, A, B). Diga a cor correspondente (Vermelho, Azul, Branco).
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Letras e Cores')
print('-------------')

letra = input('Digite uma letra (V, A ou B): ').upper()

match letra:
    case 'V':
        print('Vermelho')
    case 'A':
        print('Azul')
    case 'B':
        print('Branco')
    case _:
        print('Letra inválida')