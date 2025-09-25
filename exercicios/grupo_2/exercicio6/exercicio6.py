# Objetivo do programa: Pergunte a idade de uma pessoa. Diga se essa pessoa é uma criança (até 12 anos),
# um adolescente (13 a 17 anos), uma adulta (18 a 59 anos) ou idosa (60 anos ou mais)
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Classificação por Idade')
print('----------------------')

idade = int(input('Digite a idade: '))

if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('Idoso')