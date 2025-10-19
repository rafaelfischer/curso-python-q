# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Contador Crescente: Crie um algoritmo que imprima na tela todos os números inteiros de 1 a 100.

def contar_crescente(inicio: int, fim: int) -> None:
    """Imprime números inteiros de 'inicio' até 'fim'."""
    for numero in range(inicio, fim + 1):
        print(numero)


if __name__ == "__main__":
    # Define os limites do contador
    limite_inicial = 1
    limite_final = 100

    # Executa a função
    contar_crescente(limite_inicial, limite_final)
