"""
Grupo 3.2
Exercício: 18
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Cálculo de Média com Exclusões: Peça 7 números ao usuário. 
    Calcule a média aritmética desses números, mas use condicionais para excluir da soma e da contagem qualquer número que seja negativo OU que seja maior que 100.
"""

def solicitar_numero(posicao: int) -> float:
    """Solicita um número ao usuário e retorna o valor convertido."""
    while True:
        try:
            valor = float(input(f"Digite o {posicao}º número: "))
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número válido.")


def filtrar_numero(numero: float) -> bool:
    """Retorna True se o número deve ser considerado na média."""
    # Exclui negativos ou maiores que 100
    return 0 <= numero <= 100


def calcular_media(numeros_validos: list[float]) -> float:
    """Calcula a média aritmética dos números válidos."""
    if not numeros_validos:
        return 0.0
    return sum(numeros_validos) / len(numeros_validos)


def main():
    # Lista para armazenar números válidos
    numeros_validos = []

    # Coleta 7 números
    for i in range(1, 8):
        num = solicitar_numero(i)
        if filtrar_numero(num):
            numeros_validos.append(num)
        else:
            print("  -> Número ignorado (negativo ou > 100).")

    # Calcula e exibe a média
    media = calcular_media(numeros_validos)
    print("\nResultado:")
    print(f"Quantidade de números válidos: {len(numeros_validos)}")
    print(f"Média dos números válidos: {media:.2f}")


if __name__ == "__main__":
    main()
