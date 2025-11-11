"""
Grupo 3.2
Exercício: 17   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Busca e Contagem em Lista: Suponha uma lista predefinida de palavras (ex: ["maça", "banana", "laranja", "maça", "uva"]). 
    Peça um nome de fruta ao usuário. Use um loop para verificar se a fruta está na lista e quantas vezes ela aparece.
"""

# lista de frutas pré-definida
lista_frutas = ["maça", "banana", "laranja", "maça", "uva"]

# pede ao usuário o nome da fruta
fruta_desejada = input("Digite o nome de uma fruta: ").strip().lower()

# inicializa contador
quantidade = 0

# percorre a lista contando ocorrências
for fruta in lista_frutas:
    if fruta == fruta_desejada:
        quantidade += 1

# exibe resultado
if quantidade > 0:
    print(f"A fruta '{fruta_desejada}' aparece {quantidade} vez(es) na lista.")
else:
    print(f"A fruta '{fruta_desejada}' não foi encontrada na lista.")

