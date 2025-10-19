# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Sequência de Fibonacci: Gere e imprima os primeiros N termos da sequência de Fibonacci, onde N é fornecido pelo usuário. (Ex: 0, 1, 1, 2, 3, 5, 8...)

# pede quantidade de termos
quantidade = int(input("Quantos termos da sequência de Fibonacci você quer ver? "))

# primeiros dois valores
anterior = 0
atual = 1

# mostra os N termos
for i in range(quantidade):
    print(anterior, end=" ")
    # próximo valor é a soma dos dois anteriores
    proximo = anterior + atual
    # atualiza para o próximo ciclo
    anterior = atual
    atual = proximo
