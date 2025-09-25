# Objetivo do programa: Preço de Passagem Aérea: O preço depende da classe e promoção
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Cálculo de Passagem Aérea')
print('------------------------')

classe = input('Digite a classe (economica/executiva): ').lower()
promocao = input('Há promoção? (sim/nao): ').lower()

preco = 0
if classe == 'economica':
    preco = 300 if promocao == 'sim' else 500
elif classe == 'executiva':
    preco = 1000 if promocao == 'sim' else 1500

print(f'O preço da passagem é R$ {preco:.2f}')