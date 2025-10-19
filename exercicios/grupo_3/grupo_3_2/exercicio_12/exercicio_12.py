# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Média de Notas: Solicite ao usuário a quantidade de notas que ele deseja inserir. Em seguida, peça cada uma das notas e calcule a média aritmética delas.

def obter_quantidade_notas():
    """Pergunta ao usuário quantas notas serão inseridas."""
    while True:
        try:
            qtd = int(input("Quantas notas deseja inserir? "))
            if qtd <= 0:
                print("Digite um número positivo.")
                continue
            return qtd
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

def obter_nota(indice):
    """Solicita uma nota válida entre 0 e 10."""
    while True:
        try:
            nota = float(input(f"Digite a nota {indice + 1}: "))
            if 0 <= nota <= 10:
                return nota
            print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def calcular_media(notas):
    """Calcula a média aritmética de uma lista de notas."""
    return sum(notas) / len(notas)

def main():
    # Passo 1: Quantidade de notas
    quantidade = obter_quantidade_notas()

    # Passo 2: Coleta das notas
    lista_notas = [obter_nota(i) for i in range(quantidade)]

    # Passo 3: Cálculo da média
    media = calcular_media(lista_notas)

    # Passo 4: Exibição do resultado
    print(f"\nMédia das {quantidade} notas: {media:.2f}")

if __name__ == "__main__":
    main()
