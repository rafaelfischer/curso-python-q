# Objetivo do programa: Dia da Semana
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Dia da Semana')
print('------------')

numero = int(input('Digite um número entre 1 e 7: '))

dias = {
    1: 'Domingo',
    2: 'Segunda-feira',
    3: 'Terça-feira',
    4: 'Quarta-feira',
    5: 'Quinta-feira',
    6: 'Sexta-feira',
    7: 'Sábado'
}

print(dias.get(numero, 'Número inválido! Digite um número entre 1 e 7.'))