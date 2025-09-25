# Objetivo do programa: Pergunte o valor de uma compra. Se for maior que R$ 100, aplique 10% de desconto.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Cálculo de Desconto')
print('------------------')

valor = float(input('Digite o valor da compra: R$ '))
total_desconto = 10

if valor > 100:
    desconto = valor * (total_desconto / 100)
    print(f'Valor com desconto de {total_desconto}%: R$ {valor - desconto:.2f} - Valor do desconto: R$ {desconto:.2f}')
else:
    print(f'Valor sem desconto: R$ {valor:.2f}')