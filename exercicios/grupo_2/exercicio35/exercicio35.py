# Objetivo do programa: Decisão de Compra Online: Um usuário decide comprar um item online se o preço for menor que R$100
#                      OU se o frete for grátis E o estoque for maior que zero.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Decisão de Compra Online')
print('----------------------')

preco = float(input('Digite o preço do item: R$ '))
frete_gratis = input('O frete é grátis? (sim/não): ').lower()
estoque = int(input('Digite a quantidade em estoque: '))

deve_comprar = preco < 100 or (frete_gratis == 'sim' and estoque > 0)
print('Comprar' if deve_comprar else 'Não comprar')