# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Cálculo de Potência (sem operador **): Receba uma base e um expoente (inteiros positivos) e calcule a potência da base elevada ao expoente sem usar o operador de potência da linguagem.

# Entrada de dados
base = int(input("Base: "))
expoente = int(input("Expoente: "))

# Validação simples
if base <= 0 or expoente <= 0:
    print("Apenas números positivos.")
else:
    resultado = 1  # Acumulador da multiplicação

    # Multiplica a base por si mesma 'expoente' vezes
    for _ in range(expoente):
        resultado *= base

    print(f"{base} elevado a {expoente} = {resultado}")
