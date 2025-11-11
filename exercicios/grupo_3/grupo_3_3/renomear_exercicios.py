# Autor: Rafael Fischer 
# Data de Criação: 07/10/2025 
# Descrição da Solicitação: 

import os
import shutil

# Diretório base
base_dir = os.path.dirname(os.path.abspath(__file__))

# Mapeamento de números antigos para novos
mapeamento = {}
numero_antigo = 44
for novo_numero in range(1, 55):
    mapeamento[f"exercicio_{numero_antigo}"] = f"exercicio_{novo_numero}"
    numero_antigo += 1

# Criar diretórios temporários para evitar conflitos de nomes
for pasta_antiga, pasta_nova in mapeamento.items():
    caminho_antigo = os.path.join(base_dir, pasta_antiga)
    caminho_temp = os.path.join(base_dir, f"temp_{pasta_nova}")
    
    if os.path.exists(caminho_antigo):
        print(f"Renomeando {pasta_antiga} para temp_{pasta_nova}")
        os.rename(caminho_antigo, caminho_temp)

# Renomear de temporário para final
for pasta_antiga, pasta_nova in mapeamento.items():
    caminho_temp = os.path.join(base_dir, f"temp_{pasta_nova}")
    caminho_novo = os.path.join(base_dir, pasta_nova)
    
    if os.path.exists(caminho_temp):
        print(f"Renomeando temp_{pasta_nova} para {pasta_nova}")
        os.rename(caminho_temp, caminho_novo)
        
        # Renomear arquivos dentro da pasta
        for arquivo in os.listdir(caminho_novo):
            if arquivo.startswith(pasta_antiga):
                novo_arquivo = arquivo.replace(pasta_antiga, pasta_nova)
                os.rename(
                    os.path.join(caminho_novo, arquivo),
                    os.path.join(caminho_novo, novo_arquivo)
                )
                print(f"  Arquivo renomeado: {arquivo} -> {novo_arquivo}")

print("Renomeação concluída com sucesso!")