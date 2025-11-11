"""
Grupo 3.2
Exercício: 15  
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Validação Robusta de Entrada: Peça ao usuário para digitar um número entre 1 e 10 (inclusive). 
    Use um loop ENQUANTO para continuar pedindo a entrada até que o número seja válido (maior ou igual a 1 E menor ou igual a 10).
"""

# loop para garantir entrada válida
while True:
    # pede número ao usuário
    numero = input("Digite um número entre 1 e 10: ")

    # verifica se é dígito
    if not numero.isdigit():
        print("Entrada inválida. Precisa ser um número.")
        continue

    # converte para inteiro
    numero = int(numero)

    # verifica se está no intervalo
    if 1 <= numero <= 10:
        print(f"Você digitou: {numero}")
        break
    else:
        print("Número fora do intervalo. Tente novamente.")
