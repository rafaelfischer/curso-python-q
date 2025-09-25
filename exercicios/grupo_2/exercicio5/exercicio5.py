# Objetivo do programa: Pergunte um número. Diga se esse número é positivo, negativo ou zero.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Número Positivo ou Negativo')
print('---------------------------')

numero = float(input('Digite um número: '))

if numero > 0:
    print('O número é positivo')
elif numero < 0:
    print('O número é negativo')
else:
    print('O número é zero')