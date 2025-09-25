# Objetivo do programa: Condição de Crédito
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Análise de Crédito')
print('-----------------')

renda = float(input('Digite sua renda mensal: R$ '))
historico = input('Digite seu histórico de crédito (Bom / Ruim): ').lower()

credito_aprovado = renda > 2000 or historico == 'bom'
print('Crédito Aprovado' if credito_aprovado else 'Crédito Negado')