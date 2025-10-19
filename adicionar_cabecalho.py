import os
import re

def adicionar_cabecalho(diretorio_base):
    """
    Adiciona o cabeçalho especificado em todos os arquivos .py do diretório e subdiretórios
    que ainda não possuem esse cabeçalho.
    """
    cabecalho = """# Autor: Rafael Fischer 
# Data de Criação: 07/10/2025 
# Descrição da Solicitação: 

"""
    
    print(f"Processando diretório: {diretorio_base}")
    
    # Verifica se o diretório existe
    if not os.path.exists(diretorio_base):
        print(f"Diretório {diretorio_base} não encontrado.")
        return
    
    # Contador de arquivos modificados
    arquivos_modificados = 0
    
    # Percorre todos os diretórios e subdiretórios
    for raiz, diretorios, arquivos in os.walk(diretorio_base):
        for arquivo in arquivos:
            # Verifica se é um arquivo Python
            if arquivo.endswith('.py'):
                caminho_completo = os.path.join(raiz, arquivo)
                
                # Lê o conteúdo do arquivo
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                
                # Verifica se o arquivo já tem o cabeçalho (procura pelo nome do autor)
                if "Autor: Rafael Fischer" not in conteudo:
                    # Adiciona o cabeçalho no início do arquivo
                    novo_conteudo = cabecalho + conteudo
                    
                    # Escreve o novo conteúdo no arquivo
                    with open(caminho_completo, 'w', encoding='utf-8') as f:
                        f.write(novo_conteudo)
                    
                    print(f"Cabeçalho adicionado: {caminho_completo}")
                    arquivos_modificados += 1
    
    print(f"Total de arquivos modificados: {arquivos_modificados}")
    return arquivos_modificados

if __name__ == "__main__":
    # Diretório a ser processado
    diretorio = r"c:\GitHub\rafaelfischer\programacaomentoria\curso-python-q\exercicios\grupo_3\grupo_3_3"
    
    # Adiciona o cabeçalho nos arquivos
    adicionar_cabecalho(diretorio)