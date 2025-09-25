# Objetivo do programa: Sinal do Número: Desenvolva um algoritmo que solicite um número
# e diga se ele é positivo, negativo ou zero.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Sinal do Número')
print('--------------')

numero = float(input('Digite um número: '))

if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
else:
    print('O número é zero')