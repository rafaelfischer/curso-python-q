# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte um número. Conte quantos dígitos ele tem. Atenção, utilize um loop WHILE.

# pede número ao usuário
numero = int(input("Digite um número: "))

# garante número positivo para contar
if numero < 0:
    numero = -numero

# contador de dígitos
contador = 0

# loop while: remove último dígito até zerar
while numero > 0:
    numero = numero // 10  # tira o último dígito
    contador += 1          # conta mais um

# caso tenha digitado 0
if contador == 0:
    contador = 1

# mostra resultado
print("O número tem", contador, "dígitos.")
