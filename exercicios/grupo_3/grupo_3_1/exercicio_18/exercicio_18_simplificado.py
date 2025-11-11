"""
Grupo 3.2
Exercício: 18
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Cálculo de Média com Exclusões: Peça 7 números ao usuário. 
    Calcule a média aritmética desses números, mas use condicionais para excluir da soma e da contagem qualquer número que seja negativo OU que seja maior que 100.
"""

# acumuladores
soma_validos = 0
quantidade_validos = 0

# pede 7 números
for i in range(1, 8):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    # ignora negativos ou maiores que 100
    if numero < 0 or numero > 100:
        continue
    
    soma_validos += numero
    quantidade_validos += 1

# evita divisão por zero
if quantidade_validos > 0:
    media = soma_validos / quantidade_validos
    print(f"Média dos números válidos: {media}")
else:
    print("Nenhum número válido foi digitado.")
