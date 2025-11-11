"""
Grupo 3.2
Exercício: 9   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Tentativas de Senha Limitadas: A senha correta é "topsecret". 
    Peça ao usuário para digitar a senha. 
    Ele tem 3 tentativas. 
    Use um loop e condicionais para informar se ele acertou ou se esgotou as tentativas. 
"""

# Define a senha correta
senha_correta = "topsecret"

# Inicializa o contador de tentativas
tentativa = 0
max_tentativas = 3

# Loop enquanto ainda houver tentativas
while tentativa < max_tentativas:
    # Pede a senha ao usuário
    senha_digitada = input("Digite a senha: ")
    
    # Verifica se acertou
    if senha_digitada == senha_correta:
        print("Senha correta! Acesso liberado.")
        break  # Sai do loop se acertou
    
    # Se errou, incrementa tentativa
    tentativa += 1
    
    # Avisa quantas tentativas restam
    if tentativa < max_tentativas:
        print(f"Senha incorreta. Você ainda tem {max_tentativas - tentativa} tentativa(s).")
    else:
        print("Senha incorreta. Suas tentativas acabaram. Acesso negado.")
