# Objetivo do programa: Calcule a área de um círculo com base no raio informado.
# Como calcular: A = PI . R ao quadrado
# Data da criacao: 2025-08-28
# Criado por: @programacaomentoria
# Ultima atualizacao: 2025-09-16
# Alterado por: @rafaelfischer

pi = 3.14159

print('Exercicio 6 - Calculo da area de um circulo')
print('------------------------------------------')

raio = float(input('Informe o valor do raio: '))

area = pi * (raio ** 2)
print(f'A area do circulo de raio {raio:.2f} e: {area:.2f}')