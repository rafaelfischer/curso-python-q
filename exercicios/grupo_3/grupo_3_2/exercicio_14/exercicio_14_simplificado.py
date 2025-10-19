# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Maior e Menor Número: Peça ao usuário para digitar uma sequência de números. O programa deve parar quando o usuário digitar 0. Ao final, exiba qual foi o maior e qual foi o menor número digitado (excluindo o 0).

# Inicializa as variáveis para guardar o maior e o menor número digitado
maior = None
menor = None

# Loop para pedir números até o usuário digitar 0
while True:
    num = int(input("Digite um número (0 para parar): "))
    
    # Se for 0, encerra o programa
    if num == 0:
        break
    
    # Define o primeiro número como maior e menor se ainda não houver nenhum
    if maior is None:
        maior = num
        menor = num
    else:
        # Atualiza o maior e o menor se necessário
        if num > maior:
            maior = num
        if num < menor:
            menor = num

# Exibe o resultado final
print("Maior número digitado:", maior)
print("Menor número digitado:", menor)
