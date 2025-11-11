# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Faça um programa que some de 0 a 100 somente os números primos, e exiba o resultado. Número primo é aquele que é divisível somente por ele mesmo e pelo número 1.

soma_primos = 0
for numero in range(101):
    bln_primo = True
    if numero < 2:
        bln_primo = False

    for divisor in range(2, numero-1):
        if numero % divisor == 0:
            bln_primo = False
            break

    if bln_primo is True:
        soma_primos += numero

print(f"Soma dos números primos de 0 a 100: {soma_primos}")
