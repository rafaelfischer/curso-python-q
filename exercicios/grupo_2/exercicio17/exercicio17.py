# Objetivo do programa: Desconto por Compra
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Cálculo de Desconto')
print('-----------------')

valor_compra = float(input('Digite o valor da compra: R$ '))
desconto = 10  # porcentagem de desconto

if valor_compra > 100.0:
    valor_desconto = valor_compra * (desconto / 100)
    print(f'Valor com desconto de {desconto}%: R$ {valor_compra - valor_desconto:.2f} - Valor do desconto: R$ {valor_desconto:.2f}')
else:
    print(f'Valor sem desconto: R$ {valor_compra:.2f}')