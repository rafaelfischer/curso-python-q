# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte um número. Some todos os números de 1 até esse número. Atenção, utilize um loop WHILE.

def somar_numeros_ate_o_digitado():
    try:
        numero_limite = int(input("Por favor, digite um número inteiro positivo: "))
        
        if numero_limite < 1:
            print("Por favor, digite um número inteiro positivo.")
            return

        soma_total = 0
        numero_atual = 1
        # Loop WHILE para somar os números de 1 até o número digitado
        while numero_atual <= numero_limite:
            soma_total += numero_atual
            numero_atual += 1
            
        print(f"A soma de todos os números de 1 até {numero_limite} é: {soma_total}")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Chama a função para executar o programa
somar_numeros_ate_o_digitado()