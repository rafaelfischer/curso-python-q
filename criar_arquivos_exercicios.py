import os

def body_extensao(package_name, numero_exercicio, extensao: str) -> str:
    if '.java' in extensao:
        return '''/*
    Objetivo do programa: 
    Data da criacao: YYYY-MM-DD
    Criado por: @autor
*/
package '''+ package_name +''';

public class Exercicio'''+ str(numero_exercicio) +''' {
    public static void main(String[] args) {
        // Implementar a lógica aqui
    }
}'''

    elif '.py' in extensao: 
        return '''# Arquivo: exercicio_''' + str(numero_exercicio) + extensao + '''
# Objetivo do programa: 
# Data da criacao: YYYY-MM-DD
# Criado por: @autor

def main():
    pass  # Implementar a lógica aqui'''
    
    else:   
        return ''



# Cria arquivos exercicio_X.py com conteúdo básico, baseado na extensão do arquivo.
def criar_arquivos(item_diretorio) -> int:
    diretorio, total_exercicios, extensao_arquivo, package_name = item_diretorio
    # print(f"Processando diretório: {diretorio}")
    
    # Verifica se o diretório existe
    if not os.path.exists(diretorio):
        # print(f"Diretório {diretorio} não encontrado. ")
        os.makedirs(diretorio)
        
        if os.path.exists(diretorio):
            print(f"Diretório {diretorio} criado com sucesso.")
        else:
            print(f"Falha ao criar o diretório {diretorio}.")
            
   
   
    arquivos_criados = 0
    for numero_exercicio in range(1, total_exercicios+1):
        # Nome do arquivo 
        nome_arquivo = f"exercicio_{numero_exercicio}{extensao_arquivo}"
        # print(nome_arquivo)
        
        # Caminho completo para o arquivo 
        caminho_arquivo = os.path.join(diretorio, nome_arquivo)
        
        # Verifica se o arquivo existe 
        if (not os.path.exists(caminho_arquivo)):
            # Cria o arquivo vazio
            with open(caminho_arquivo, 'w') as f:
                f.write(body_extensao(package_name, numero_exercicio, extensao_arquivo).encode('utf-8').decode('iso-8859-1'))
            
            print(f"Arquivo criado: {caminho_arquivo}")
            arquivos_criados += 1
        # else:
        #     print(f"Arquivo já existe: {caminho_arquivo}")
            

        # print(f"Total de arquivos criados em {diretorio}: {arquivos_criados}")

    return arquivos_criados



if __name__ == "__main__":
    print('-----------------------\nBem vindo ao criador de arquivos de exercícios!\n-----------------------')
    while True:
        try:
            diretorio = input("Digite o diretório completo: ")
            if not diretorio:
                print("Diretório inválido. Tente novamente.")
                break

            quantidade = int(input("Digite a quantidade de exercícios a serem criados: "))
            extensao = input("Digite a extensão do arquivo (ex: .py, .java): ")
            package_name = input("Digite o nome do package (deixe vazio se não for Java): ")
            total_arquivos_criados = criar_arquivos([diretorio, quantidade, extensao, package_name])
            print(f"Total geral de arquivos criados: {total_arquivos_criados}")


            criar_outra_pasta = input("\nDeseja criar outra pasta (s/n): ")
            if criar_outra_pasta.lower() != 's':
                print('-----------------------\nObrigado por usar mais um produto das organizações Tabajara!\n-----------------------')
                break

        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            continue
