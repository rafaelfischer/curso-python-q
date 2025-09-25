# Objetivo do programa: Acesso ao Sistema: Um sistema requer que a senha tenha no mínimo 6 caracteres. 
#                      Peça uma senha e informe se ela é "Válida" ou "Inválida".
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

print('Validação de Senha')
print('-----------------')

senha = input('Digite uma senha: ')

if len(senha) >= 6:
    print('Válida')
else:
    print('Inválida')