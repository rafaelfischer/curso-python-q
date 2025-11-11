"""
Grupo 3.2
Exercício: 7   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Parar em Condição Específica: Peça números inteiros ao usuário continuamente. 
    Use um loop ENQUANTO para continuar pedindo até que ele digite um número negativo. 
    Ao final, imprima quantos números positivos foram digitados.
"""

# Contador de números positivos
contador_positivos = 0

# Loop enquanto o número for não negativo
while True:
    numero = int(input("Digite um número inteiro (negativo para parar): "))
    
    # Se for negativo, sai do loop
    if numero < 0:
        break
    
    # Conta apenas positivos
    contador_positivos += 1

# Mostra quantos positivos foram digitados
print(f"Quantidade de números positivos digitados: {contador_positivos}")
