# Objetivo do programa: Cálculo de Bônus: Um funcionário recebe bônus se atingir uma meta de vendas (vendas >= 10000)
#                      OU se tiver mais de 5 anos de empresa. Se ambas as condições forem verdadeiras, o bônus é dobrado.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Cálculo de Bônus')
print('---------------')

vendas = float(input('Digite o valor das vendas: '))
anos_empresa = int(input('Digite os anos de empresa: '))

bonus = 500.0
meta_vendas = vendas >= 10000
tempo_empresa = anos_empresa > 5

if meta_vendas and tempo_empresa:
    bonus *= 2
else:
    bonus = 0

print(f'O bônus do funcionário é R$ {bonus:.2f}')