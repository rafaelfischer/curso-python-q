import os
import sys

def criar_arquivos_simplificados(diretorio_base):
    """
    Cria arquivos exercicio_X_simplificado.py vazios nas pastas que não os possuem.
    """
    print(f"Processando diretório: {diretorio_base}")
    
    # Verifica se o diretório existe
    if not os.path.exists(diretorio_base):
        print(f"Diretório {diretorio_base} não encontrado.")
        return
    
    # Lista todas as pastas de exercícios
    pastas_exercicios = [pasta for pasta in os.listdir(diretorio_base) 
                         if os.path.isdir(os.path.join(diretorio_base, pasta)) 
                         and pasta.startswith("exercicio_")]
    
    arquivos_criados = 0
    
    # Para cada pasta de exercício
    for pasta in pastas_exercicios:
        pasta_completa = os.path.join(diretorio_base, pasta)
        
        # Obtém o número do exercício
        numero_exercicio = pasta.replace("exercicio_", "")
        
        # Nome do arquivo original e simplificado
        arquivo_original = f"exercicio_{numero_exercicio}.py"
        arquivo_simplificado = f"exercicio_{numero_exercicio}_simplificado.py"
        
        # Caminho completo para o arquivo simplificado
        caminho_simplificado = os.path.join(pasta_completa, arquivo_simplificado)
        
        # Verifica se o arquivo original existe e o simplificado não existe
        if (os.path.exists(os.path.join(pasta_completa, arquivo_original)) and 
            not os.path.exists(caminho_simplificado)):
            # Cria o arquivo simplificado vazio
            with open(caminho_simplificado, 'w') as f:
                pass  # Cria um arquivo vazio
            
            print(f"Criado: {caminho_simplificado}")
            arquivos_criados += 1
    
    print(f"Total de arquivos criados em {diretorio_base}: {arquivos_criados}")
    return arquivos_criados

if __name__ == "__main__":
    # Diretórios a serem processados
    diretorios = [
        r"c:\GitHub\rafaelfischer\programacaomentoria\curso-python-q\exercicios\grupo_3\grupo_3_2",
        r"c:\GitHub\rafaelfischer\programacaomentoria\curso-python-q\exercicios\grupo_3\grupo_3_3"
    ]
    
    total_criados = 0
    for diretorio in diretorios:
        total_criados += criar_arquivos_simplificados(diretorio)
    
    print(f"Total geral de arquivos criados: {total_criados}")