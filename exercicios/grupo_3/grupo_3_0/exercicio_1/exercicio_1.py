# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Calcule o fatorial de um número. Pergunte o número, faça o loop e exiba o resultado no final. 
# Exemplo: Fatorial de 5 => 5 * 4 * 3 * 2 * 1 = 120

def calcular_fatorial_simples():
    # Solicita ao usuário um número inteiro
    numero_digitado = int(input("Digite um número inteiro para calcular o fatorial: "))

    # Inicializa o fatorial com 1
    fatorial_calculado = 1

    # Loop para multiplicar os números de 1 até o número digitado
    # Não inclui validações complexas para simplificar a lógica
    for i in range(1, numero_digitado + 1):
        fatorial_calculado *= i

    print(f"O fatorial de {numero_digitado} é {fatorial_calculado}")

# Chama a função para executar o programa
calcular_fatorial_simples()