# Objetivo do programa: Perguntar o nome de um aluno, pergunte as 4 notas e calcule a média aritmética, exibindo no final.
# Data da criacao: 2025-08-28
# Criado por: @programacaomentoria
# Ultima atualizacao: 2025-09-16
# Alterado por: @rafaelfischer

print('Exercicio 3 - Calculo de media aritmetica')
print('-----------------------------------------')
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4
print('A media do aluno', nome, 'e:', '{:.2f}'.format(media))