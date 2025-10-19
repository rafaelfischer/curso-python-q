# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Sistema de Votação Simples: Crie um sistema que permita votar em três candidatos (A, B, C). Os votos são inseridos um por um. O programa deve parar de receber votos quando o usuário digitar "fim". Ao final, exiba o total de votos para cada candidato.

def votar(candidatos: dict[str, int]) -> None:
    """Recebe votos até o usuário digitar 'fim'."""
    while True:
        voto = input("Vote em A, B ou C (ou digite 'fim' para encerrar): ").strip().upper()
        if voto == "FIM":
            break
        if voto in candidatos:
            candidatos[voto] += 1
        else:
            print("Voto inválido. Use apenas A, B ou C.")

def exibir_resultados(candidatos: dict[str, int]) -> None:
    """Exibe o total de votos de cada candidato."""
    print("\nResultado da votação:")
    for candidato, total in candidatos.items():
        print(f"Candidato {candidato}: {total} voto(s)")

def main() -> None:
    """Função principal que coordena a votação e a exibição dos resultados."""
    candidatos = {"A": 0, "B": 0, "C": 0}
    votar(candidatos)
    exibir_resultados(candidatos)

if __name__ == "__main__":
    main()
