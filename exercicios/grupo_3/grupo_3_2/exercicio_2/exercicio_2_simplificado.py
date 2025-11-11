"""
Grupo 3.2
Exercício: 2
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Contador Decrescente: 
        Contar Múltiplos de 3: Utilize um loop para iterar de 1 a 50 e conte quantos números são múltiplos de 3. 
        Ao final, imprima a contagem.
"""

# Conta múltiplos de 3 entre 1 e 50
contador = 0

# Percorre de 1 a 50
for numero in range(1, 51):
    # Verifica se é múltiplo de 3
    if numero % 3 == 0:
        contador += 1

# Exibe o total
print(f"Total de múltiplos de 3: {contador}")
