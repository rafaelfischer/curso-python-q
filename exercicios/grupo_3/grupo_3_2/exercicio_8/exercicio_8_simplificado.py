# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Contagem Regressiva Personalizada: Solicite um número inteiro ao usuário e faça uma contagem regressiva a partir desse número até 0, exibindo "FIM!" ao final.

# Pede número ao usuário
numero = int(input("Digite um número inteiro: "))

# Conta de número até 0
while numero >= 0:
    print(numero)
    numero -= 1

# Exibe fim
print("FIM!")
