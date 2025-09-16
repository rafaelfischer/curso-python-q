#	Pergunte um número. Diga se este numero faz parte da tabuada do 3, escrevendo na tela.
#	Data da criacao: 2025-08-28
#	Criado por: @programacaomentoria
#	Ultima atualizacao: 2025-09-16
#	Alterado por: @rafaelfischer

print('Exercicio 3 - Tabuada do 3')
print('-----------------------')

numero = int(input('Digite um numero: '))

if (numero % 3 == 0):
	print('O numero', numero, 'faz parte da tabuada do 3')
else:
	print('O numero', numero, 'nao faz parte da tabuada do 3')
