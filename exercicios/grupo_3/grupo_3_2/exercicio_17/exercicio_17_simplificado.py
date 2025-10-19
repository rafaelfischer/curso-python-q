# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Verificador de Número Primo: Solicite um número inteiro ao usuário e verifique se ele é um número primo (ou seja, divisível apenas por 1 e por ele mesmo).

# pede número ao usuário
numero = int(input("Digite um número inteiro: "))

# primo só pode ser >= 2
if numero < 2:
    print("Não é primo")
else:
    # testa divisores de 2 até raiz quadrada
    divisor = 2
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            print("Não é primo")
            break
        divisor += 1
    else:
        print("É primo")
