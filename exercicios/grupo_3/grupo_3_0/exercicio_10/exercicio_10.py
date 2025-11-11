# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Imprima os múltiplos de 3 entre 1 e 30. Atenção, utilize um loop WHILE.

def imprimir_multiplos_de_tres():
    print("Múltiplos de 3 entre 1 e 30:")
    numero_atual = 1
    multiplos_encontrados = []
    # Loop WHILE para iterar de 1 a 30
    while numero_atual <= 30:
        # Verifica se o número é múltiplo de 3
        if numero_atual % 3 == 0:
            multiplos_encontrados.append(str(numero_atual)) # Adiciona o múltiplo à lista como string
        numero_atual += 1 # Incrementa o número para a próxima iteração
    
    # Exibe os múltiplos encontrados separados por espaço
    print(" ".join(multiplos_encontrados))

# Chama a função para executar o programa
imprimir_multiplos_de_tres()