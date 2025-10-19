# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Imprima os primeiros 10 números da sequência de Fibonacci. A Sequência de Fibonacci é uma série de números onde cada número subsequente é a soma dos dois anteriores, começando geralmente com 0 e 1 (ou 1 e 1). A sequência inicia assim: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, e assim por diante. Atenção, utilize um loop FOR.

# loop for: imprime os primeiros 10 números da sequência de Fibonacci
for i in range(10):
    if i == 0:
        print(0)
    elif i == 1:
        print(1)
    else:
        # soma dos dois números anteriores
        fibonacci = fibonacci_anterior + fibonacci_anterior_anterior
        print(fibonacci)
        # atualiza os dois números anteriores
        fibonacci_anterior_anterior = fibonacci_anterior
        fibonacci_anterior = fibonacci
