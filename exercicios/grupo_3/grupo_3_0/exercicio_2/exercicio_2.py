# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que some de 0 a 100 somente os números primos, e exiba o resultado. Número primo é aquele que é divisível somente por ele mesmo e pelo número 1.

def eh_primo_simples(numero):
    # Números menores que 2 não são primos
    if numero < 2:
        return False
    # Verifica divisibilidade de 2 até o número - 1
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

def somar_primos_ate_cem_simples():
    soma_total_primos = 0
    # Itera de 0 a 100
    for numero_atual in range(101):
        # Se o número for primo, adiciona à soma
        if eh_primo_simples(numero_atual):
            soma_total_primos += numero_atual
    print(f"A soma dos números primos de 0 a 100 é: {soma_total_primos}")

# Chama a função para executar o programa
somar_primos_ate_cem_simples()