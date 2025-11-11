"""
Grupo 3.2
Exercício: 16   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Verificação de Palíndromo (Otimizado): Peça uma palavra ao usuário. 
    Use um loop para comparar os caracteres do início com os caracteres do final da palavra (ex: o primeiro com o último, o segundo com o penúltimo, etc.). 
    Informe se a palavra é um palíndromo.
"""

# pede palavra ao usuário
palavra = input("Digite uma palavra: ")

# remove espaços e deixa tudo minúsculo para comparar igual
palavra_limpa = palavra.replace(" ", "").lower()

# assume que é palíndromo
eh_palindromo = True

# compara primeiro com último, segundo com penúltimo...
for i in range(len(palavra_limpa) // 2):
    if palavra_limpa[i] != palavra_limpa[-1 - i]:
        eh_palindromo = False
        break  # já achou diferença, pode parar

# mostra resultado
if eh_palindromo:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")
