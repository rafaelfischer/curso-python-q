# Objetivo do programa: Exclusão de Desconto
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Verificação de Desconto')
print('---------------------')

categoria = input('Digite a categoria do produto: ')
valor = float(input('Digite o valor do produto: '))

aplica_desconto = not (categoria.lower() == 'eletronicos' and valor < 500)

if aplica_desconto:
    print('O desconto de 15% será aplicado.')
else:
    print('O desconto não será aplicado.')