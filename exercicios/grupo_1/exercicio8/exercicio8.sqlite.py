# Objetivo do programa: Você está montando um cadastro para uma empresa de vendas na internet, e precisa fornecer este 'formulário de dados de clientes'.
#                         Não se preocupe neste momento se irá ou não guardar este dado em algum lugar.
#                         Pergunte e obtenha os seguintes dados e depois exiba todos na tela:
#                                 - Nome Completo
#                                 - Data de Nascimento
#                                 - Cidade/Pais de Origem(Nascimento)
#                                 - Endereco completo de onde mora
#                                 - Pais onde reside
#                                 - Data do Cadastro
#                                 - Escolaridade: (Ensino Básico/Ensino Fundamental/Ensino Superior)
#  Data da criacao: 2025-08-28
#  Criado por: @programacaomentoria
#  Ultima atualizacao: 2025-09-16
#  Alterado por: @rafaelfischer
import sqlite3
conn = sqlite3.connect('exercicios/grupo_1/exercicio8/cadastros.db')
cursor = conn.cursor()


# Crio a tabela de clientes se nao existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome_completo TEXT,
        data_nascimento TEXT,
        cidade_pais_origem TEXT,
        endereco_completo TEXT,
        pais_residencia TEXT,
        data_cadastro TEXT,
        escolaridade TEXT,
        data_insercao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )'''
)


# Inicio do programa
print('Cadastro de Clientes')
print('-------------------')

# Entrada de dados
NomeCompleto = input('Nome Completo: ')
DataNascimento = input('Data de Nascimento: ')
CidadePaisOrigem = input('Cidade/Pais de Origem (Nascimento): ')
EnderecoCompleto = input('Endereco completo de onde mora: ')
PaisResidencia = input('Pais onde reside: ')
DataCadastro = input('Data do Cadastro - (padrão data atual): ')
Escolaridade = input('Escolaridade (Ensino Básico/Ensino Fundamental/Ensino Superior): ')

# Se DataCadastro estiver vazio, atribuo a data atual
if DataCadastro.strip() == '':
    from datetime import datetime
    DataCadastro = datetime.now().strftime('%d/%m/%Y')

# Efetuo tratamento SQL Injection simples
NomeCompleto = NomeCompleto.replace("'", "''")
DataNascimento = DataNascimento.replace("'", "''")
CidadePaisOrigem = CidadePaisOrigem.replace("'", "''")
EnderecoCompleto = EnderecoCompleto.replace("'", "''")
PaisResidencia = PaisResidencia.replace("'", "''")
DataCadastro = DataCadastro.replace("'", "''")
Escolaridade = Escolaridade.replace("'", "''")


# Insiro os dados na tabela
cursor.execute(fr'''
    INSERT INTO clientes (
        nome_completo, data_nascimento, cidade_pais_origem,
        endereco_completo, pais_residencia, data_cadastro, escolaridade
    ) 
    VALUES ('{NomeCompleto}', '{DataNascimento}', '{CidadePaisOrigem}', '{EnderecoCompleto}', '{PaisResidencia}', '{DataCadastro}', '{Escolaridade}')
''')
conn.commit()   # Salvo as alteracoes
conn.close()    # Fecho a conexao



# Saida de dados
print()
print('============================')
print('Dados do Cliente Cadastrado:')
print('============================')
print('Nome Completo:', NomeCompleto)
print('Data de Nascimento:', DataNascimento)
print('Cidade/Pais de Origem:', CidadePaisOrigem)
print('Endereco Completo:', EnderecoCompleto)
print('Pais de Residencia:', PaisResidencia)
print('Data de Cadastro:', DataCadastro)
print('Escolaridade:', Escolaridade)