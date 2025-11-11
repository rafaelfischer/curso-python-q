"""
Grupo 3.2
Exercício: 15   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Validação Robusta de Entrada: Peça ao usuário para digitar um número entre 1 e 10 (inclusive). 
    Use um loop ENQUANTO para continuar pedindo a entrada até que o número seja válido (maior ou igual a 1 E menor ou igual a 10).
"""

def obter_numero_valido():
    """
    Solicita ao usuário um número entre 1 e 10 até que a entrada seja válida.
    Retorna o número válido.
    """
    while True:
        entrada = input("Digite um número entre 1 e 10: ")
        try:
            numero = int(entrada)
            if 1 <= numero <= 10:
                return numero
            else:
                print("Fora do intervalo! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite apenas números inteiros.")

# Executa a função e exibe o resultado
numero_valido = obter_numero_valido()
print(f"Você digitou: {numero_valido}")
