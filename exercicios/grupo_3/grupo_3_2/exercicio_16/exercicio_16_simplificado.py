# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Cálculo de Fatorial: Peça um número N ao usuário e calcule o seu fatorial (N! = N * (N-1) * ... * 1).


# pede número ao usuário
numero = int(input("Digite um número inteiro positivo: "))

# inicia resultado em 1 (neutro da multiplicação)
fatorial = 1

# multiplica de 1 até o número escolhido
for contador in range(1, numero + 1):
    fatorial *= contador

# mostra o resultado
print(f"O fatorial de {numero} é {fatorial}")
