"""
Grupo 3.2
Exercício: 3   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Números Pares: Escreva um algoritmo que imprima apenas os números pares de 2 a 20.
"""
def imprimir_pares(inicio: int = 2, fim: int = 20) -> None:
    """
    Imprime números pares no intervalo especificado.
    """
    # Percorre o intervalo de 2 a 20
    for numero in range(inicio, fim + 1):
        # Verifica se o número é par
        if numero % 2 == 0:
            print(numero)


if __name__ == "__main__":
    # Executa a função para imprimir pares de 2 a 20
    imprimir_pares()
