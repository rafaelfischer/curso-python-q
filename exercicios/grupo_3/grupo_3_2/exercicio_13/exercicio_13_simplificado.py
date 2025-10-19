# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Contagem de Caracteres: Receba uma frase do usuário e conte quantas vezes a letra 'a' (maiúscula ou minúscula) aparece na frase.

# pede a frase ao usuário
frase = input("Digite uma frase: ")

# converte tudo para minúsculo para facilitar a contagem
frase_minuscula = frase.lower()

# conta quantas vezes a letra 'a' aparece
quantidade_a = frase_minuscula.count('a')

# mostra o resultado
print("A letra 'a' aparece", quantidade_a, "vezes na frase.")
