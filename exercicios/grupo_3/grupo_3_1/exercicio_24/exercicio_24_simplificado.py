# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Localizador de Divisores: Peça um número inteiro ao usuário e liste todos os seus divisores.

# Pede número ao usuário
numero = int(input("Digite um número inteiro: "))

# Lista para guardar divisores
divisores = []

# Testa cada candidato de 1 até o próprio número
for candidato in range(1, numero + 1):
    # Se divide sem resto, é divisor
    if numero % candidato == 0:
        divisores.append(candidato)

# Mostra todos os divisores encontrados
print("Divisores de", numero, ":", divisores)
