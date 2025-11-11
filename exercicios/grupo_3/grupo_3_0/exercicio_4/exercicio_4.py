# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que some de 0 a 100 os números pares, e exiba o resultado.

def somar_numeros_pares_simples():
    soma_dos_pares = 0
    # Itera de 0 a 100
    for numero_atual in range(101):
        # Verifica se o número é par
        if numero_atual % 2 == 0:
            soma_dos_pares += numero_atual  # Adiciona o número par à soma
    print(f"A soma dos números pares de 0 a 100 é: {soma_dos_pares}")

# Chama a função para executar o programa
somar_numeros_pares_simples()