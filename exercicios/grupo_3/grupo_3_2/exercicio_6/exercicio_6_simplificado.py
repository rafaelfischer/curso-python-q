# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Soma de Números até um Limite: Crie um programa que peça números ao usuário repetidamente até que a soma dos números digitados seja maior que 50. Ao final, imprima a soma total.

# Inicializa a soma
soma = 0

# Continua pedindo números até a soma ultrapassar 50
while soma <= 50:
    # Pede um número ao usuário
    numero = int(input("Digite um número: "))
    # Adiciona o número à soma
    soma += numero

# Mostra o resultado final
print("Soma total:", soma)
