# Objetivo do programa: Faixa Etária Simples
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Classificação por Idade')
print('---------------------')

idade = int(input('Digite a idade: '))

if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
else:
    print('Adulto')