# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Tabuada de um Número: Peça ao usuário para digitar um número inteiro e, em seguida, imprima a tabuada desse número (de 1 a 10).

# pede número ao usuário
numero = int(input("Digite um número inteiro: "))

# loop de 1 a 10
for i in range(1, 11):
    # exibe a tabuada
    print(f"{numero} x {i} = {numero * i}")
