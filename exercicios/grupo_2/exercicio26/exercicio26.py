# Objetivo do programa: Verificar Vogal
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Verificação de Vogal')
print('------------------')

letra = input('Digite um caractere: ').lower()

eh_vogal = letra in 'aeiou'

print('O caractere é uma vogal' if eh_vogal else 'O caractere não é uma vogal')