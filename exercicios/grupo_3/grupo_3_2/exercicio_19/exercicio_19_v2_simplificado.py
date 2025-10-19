# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Desenho de Quadrado: Peça um número ao usuário e desenhe um quadrado de asteriscos (*) com esse número de linhas e colunas. Exemplo (lado 4):
#							****
#							*  *
#							*  *
#							****

# Pergunta o tamanho do lado ao usuário
tamanho = int(input("Digite o tamanho do lado do quadrado: "))

# Desenha a primeira linha cheia
print("*" * tamanho)

# Desenha as linhas do meio com espaços internos
for linha in range(tamanho - 2):
    print("*" + " " * (tamanho - 2) + "*")

# Desenha a última linha cheia, se tamanho > 1
if tamanho > 1:
    print("*" * tamanho)
