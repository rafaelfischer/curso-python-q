"""
Grupo 3.2
Exercício: 12
Metodo: Tradicional
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Contagem de Valores em Faixas: Peça 10 números inteiros ao usuário. 
    Use um loop e condicionais para contar quantos números estão em cada uma das seguintes faixas: [0, 25], [26, 50], [51, 75], e [76, 100].
"""

def contar_faixas():
    # Inicializa contadores para cada faixa
    faixa_0_25 = 0
    faixa_26_50 = 0
    faixa_51_75 = 0
    faixa_76_100 = 0

    # Loop para coletar 10 números
    for i in range(10):
        while True:
            try:
                num = int(input(f"Digite o número {i + 1} (0 a 100): "))
                if 0 <= num <= 100:
                    break
                else:
                    print("Número fora da faixa permitida. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

        # Conta o número na faixa correspondente
        if 0 <= num <= 25:
            faixa_0_25 += 1
        elif 26 <= num <= 50:
            faixa_26_50 += 1
        elif 51 <= num <= 75:
            faixa_51_75 += 1
        else:  # 76 a 100
            faixa_76_100 += 1

    # Exibe os resultados
    print("\nContagem por faixas:")
    print(f"[0-25]:   {faixa_0_25} números")
    print(f"[26-50]:  {faixa_26_50} números")
    print(f"[51-75]:  {faixa_51_75} números")
    print(f"[76-100]: {faixa_76_100} números")

# Executa a função
if __name__ == "__main__":
    contar_faixas()
