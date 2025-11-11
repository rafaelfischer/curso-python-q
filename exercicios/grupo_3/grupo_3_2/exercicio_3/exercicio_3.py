"""
Grupo 3.2
Exercício: 3   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Soma de Números Positivos: Peça ao usuário para digitar 5 números. 
    Use um loop para receber esses números e uma condicional para somar apenas os que são positivos.
"""

def soma_positivos(quantidade: int = 5) -> int:
    """
    Solicita ao usuário uma quantidade de números e retorna
    a soma apenas dos valores positivos.
    """
    soma = 0  # acumulador para números positivos

    for i in range(1, quantidade + 1):
        while True:
            try:
                numero = float(input(f"Digite o {i}º número: "))
                break
            except ValueError:
                print("Entrada inválida! Digite um número.")

        if numero > 0:  # considera apenas positivos
            soma += numero

    return soma


if __name__ == "__main__":
    total = soma_positivos()
    print(f"Soma dos números positivos: {total}")
