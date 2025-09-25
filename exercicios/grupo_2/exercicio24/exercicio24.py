# Objetivo do programa: Ano Bissexto
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Verificação de Ano Bissexto')
print('-------------------------')

ano = int(input('Digite um ano: '))

eh_bissexto = (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0)
print(f'{ano} é um ano bissexto.' if eh_bissexto else f'{ano} não é um ano bissexto.')