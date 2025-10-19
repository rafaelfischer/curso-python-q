# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Preço Total da Compra: Solicite ao usuário os preços de vários produtos. O programa deve parar de pedir preços quando o usuário digitar 0. Ao final, mostre o valor total da compra.

# inicia o total da compra
total = 0

# loop infinito até usuário digitar 0
while True:
    # solicita preço do produto
    preco = float(input("Digite o preço do produto (0 para encerrar): "))
    
    # verifica se é 0 para sair
    if preco == 0:
        break
    
    # adiciona ao total
    total += preco

# mostra o total final
print(f"Total da compra: R$ {total:.2f}")
