# Objetivo do programa: Pergunte o número do mês (1 a 12). Diga quantos dias ele tem (ano não bissexto).
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Dias do Mês')
print('-----------')

mes = int(input('Digite o número do mês (1-12): '))

match mes:
    case 2:
        dias = 28
    case 4 | 6 | 9 | 11:
        dias = 30
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        dias = 31
    case _:
        print('Mês inválido!')
        exit()

print(f'O mês {mes} tem {dias} dias.')