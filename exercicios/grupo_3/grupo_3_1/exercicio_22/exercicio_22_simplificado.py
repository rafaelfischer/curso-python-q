# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Sistema de Votação Simples: Crie um sistema que permita votar em três candidatos (A, B, C). Os votos são inseridos um por um. O programa deve parar de receber votos quando o usuário digitar "fim". Ao final, exiba o total de votos para cada candidato.

# inicia contadores
votos_candidato_a = 0
votos_candidato_b = 0
votos_candidato_c = 0

# loop para receber votos
while True:
    voto = input("Vote em A, B ou C (digite 'fim' para encerrar): ").strip().upper()
    
    # verifica se o usuário quer parar
    if voto == "FIM":
        break
    
    # registra o voto ou avisa se for inválido
    if voto == "A":
        votos_candidato_a += 1
    elif voto == "B":
        votos_candidato_b += 1
    elif voto == "C":
        votos_candidato_c += 1
    else:
        print("Voto inválido. Tente novamente.")

# exibe o resultado
print("\nResultado da votação:")
print(f"Candidato A: {votos_candidato_a} votos")
print(f"Candidato B: {votos_candidato_b} votos")
print(f"Candidato C: {votos_candidato_c} votos")
