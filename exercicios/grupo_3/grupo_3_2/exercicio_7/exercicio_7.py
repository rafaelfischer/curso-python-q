# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Validação de Senha Simples: Peça ao usuário para digitar uma senha. Continue pedindo a senha até que ele digite "secreta123".

# Função que solicita a senha correta ao usuário
def solicitar_senha():
    senha_correta = "secreta123"
    while True:
        # Pede a senha e remove espaços extras
        senha_digitada = input("Digite a senha: ").strip()
        # Verifica se acertou
        if senha_digitada == senha_correta:
            print("Acesso liberado!")
            break
        # Senha errada: avisa e repete
        print("Senha incorreta. Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    solicitar_senha()
