# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte um número. Conte quantos dígitos ele tem. Atenção, utilize um loop WHILE.

def contar_digitos_de_numero():
    try:
        numero_str = input("Por favor, digite um número inteiro: ")
        # Converte a string para um número inteiro para garantir que é um número
        # e depois converte de volta para string para contar os dígitos, ignorando o sinal se houver.
        numero_abs_str = str(abs(int(numero_str)))
        
        contador_digitos = 0
        indice = 0
        # Loop WHILE para contar os dígitos
        while indice < len(numero_abs_str):
            contador_digitos += 1
            indice += 1
            
        print(f"O número {numero_str} tem {contador_digitos} dígitos.")

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")

# Chama a função para executar o programa
contar_digitos_de_numero()