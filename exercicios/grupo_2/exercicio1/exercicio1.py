# Objetivo do programa: Pergunte um número. Diga se este numero é par ou ímpar, escrevendo na tela.
# Data da criacao: 2025-08-28
# Criado por: @programacaomentoria
# Ultima atualizacao: 2025-09-16
# Alterado por: @rafaelfischer

print('Par ou Impar')
print('-----------------------')

numero = int(input('Digite um numero: '))

if numero % 2 == 0:
	print('O numero', numero, 'eh par.')
else:
	print('O numero', numero, 'eh impar.')
