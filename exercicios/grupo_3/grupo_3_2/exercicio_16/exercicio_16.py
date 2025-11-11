"""
Grupo 3.2
Exercício: 16   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Verificação de Palíndromo (Otimizado): Peça uma palavra ao usuário. 
    Use um loop para comparar os caracteres do início com os caracteres do final da palavra (ex: o primeiro com o último, o segundo com o penúltimo, etc.). 
    Informe se a palavra é um palíndromo.
"""

def eh_palindromo(palavra: str) -> bool:
    """
    Verifica se a palavra é um palíndromo.
    Compara o 1º caractere com o último, o 2º com o penúltimo, etc.
    """
    inicio = 0
    fim = len(palavra) - 1

    # Loop até o meio da palavra
    while inicio < fim:
        if palavra[inicio] != palavra[fim]:
            return False
        inicio += 1
        fim -= 1
    return True


def main():
    # Entrada do usuário
    palavra = input("Digite uma palavra: ").strip()

    # Validação simples
    if not palavra:
        print("Você não digitou nada.")
        return

    # Verificação e saída
    if eh_palindromo(palavra):
        print(f'"{palavra}" é um palíndromo.')
    else:
        print(f'"{palavra}" não é um palíndromo.')


if __name__ == "__main__":
    main()
