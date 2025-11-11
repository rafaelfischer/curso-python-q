import random
"""
Grupo 3.2
Exercício: 14   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    JOGO: 
        Jokenpô (Pedra, Papel, Tesoura) - Melhor de 3: Simule um jogo de Jokenpô onde o usuário joga contra o "computador" (você pode pré-definir as jogadas do computador ou simular aleatoriamente). 
        Joguem 3 rodadas. 
        Use um loop e condicionais para determinar o vencedor de cada rodada e o vencedor final (quem ganhar 2 ou 3 rodadas).
"""

# placar
vitorias_usuario = 0
vitorias_computador = 0

# opções do jogo
opcoes = ["pedra", "papel", "tesoura"]

# loop para 3 rodadas
for rodada in range(1, 4):
    print(f"\nRodada {rodada}:")
    
    # entrada do usuário
    escolha_usuario = input("Escolha pedra, papel ou tesoura: ").lower()
    
    # valida entrada
    while escolha_usuario not in opcoes:
        escolha_usuario = input("Opção inválida. Tente novamente: ").lower()
    
    # escolha aleatória do computador
    escolha_computador = random.choice(opcoes)
    print(f"Computador escolheu: {escolha_computador}")
    
    # regras do jogo
    if escolha_usuario == escolha_computador:
        print("Empate!")
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        print("Você venceu esta rodada!")
        vitorias_usuario += 1
    else:
        print("Computador venceu esta rodada!")
        vitorias_computador += 1

# resultado final
print("\n--- Resultado Final ---")
print(f"Você: {vitorias_usuario} vitórias")
print(f"Computador: {vitorias_computador} vitórias")

if vitorias_usuario > vitorias_computador:
    print("Parabéns! Você ganhou o melhor de 3!")
elif vitorias_computador > vitorias_usuario:
    print("Computador venceu o melhor de 3!")
else:
    print("O jogo terminou empatado!")
