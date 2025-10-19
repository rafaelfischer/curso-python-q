# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: JOGO: Adivinhe o Número: O programa deve "escolher" um número aleatório entre 1 e 100 (você pode definir um número fixo para simplificar). O usuário tenta adivinhar o número. A cada tentativa, o programa informa se o palpite foi "muito alto", "muito baixo" ou "correto".
#							O jogo termina quando o usuário acerta.

# Número fixo para adivinhar (simplificado)
numero_secreto = 42

# Contador de tentativas
tentativas = 0

# Loop até acertar
while True:
    # Pede palpite ao usuário
    palpite = int(input("Digite seu palpite (1-100): "))
    tentativas += 1

    # Compara e dá dica
    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print(f"Correto! Você acertou em {tentativas} tentativas.")
        break
