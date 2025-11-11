"""
Grupo 3.2
Exercício: 12
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Contagem de Valores em Faixas: Peça 10 números inteiros ao usuário. 
    Use um loop e condicionais para contar quantos números estão em cada uma das seguintes faixas: [0, 25], [26, 50], [51, 75], e [76, 100].
"""

# Contadores para cada faixa
contador_faixa_0_25 = 0
contador_faixa_26_50 = 0
contador_faixa_51_75 = 0
contador_faixa_76_100 = 0

# Loop para pedir 10 números
for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    
    # Verifica em qual faixa o número está e incrementa o contador correspondente
    if 0 <= numero <= 25:
        contador_faixa_0_25 += 1
    elif 26 <= numero <= 50:
        contador_faixa_26_50 += 1
    elif 51 <= numero <= 75:
        contador_faixa_51_75 += 1
    elif 76 <= numero <= 100:
        contador_faixa_76_100 += 1

# Exibe os resultados
print("\nQuantidade de números em cada faixa:")
print(f"Faixa [0, 25]: {contador_faixa_0_25}")
print(f"Faixa [26, 50]: {contador_faixa_26_50}")
print(f"Faixa [51, 75]: {contador_faixa_51_75}")
print(f"Faixa [76, 100]: {contador_faixa_76_100}")
