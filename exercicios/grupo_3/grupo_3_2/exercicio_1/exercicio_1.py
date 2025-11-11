"""
Grupo 3.2
Exercício: 1
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
	Imprimir Números Pares em Intervalo: Crie um algoritmo que use um loop para percorrer os números de 1 a 20 e imprima apenas os números pares.
"""
def imprimir_pares(inicio: int, fim: int) -> None:
    """Imprime números pares no intervalo [inicio, fim]."""
    for numero in range(inicio, fim + 1):
        if numero % 2 == 0:  # Verifica se é par
            print(numero)


if __name__ == "__main__":
    # Define o intervalo desejado
    inicio_intervalo = 1
    fim_intervalo = 20
    imprimir_pares(inicio_intervalo, fim_intervalo)
