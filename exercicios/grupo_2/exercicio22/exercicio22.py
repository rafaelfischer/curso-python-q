# Objetivo do programa: Login com Credenciais: Crie um algoritmo que verifique se um nome de usuário (ex: "admin") 
#                      E uma senha (ex: "1234") estão corretos para conceder acesso.
# Data da criacao: 2025-09-25
# Criado por: @rafaelfischer

ADMIN_USUARIO = "admin"
ADMIN_SENHA = "1234"

print('Sistema de Login')
print('---------------')

usuario = input('Digite o usuário: ')
senha = input('Digite a senha: ')

if usuario == ADMIN_USUARIO and senha == ADMIN_SENHA:
    print('Acesso concedido!')
else:
    print('Acesso negado!')