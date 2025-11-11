"""
Grupo 3.2
Exercício: 10   
Metodo: Simplificado
Autor: Rafael Fischer
Data de Criação: 07/10/2025
Descrição da Solicitação: 
    Aumento Salarial Condicional: Para 5 funcionários, peça o salário atual de cada um. 
    Use um loop para processá-los. 
    Se o salário for menor que R$1500, aplique um aumento de 15% e mostre o novo salário. 
    Caso contrário, mostre o salário original.
"""

# loop para 5 funcionários
for i in range(5):
    # pede salário atual
    salario = float(input(f"Salário do funcionário {i+1}: R$"))
    
    # verifica se ganha menos de 1500
    if salario < 1500:
        # aplica 15% de aumento
        novo_salario = salario * 1.15
        print(f"Novo salário: R${novo_salario:.2f}")
    else:
        # mantém salário original
        print(f"Salário sem alteração: R${salario:.2f}")
