# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Preço Total da Compra: Solicite ao usuário os preços de vários produtos. O programa deve parar de pedir preços quando o usuário digitar 0. Ao final, mostre o valor total da compra.

def obter_preco():
    """Solicita preço ao usuário e valida entrada."""
    while True:
        try:
            preco = float(input("Digite o preço do produto (0 para finalizar): "))
            if preco < 0:
                print("Preço não pode ser negativo.")
                continue
            return preco
        except ValueError:
            print("Entrada inválida. Digite um número.")

def calcular_total():
    """Acumula preços até usuário digitar 0."""
    total = 0.0
    while True:
        preco = obter_preco()
        if preco == 0:
            break
        total += preco
    return total

def main():
    # Exibe cabeçalho
    print("=== Soma de Preços ===")
    
    # Calcula e exibe total
    total_compra = calcular_total()
    print(f"\nTotal da compra: R$ {total_compra:.2f}")

if __name__ == "__main__":
    main()
