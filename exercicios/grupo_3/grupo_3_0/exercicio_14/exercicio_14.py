# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte 5 números e calcule a média. Atenção, utilize um loop FOR.

def calcular_media_cinco_numeros():
    soma_dos_numeros = 0
    quantidade_numeros = 5
    
    print(f"Por favor, digite {quantidade_numeros} números para calcular a média.")
    
    # Loop FOR para pedir 5 números ao usuário
    for i in range(quantidade_numeros):
        try:
            numero_digitado = float(input(f"Digite o {i + 1}º número: "))
            soma_dos_numeros += numero_digitado
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")
            return # Sai da função se a entrada for inválida
            
    # Calcula a média
    media = soma_dos_numeros / quantidade_numeros
    
    print(f"A soma dos números é: {soma_dos_numeros}")
    print(f"A média dos {quantidade_numeros} números é: {media:.2f}") # Exibe a média com 2 casas decimais

# Chama a função para executar o programa
calcular_media_cinco_numeros()