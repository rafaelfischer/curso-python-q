# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que exiba de 0 a 100, somente os números ímpares e não divísiveis por 5, e exiba o resultado.

def exibir_impares_nao_divisiveis_por_cinco_simples():
    numeros_encontrados = []
    # Itera de 0 a 100
    for numero_atual in range(101):
        # Verifica se o número é ímpar e não é divisível por 5
        if numero_atual % 2 != 0 and numero_atual % 5 != 0:
            numeros_encontrados.append(str(numero_atual)) # Adiciona o número à lista como string
    
    # Exibe os números encontrados separados por espaço
    print("Números ímpares e não divisíveis por 5 (de 0 a 100):", " ".join(numeros_encontrados))

# Chama a função para executar o programa
exibir_impares_nao_divisiveis_por_cinco_simples()