import random
# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: JOGO: Adivinhe o Número: O programa deve "escolher" um número aleatório entre 1 e 100 (você pode definir um número fixo para simplificar). O usuário tenta adivinhar o número. A cada tentativa, o programa informa se o palpite foi "muito alto", "muito baixo" ou "correto".
#							O jogo termina quando o usuário acerta.

def escolhe_numero_secreto():
    # Gera número aleatório entre 1 e 100
    return random.randint(1, 100)

def pede_palpite():
    # Pergunta ao usuário e valida entrada
    while True:
        try:
            palpite = int(input("Digite seu palpite (1-100): "))
            if 1 <= palpite <= 100:
                return palpite
            print("Número deve estar entre 1 e 100.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def compara_palpite(numero_secreto, palpite):
    # Compara e retorna dica
    if palpite < numero_secreto:
        return "Muito baixo!"
    elif palpite > numero_secreto:
        return "Muito alto!"
    else:
        return "Correto!"

def jogo_adivinha():
    # Função principal do jogo
    print("Bem-vindo ao Adivinhe o Número!")
    numero_secreto = escolhe_numero_secreto()
    tentativas = 0

    while True:
        palpite = pede_palpite()
        tentativas += 1
        resultado = compara_palpite(numero_secreto, palpite)
        print(resultado)

        if resultado == "Correto!":
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
            break

if __name__ == "__main__":
    jogo_adivinha()
