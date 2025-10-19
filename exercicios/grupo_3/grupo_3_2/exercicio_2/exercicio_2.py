# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Contador Decrescente: Desenvolva um programa que imprima na tela todos os números inteiros de 50 a 1, em ordem decrescente.

def contador_decrescente(inicio: int = 50, fim: int = 1) -> None:
    """
    Imprime números inteiros de 'inicio' até 'fim' em ordem decrescente.
    """
    for numero in range(inicio, fim - 1, -1):
        print(numero)


# Ponto de entrada do script
if __name__ == "__main__":
    contador_decrescente()
