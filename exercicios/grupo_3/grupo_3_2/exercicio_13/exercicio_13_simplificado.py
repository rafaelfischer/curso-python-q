"""
Grupo 3.2
Exercício: 13
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Verificar Caracteres Específicos em Frase: Receba uma frase do usuário. 
	Use um loop para iterar sobre a frase e conte quantos caracteres são vogais (a, e, i, o, u, maiúsculas ou minúsculas) OU são dígitos numéricos (0-9).
"""

# pede a frase ao usuário
frase = input("Digite uma frase: ")

# contador de vogais ou dígitos
contador = 0

# percorre cada caractere da frase
for caractere in frase:
    # verifica se é vogal (minúscula ou maiúscula) ou dígito
    if caractere.lower() in "aeiou" or caractere.isdigit():
        contador += 1

# exibe o resultado
print("Total de vogais ou dígitos na frase:", contador)
