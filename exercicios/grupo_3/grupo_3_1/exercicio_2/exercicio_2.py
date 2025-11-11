"""
Grupo 3.2
Exercício: 2
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Contador Decrescente: Desenvolva um programa que imprima na tela todos os números inteiros de 50 a 1, em ordem decrescente.
"""

def contador_decrescente(inicio: int = 50, fim: int = 1) -> None:
    """
    Imprime números inteiros de 'inicio' até 'fim' em ordem decrescente.
    """
    # Valida se os valores estão corretos para decrescimento
    if inicio < fim:
        print("Erro: o valor inicial deve ser maior ou igual ao final.")
        return

    # Loop de inicio até fim, decrementando 1
    for numero in range(inicio, fim - 1, -1):
        print(numero)


if __name__ == "__main__":
    # Executa o contador padrão (50 a 1)
    contador_decrescente()
