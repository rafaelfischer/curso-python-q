# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte 5 números e calcule a média. Atenção, utilize um loop FOR.

# Inicializa a soma
soma = 0

# Loop para pedir 5 números
for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

# Calcula a média
media = soma / 5

# Exibe o resultado
print("A média dos números é:", media)
