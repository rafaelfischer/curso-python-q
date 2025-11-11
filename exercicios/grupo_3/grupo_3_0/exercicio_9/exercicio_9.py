# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que exiba de 0 a 100, somente os números pares, e exiba o resultado.

def exibir_numeros_pares_de_zero_a_cem():
    numeros_pares = []
    # Itera de 0 a 100
    for numero_atual in range(101):
        # Verifica se o número é par
        if numero_atual % 2 == 0:
            numeros_pares.append(str(numero_atual)) # Adiciona o número par à lista como string
    
    # Exibe os números pares encontrados separados por espaço
    print("Números pares de 0 a 100:", " ".join(numeros_pares))

# Chama a função para executar o programa
exibir_numeros_pares_de_zero_a_cem()