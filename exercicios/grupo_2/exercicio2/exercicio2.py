#	Pergunte um número. Diga se este numero é primo ou não, escrevendo na tela.
#	Data da criacao: 2025-08-28
#	Criado por: @programacaomentoria
#	Ultima atualizacao: 2025-09-16
#	Alterado por: @rafaelfischer

print('Eh um numero primo?')
print('-----------------------')

numero = int(input("Digite um numero: "))

# Por 2: Se o número for par (termina em 0, 2, 4, 6 ou 8), ele não é primo.
# Por 3: Se a soma dos algarismos do número for divisível por 3, o número também é divisível por 3 e não é primo.
# Por 5: Se o número terminar em 0 ou 5, ele não é primo.
if (numero == 0):
	primo = False
elif (numero % 2 == 0) and (numero != 2):
	primo = False
elif (numero % 3 == 0) and (numero != 3):
	primo = False
elif (numero % 5 == 0) and (numero != 5):
	primo = False
else:
	primo = True



print('O numero', numero, 'eh primo?: ')
if (primo is True):
	print('Sim')
else:
	print('Nao')