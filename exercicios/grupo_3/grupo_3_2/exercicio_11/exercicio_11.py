# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Soma dos N Primeiros Números: Peça ao usuário um número N e calcule a soma de todos os números inteiros de 1 a N.

def soma_numeros_ate(n: int) -> int:
    """
    Calcula a soma dos N primeiros números inteiros positivos.
    Usa fórmula fechada para evitar loop e garantir performance.
    """
    return n * (n + 1) // 2


def obter_numero_do_usuario() -> int:
    """
    Solicita ao usuário um número inteiro positivo.
    Valida a entrada até receber um valor válido.
    """
    while True:
        try:
            valor = int(input("Digite um número inteiro positivo N: "))
            if valor <= 0:
                print("Por favor, insira um número maior que zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def main():
    """
    Função principal: orquestra a leitura, cálculo e exibição do resultado.
    """
    numero = obter_numero_do_usuario()
    resultado = soma_numeros_ate(numero)
    print(f"A soma dos {numero} primeiros números é: {resultado}")


# Executa o programa apenas se este arquivo for o principal
if __name__ == "__main__":
    main()
