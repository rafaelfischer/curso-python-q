# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Soma de Números até um Limite: Crie um programa que peça números ao usuário repetidamente até que a soma dos números digitados seja maior que 50. Ao final, imprima a soma total.

def solicita_numero():
    """Pede um número ao usuário e devolve como float."""
    while True:
        try:
            return float(input("Digite um número: "))
        except ValueError:
            print("Entrada inválida! Digite apenas números.")

def soma_ate_limite(limite=50):
    """Soma números até ultrapassar o limite definido."""
    soma = 0
    while soma <= limite:
        numero = solicita_numero()
        soma += numero
        print(f"Soma parcial: {soma}")
    return soma

if __name__ == "__main__":
    total = soma_ate_limite()
    print(f"Soma total ultrapassou 50: {total}")
