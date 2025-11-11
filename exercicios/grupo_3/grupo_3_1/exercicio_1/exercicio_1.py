"""
Grupo 3.1
Exercício: 1
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
	Contador Crescente: Crie um algoritmo que imprima na tela todos os números inteiros de 1 a 100.
"""

def contar_crescente(limite: int = 100) -> None:
    """
    Imprime números inteiros de 1 até o limite especificado.
    """
    for numero in range(1, limite + 1):
        print(numero)


# Execução principal
if __name__ == "__main__":
    contar_crescente()  # Imprime de 1 a 100
