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

print('Cadastro de Clientes')
print('-------------------')

# Entrada de dados
NomeCompleto = input('Nome Completo: ')
DataNascimento = input('Data de Nascimento: ')
CidadePaisOrigem = input('Cidade/Pais de Origem (Nascimento): ')
EnderecoCompleto = input('Endereco completo de onde mora: ')
PaisResidencia = input('Pais onde reside: ')
DataCadastro = input('Data do Cadastro: ')
Escolaridade = input('Escolaridade (Ensino Básico/Ensino Fundamental/Ensino Superior): ')

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