# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Desenho de Triângulo Retângulo: Peça um número N ao usuário e desenhe um triângulo retângulo de asteriscos (*) com N linhas. Exemplo (N=4):
#							*
#							**
#							***
#							****

# pede número ao usuário
n = int(input("Digite N: "))

# desenha triângulo linha por linha
for linha in range(1, n + 1):
    print("*" * linha)
