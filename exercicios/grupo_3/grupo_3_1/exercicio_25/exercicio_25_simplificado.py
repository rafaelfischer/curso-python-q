# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Investimento Simples (Juros Compostos): Um usuário investe um valor inicial, com uma taxa de juros anual. Peça o valor inicial, a taxa de juros (em porcentagem) e o número de anos. Calcule e exiba o montante final para cada ano.

# Entrada de dados
valor_inicial = float(input("Valor inicial (R$): "))
taxa_juros = float(input("Taxa de juros anual (%): "))
anos = int(input("Número de anos: "))

# Conversão da taxa para formato decimal
taxa_decimal = taxa_juros / 100

# Cálculo e exibição do montante ano a ano
montante = valor_inicial
for ano in range(1, anos + 1):
    montante = montante * (1 + taxa_decimal)
    print(f"Ano {ano}: R$ {montante:.2f}")
