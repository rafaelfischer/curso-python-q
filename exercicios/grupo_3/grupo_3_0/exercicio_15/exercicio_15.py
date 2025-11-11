# Autor: Rafael Fischer
# Data de Criação: 07/10/2025
# Descrição da Solicitação: Pergunte quantos alunos há na turma. Para cada aluno, pergunte a nota e calcule a média da turma. Atenção, utilize um loop FOR.

def calcular_media_turma():
    try:
        quantidade_alunos = int(input("Quantos alunos há na turma? "))
        
        if quantidade_alunos <= 0:
            print("A quantidade de alunos deve ser um número positivo.")
            return

        soma_das_notas = 0
        
        # Loop FOR para perguntar a nota de cada aluno
        for i in range(quantidade_alunos):
            while True:
                try:
                    nota_aluno = float(input(f"Digite a nota do aluno {i + 1}: "))
                    if 0 <= nota_aluno <= 10:
                        soma_das_notas += nota_aluno
                        break # Sai do loop interno se a nota for válida
                    else:
                        print("A nota deve estar entre 0 e 10.")
                except ValueError:
                    print("Entrada inválida. Por favor, digite um número para a nota.")
            
        # Calcula a média da turma
        media_turma = soma_das_notas / quantidade_alunos
        
        print(f"A soma total das notas é: {soma_das_notas}")
        print(f"A média da turma com {quantidade_alunos} alunos é: {media_turma:.2f}") # Exibe a média com 2 casas decimais

    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro para a quantidade de alunos.")

# Chama a função para executar o programa
calcular_media_turma()