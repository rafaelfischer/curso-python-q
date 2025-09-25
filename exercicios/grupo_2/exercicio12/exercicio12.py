# Objetivo do programa: Verificar Idade para Votar
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Verificação de Idade para Votação')
print('-------------------------------')

idade = int(input('Digite a idade: '))

print('Você já pode votar!' if idade >= 16 else 'Você ainda não pode votar.')