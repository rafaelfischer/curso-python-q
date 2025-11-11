"""
Grupo 3.2
Exercício: 8   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Listar Números Múltiplos Duplos: De 1 a 100, use um loop para listar todos os números que são divisíveis por 4 E também por 6.
"""

def listar_multiplos_duplos(limite: int = 100) -> list[int]:
    """
    Retorna lista de números entre 1 e limite divisíveis por 4 e 6 simultaneamente.
    """
    multiplos = []  # Armazena os números que atendem à condição
    for numero in range(1, limite + 1):
        if numero % 4 == 0 and numero % 6 == 0:  # Verifica dupla divisibilidade
            multiplos.append(numero)
    return multiplos


if __name__ == "__main__":
    resultado = listar_multiplos_duplos()
    print("Números divisíveis por 4 e 6 de 1 a 100:")
    print(resultado)
