# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Média de Notas: Solicite ao usuário a quantidade de notas que ele deseja inserir. Em seguida, peça cada uma das notas e calcule a média aritmética delas.

# Pergunta quantas notas serão digitadas
quantidade = int(input("Quantas notas deseja inserir? "))

soma = 0  # Acumula a soma das notas

# Loop para ler cada nota
for i in range(1, quantidade + 1):
    nota = float(input(f"Digite a {i}ª nota: "))
    soma += nota  # Adiciona a nota à soma

# Calcula a média
media = soma / quantidade

# Exibe o resultado
print(f"A média das {quantidade} notas é {media:.2f}")
