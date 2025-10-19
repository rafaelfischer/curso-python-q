# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Múltiplos de 5: Imprima todos os múltiplos de 5 que estão entre 1 e 50 (inclusive).

def multiplos_de_5(inicio: int = 1, fim: int = 50) -> list[int]:
    """
    Retorna lista com todos os múltiplos de 5 no intervalo [inicio, fim].
    """
    # Lista para guardar os múltiplos encontrados
    resultado = []

    # Percorre cada número do intervalo
    for numero in range(inicio, fim + 1):
        # Verifica se é múltiplo de 5
        if numero % 5 == 0:
            resultado.append(numero)

    return resultado


if __name__ == "__main__":
    # Obtém os múltiplos de 5 entre 1 e 50
    multiplos = multiplos_de_5()

    # Exibe os valores encontrados
    print("Múltiplos de 5 entre 1 e 50:")
    print(multiplos)
