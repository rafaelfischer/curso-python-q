# Objetivo do programa: Maior de Dois Números
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Comparação de Números')
print('-------------------')

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

if num1 > num2:
    print(f'{num1} é maior que {num2}')
elif num2 > num1:
    print(f'{num2} é maior que {num1}')
else:
    print('Os números são iguais')