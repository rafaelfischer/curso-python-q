# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Desenho de Quadrado: Peça um número ao usuário e desenhe um quadrado de asteriscos (*) com esse número de linhas e colunas. Exemplo (lado 4):
#							****
#							****
#							****
#							****

# pede tamanho do lado ao usuário
tamanho = int(input("Digite o tamanho do lado do quadrado: "))

# desenha cada linha do quadrado
for linha in range(tamanho):
    # imprime uma linha com asteriscos
    print("*" * tamanho)
