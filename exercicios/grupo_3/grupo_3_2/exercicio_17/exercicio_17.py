"""
Grupo 3.2
Exercício: 17   
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Busca e Contagem em Lista: Suponha uma lista predefinida de palavras (ex: ["maça", "banana", "laranja", "maça", "uva"]). 
    Peça um nome de fruta ao usuário. 
    Use um loop para verificar se a fruta está na lista e quantas vezes ela aparece.
"""

# Lista de frutas pré-definida
lista_frutas = ["maça", "banana", "laranja", "maça", "uva"]

# Função para contar ocorrências de uma fruta na lista
def contar_fruta(fruta_buscada, lista):
    """Conta quantas vezes a fruta aparece na lista."""
    contador = 0
    for item in lista:
        if item == fruta_buscada:
            contador += 1
    return contador

# Pede ao usuário o nome da fruta
fruta_usuario = input("Digite o nome de uma fruta: ").strip().lower()

# Conta quantas vezes a fruta aparece
quantidade = contar_fruta(fruta_usuario, lista_frutas)

# Exibe o resultado
if quantidade > 0:
    print(f"A fruta '{fruta_usuario}' aparece {quantidade} vez(es) na lista.")
else:
    print(f"A fruta '{fruta_usuario}' não foi encontrada na lista.")
