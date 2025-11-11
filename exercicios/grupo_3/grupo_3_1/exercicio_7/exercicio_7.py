"""
Grupo 3.2
Exercício: 7   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Parar em Condição Específica: Peça números inteiros ao usuário continuamente. 
    Use um loop ENQUANTO para continuar pedindo até que ele digite um número negativo. 
    Ao final, imprima quantos números positivos foram digitados.
"""

def contar_positivos():
    """
    Pede números inteiros ao usuário até que ele digite um negativo.
    Retorna a quantidade de números positivos digitados.
    """
    qtd_positivos = 0  # Contador de números positivos

    while True:
        try:
            num = int(input("Digite um número inteiro (negativo para parar): "))
            if num < 0:
                break  # Sai do loop ao receber negativo
            if num > 0:
                qtd_positivos += 1  # Só conta positivos
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

    return qtd_positivos


if __name__ == "__main__":
    total = contar_positivos()
    print(f"Quantidade de números positivos digitados: {total}")
