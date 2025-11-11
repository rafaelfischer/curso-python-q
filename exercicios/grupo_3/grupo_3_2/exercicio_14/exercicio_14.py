import random
"""
Grupo 3.2
Exercício: 14   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    JOGO: 
        Jokenpô (Pedra, Papel, Tesoura) - Melhor de 3: Simule um jogo de Jokenpô onde o usuário joga contra o "computador" (você pode pré-definir as jogadas do computador ou simular aleatoriamente). 
        Joguem 3 rodadas. 
        Use um loop e condicionais para determinar o vencedor de cada rodada e o vencedor final (quem ganhar 2 ou 3 rodadas).
"""

def exibir_regras():
    """Exibe as regras do Jokenpô."""
    print("\nRegras do Jokenpô:")
    print("1 - Pedra vence Tesoura")
    print("2 - Tesoura vence Papel")
    print("3 - Papel vence Pedra")
    print("4 - Mesma jogada resulta em empate\n")

def obter_jogada_usuario():
    """Solicita e valida a jogada do usuário."""
    while True:
        jogada = input("Escolha: 1-Pedra, 2-Papel, 3-Tesoura: ").strip()
        if jogada in {"1", "2", "3"}:
            return int(jogada)
        print("Opção inválida. Tente novamente.")

def obter_jogada_computador():
    """Sorteia a jogada do computador."""
    return random.randint(1, 3)

def determinar_vencedor(jogador, computador):
    """Retorna quem venceu a rodada: 'empate', 'jogador' ou 'computador'."""
    if jogador == computador:
        return "empate"
    # Pedra(1) ganha de Tesoura(3), Tesoura(3) ganha de Papel(2), Papel(2) ganha de Pedra(1)
    if (jogador == 1 and computador == 3) or \
       (jogador == 3 and computador == 2) or \
       (jogador == 2 and computador == 1):
        return "jogador"
    return "computador"

def nome_jogada(codigo):
    """Converte código numérico em nome da jogada."""
    nomes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
    return nomes[codigo]

def jokenpo():
    """Executa melhor de 3 no Jokenpô."""
    exibir_regras()
    placar_jogador = 0
    placar_computador = 0
    rodada = 1

    # Loop até alguém vencer 2 rodadas
    while placar_jogador < 2 and placar_computador < 2:
        print(f"\n--- Rodada {rodada} ---")
        jogada_usuario = obter_jogada_usuario()
        jogada_pc = obter_jogada_computador()

        print(f"Você jogou: {nome_jogada(jogada_usuario)}")
        print(f"Computador jogou: {nome_jogada(jogada_pc)}")

        resultado = determinar_vencedor(jogada_usuario, jogada_pc)

        if resultado == "empate":
            print("Empate nesta rodada!")
        elif resultado == "jogador":
            print("Você venceu esta rodada!")
            placar_jogador += 1
        else:
            print("Computador venceu esta rodada!")
            placar_computador += 1

        print(f"Placar: Jogador {placar_jogador} x {placar_computador} Computador")
        rodada += 1

    # Resultado final
    if placar_jogador > placar_computador:
        print("\nParabéns! Você venceu o melhor de 3!")
    else:
        print("\nComputador venceu o melhor de 3. Tente novamente!")

if __name__ == "__main__":
    jokenpo()
