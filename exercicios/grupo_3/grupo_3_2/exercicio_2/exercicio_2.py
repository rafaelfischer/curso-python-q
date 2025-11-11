"""
Grupo 3.2
Exercício: 2
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Contar Múltiplos de 3: Utilize um loop para iterar de 1 a 50 e conte quantos números são múltiplos de 3. 
    Ao final, imprima a contagem.
"""

def contar_multiplos_de_tres(limite: int = 50) -> int:
    """
    Conta quantos números entre 1 e limite (inclusive) são múltiplos de 3.
    """
    contador = 0
    for numero in range(1, limite + 1):
        if numero % 3 == 0:  # Verifica se é múltiplo de 3
            contador += 1
    return contador


if __name__ == "__main__":
    total = contar_multiplos_de_tres()
    print(f"Quantidade de múltiplos de 3 entre 1 e 50: {total}")
