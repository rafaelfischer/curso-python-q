# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Imprima os primeiros 10 números da sequência de Fibonacci. A Sequência de Fibonacci é uma série de números onde cada número subsequente é a soma dos dois anteriores, começando geralmente com 0 e 1 (ou 1 e 1). A sequência inicia assim: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, e assim por diante. Atenção, utilize um loop FOR.

def imprimir_fibonacci():
    print("Os primeiros 10 números da sequência de Fibonacci são:")
    # Inicializa os dois primeiros números da sequência
    primeiro_numero = 0
    segundo_numero = 1
    
    # Lista para armazenar os números de Fibonacci
    sequencia_fibonacci = []
    
    # Adiciona o primeiro número (0) se a sequência começar com 0
    sequencia_fibonacci.append(str(primeiro_numero))
    
    # Adiciona o segundo número (1)
    sequencia_fibonacci.append(str(segundo_numero))
    
    # Loop FOR para gerar os próximos 8 números (totalizando 10)
    for _ in range(8): # Usamos _ pois não precisamos do índice
        proximo_numero = primeiro_numero + segundo_numero
        sequencia_fibonacci.append(str(proximo_numero))
        # Atualiza os números para a próxima iteração
        primeiro_numero = segundo_numero
        segundo_numero = proximo_numero
        
    # Exibe a sequência de Fibonacci separada por vírgula e espaço
    print(", ".join(sequencia_fibonacci))

# Chama a função para executar o programa
imprimir_fibonacci()