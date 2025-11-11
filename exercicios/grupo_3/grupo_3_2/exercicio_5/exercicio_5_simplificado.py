"""
Grupo 3.2
Exercício: 5   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Verificar Presença de Vogal: Peça ao usuário para digitar uma palavra. 
    Use um loop para verificar cada letra da palavra e informe se a palavra contém pelo menos uma vogal.
"""
# pede palavra
palavra = input("Digite uma palavra: ")

# vogais a conferir
vogais = "aeiouAEIOU"
tem_vogal = False

# percorre cada letra
for letra in palavra:
    if letra in vogais:
        tem_vogal = True
        break

# mostra resultado
if tem_vogal:
    print("A palavra contém pelo menos uma vogal.")
else:
    print("A palavra não possui vogais.")
