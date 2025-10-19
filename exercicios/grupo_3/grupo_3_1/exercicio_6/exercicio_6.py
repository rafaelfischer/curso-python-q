# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que pergunte um número. Exiba os números de 0 até o número digitado, separados por um espaço, exibindo o resultado.

def exibir_numeros_ate_o_digitado():
    try:
        numero_limite = int(input("Por favor, digite um número inteiro: "))
        
        if numero_limite < 0:
            print("Por favor, digite um número não negativo.")
            return

        numeros_exibidos = []
        # Itera de 0 até o número digitado (inclusive)
        for numero_atual in range(numero_limite + 1):
            numeros_exibidos.append(str(numero_atual)) # Adiciona o número à lista como string
        
        # Exibe os números encontrados separados por espaço
        print(f"Números de 0 até {numero_limite}:", " ".join(numeros_exibidos))

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Chama a função para executar o programa
exibir_numeros_ate_o_digitado()