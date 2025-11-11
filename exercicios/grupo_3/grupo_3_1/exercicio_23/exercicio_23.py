# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Cálculo de Potência (sem operador **): Receba uma base e um expoente (inteiros positivos) e calcule a potência da base elevada ao expoente sem usar o operador de potência da linguagem.


# Função que calcula a potência sem usar o operador **
def calcular_potencia(base, expoente):
    # Se o expoente for 0, o resultado sempre é 1
    if expoente == 0:
        return 1
    
    # Inicia o resultado com 1 (elemento neutro da multiplicação)
    resultado = 1
    
    # Multiplica a base pelo resultado, 'expoente' vezes
    for _ in range(expoente):
        resultado *= base
    
    return resultado


# Entrada do usuário
base = int(input("Digite a base (inteiro positivo): "))
expoente = int(input("Digite o expoente (inteiro positivo): "))

# Validação simples
if base < 0 or expoente < 0:
    print("Por favor, insira apenas números inteiros positivos.")
else:
    # Chama a função e exibe o resultado
    print(f"{base} elevado a {expoente} é {calcular_potencia(base, expoente)}")
