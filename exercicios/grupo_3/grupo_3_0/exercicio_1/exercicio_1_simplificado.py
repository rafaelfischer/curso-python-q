# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Calcule o fatorial de um número.
# Pergunte o número, faça o loop e exiba o resultado no final. Exemplo: Fatorial de 5 => 5 * 4 * 3 * 2 * 1 = 120


# Pergunte ao usuário um número
numero = int(input("Digite um número para calcular o fatorial: "))

# Initialize the result
fatorial = 1

# Loop to calculate the factorial
contador = numero
while contador > 1:
    fatorial *= contador
    contador -= 1

# Display the result
print(f"O fatorial de {numero} é {fatorial}")
