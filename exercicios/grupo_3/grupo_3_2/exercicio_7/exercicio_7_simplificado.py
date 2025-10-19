# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Validação de Senha Simples: Peça ao usuário para digitar uma senha. Continue pedindo a senha até que ele digite "secreta123".

# Constant for the correct password
SENHA_CORRETA = "secreta123"

# Ask for the password until the correct one is provided
senha_digitada = ""
while senha_digitada != SENHA_CORRETA:
    senha_digitada = input("Digite a senha: ")
    if senha_digitada != SENHA_CORRETA:
        print("Senha incorreta. Tente novamente.")

print("Acesso liberado!")
