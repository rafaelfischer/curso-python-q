"""
bank_common.py

Este módulo contém funções e constantes comuns utilizadas por diferentes versões do sistema bancário BankFischer.
Ele centraliza a lógica de persistência de dados, gerenciamento de contas, operações bancárias básicas e utilitários de interface,
promovendo a reutilização de código e facilitando a manutenção.
"""

import json
import os
from datetime import datetime

# --- Constantes de Cores ANSI para Terminal ---
# Utilizadas para formatar a saída do console com cores, melhorando a legibilidade e a experiência do usuário.
VERMELHO = '\033[91m'  # Vermelho para mensagens de erro ou destaque negativo
VERDE = '\033[92m'    # Verde para mensagens de sucesso ou destaque positivo
AMARELO = '\033[93m'  # Amarelo para avisos ou informações importantes
AZUL = '\033[94m'     # Azul para informações gerais ou títulos
RESET = '\033[0m'     # Reseta a cor do terminal para o padrão

# --- Funções Auxiliares de Impressão Colorida ---
# Simplificam a exibição de mensagens no console com cores predefinidas.
def print_success(message):
    """Imprime uma mensagem em verde, indicando sucesso."""
    print(f"{VERDE}{message}{RESET}")

def print_error(message):
    """Imprime uma mensagem em vermelho, indicando um erro."""
    print(f"{VERMELHO}{message}{RESET}")

def print_warning(message):
    """Imprime uma mensagem em amarelo, indicando um aviso."""
    print(f"{AMARELO}{message}{RESET}")

def print_info(message):
    """Imprime uma mensagem em azul, indicando informação geral."""
    print(f"{AZUL}{message}{RESET}")

# --- Definições de Arquivos de Dados ---
# Caminhos para os arquivos JSON que armazenam os dados do sistema.
ARQUIVO_DADOS = './data/dataPorConta.json'
ARQUIVO_TIPOS_TRANSACAO = './data/transaction_types.json'

# --- Funções de Persistência de Dados ---
def carregar_contas():
    """
    Carrega os dados das contas bancárias de um arquivo JSON.
    Se o arquivo não existir ou estiver vazio, retorna um dicionário vazio.

    Retorno:
        dict: Um dicionário onde as chaves são os CPFs e os valores são os dados das contas.
    """
    if not os.path.exists(ARQUIVO_DADOS):
        return {}
    with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
        content = f.read()
        if not content:
            return {}
        return json.loads(content)

def salvar_contas(contas):
    """
    Salva os dados das contas bancárias em um arquivo JSON.
    O arquivo é formatado com indentação para facilitar a leitura.

    Parâmetros:
        contas (dict): O dicionário contendo todas as contas a serem salvas.
    """
    # Garante que o diretório 'data' exista
    os.makedirs(os.path.dirname(ARQUIVO_DADOS), exist_ok=True)
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(contas, f, indent=4, ensure_ascii=False)

def carregar_tipos_transacao():
    """
    Carrega os tipos de transação de um arquivo JSON.
    Se o arquivo não existir, retorna um dicionário vazio.

    Retorno:
        dict: Um dicionário onde as chaves são os IDs dos tipos de transação e os valores são os detalhes.
    """
    if not os.path.exists(ARQUIVO_TIPOS_TRANSACAO):
        return {}
    with open(ARQUIVO_TIPOS_TRANSACAO, 'r', encoding='utf-8') as f:
        tipos_transacao_lista = json.load(f)
        # Converte a lista de tipos de transação para um dicionário para fácil acesso pelo ID
        return {tipo['ID']: tipo for tipo in tipos_transacao_lista}

# --- Funções de Gerenciamento de Conta ---
def cadastrar_conta():
    """
    Permite o cadastro de um novo cliente no sistema bancário.
    Solicita CPF e nome, valida o CPF e verifica se já existe.
    Cria uma nova conta com saldo zero, limite de cheque especial zero e sem transações.
    """
    print_info("\n--- CADASTRO DE CLIENTE ---")
    while True:
        cpf = input("Informe o CPF (apenas números, 11 dígitos) ou deixe em branco para sair: ")
        if not cpf:
            print_warning("Cadastro de cliente cancelado.")
            return # Sai da função se o CPF for vazio

        if not cpf.isdigit() or len(cpf) != 11:
            print_error("CPF inválido. O CPF deve conter 11 dígitos numéricos.")
            continue
        contas = carregar_contas()
        # Verifica se o CPF já está cadastrado
        if cpf in contas:
            print_error("CPF já cadastrado. Por favor, tente novamente com outro CPF ou faça login.")
        else:
            break # CPF válido e não cadastrado, sai do loop

    nome = input("Informe o nome completo: ")
    contas = carregar_contas() # Recarrega as contas para garantir dados atualizados
    contas[cpf] = {
        "nome": nome,
        "saldo": 0.0,
        "limite_cheque_especial": 0.0,
        "cheque_especial_utilizado": 0.0, # Novo campo para rastrear o uso do cheque especial
        "status": "Ativo", # Novo campo para o status do usuário
        "transacoes": [] # Lista para armazenar o histórico de transações
    }
    salvar_contas(contas)
    print_success(f"Conta para {nome} cadastrada com sucesso!")

def fazer_login():
    """
    Realiza o login de um cliente no sistema.
    Solicita o CPF e verifica se ele corresponde a uma conta existente e ativa.

    Retorno:
        str or None: O CPF do cliente logado se o login for bem-sucedido, caso contrário, None.
    """
    print_info("\n--- LOGIN DO CLIENTE ---\n")
    cpf = input("Informe o CPF para login: ")
    contas = carregar_contas()
    if cpf in contas:
        if contas[cpf]['status'] == "Inativo":
            print_error("Login negado. Sua conta está inativa.")
            return None
        print_success("Login realizado com sucesso!")
        return cpf
    else:
        print_error("CPF não encontrado. Por favor, cadastre-se ou tente novamente.")
        return None

# --- Funções de Operações Bancárias ---
def depositar(cpf):
    """
    Realiza um depósito na conta do cliente especificado.
    Solicita o valor do depósito, valida-o e atualiza o saldo e o histórico de transações.

    Parâmetros:
        cpf (str): O CPF do cliente que realizará o depósito.
    """
    contas = carregar_contas()
    conta = contas[cpf] # Obtém a conta do cliente logado

    while True:
        try:
            valor = float(input("Informe o valor a ser depositado: "))
            if valor <= 0:
                print_error("O valor do depósito deve ser positivo.")
            else:
                break # Valor válido, sai do loop
        except ValueError:
            print_error("Valor inválido. Por favor, digite um número.")

    conta['saldo'] += valor # Adiciona o valor ao saldo
    data_hora = datetime.now().strftime("%d-%m-%Y %H:%M")
    # Registra a transação no histórico
    conta['transacoes'].append({"data_hora": data_hora, "tipo": "DEP", "valor": valor})
    salvar_contas(contas) # Salva as alterações no arquivo
    print_success(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

def verificar_saldo(cpf):
    """
    Exibe o saldo atual, o limite de cheque especial e o saldo total disponível
    (saldo + limite de cheque especial) da conta do cliente.

    Parâmetros:
        cpf (str): O CPF do cliente para verificar o saldo.
    """
    contas = carregar_contas()
    conta = contas[cpf]

    print_success(f"\nSeu saldo atual é: R$ {conta['saldo']:.2f}")
    print_success(f"Seu limite de cheque especial é: R$ {conta['limite_cheque_especial']:.2f}")
    print_success(f"Cheque especial utilizado: R$ {conta.get('cheque_especial_utilizado', 0.0):.2f}")
    print_success(f"Seu saldo total disponível (incluindo cheque especial) é: R$ {(conta['saldo'] + conta['limite_cheque_especial']):.2f}")
    input("\nPressione Enter para voltar ao menu pós-login.")

def gerar_extrato(cpf):
    """
    Gera e exibe o extrato bancário detalhado de todas as transações da conta.
    Inclui data, tipo de operação e valor.
    No final, exibe o saldo atual da conta.

    Parâmetros:
        cpf (str): O CPF do cliente para gerar o extrato.
    """
    contas = carregar_contas()
    conta = contas[cpf]
    print("\n--- EXTRATO BANCÁRIO ---")
    tipos_transacao = carregar_tipos_transacao() # Carrega os nomes dos tipos de transação

    if not conta['transacoes']:
        print_error("Não há movimentações para esta conta.")
    else:
        # Itera sobre as transações e as exibe formatadas
        for transacao in conta['transacoes']:
            data_hora = transacao['data_hora']
            tipo_operacao_id = transacao['tipo']
            # Obtém o nome amigável do tipo de transação, ou usa o ID se não encontrado
            tipo_operacao_nome = tipos_transacao.get(tipo_operacao_id, {}).get('Nome', tipo_operacao_id)
            valor = transacao['valor']
            if valor is None:
                valor = 0

            # Formata a exibição do valor com '+' para depósitos e '-' para saques
            if valor > 0:
                print(f"{data_hora} {tipo_operacao_nome:<10} {valor:>10.2f}+")
            else:
                print(f"{data_hora} {tipo_operacao_nome:<10} {abs(valor):>10.2f}-")


    saldo = conta['saldo']
    if saldo > 0:
        saldo = f"{saldo:>30.2f}+"
    else:
        saldo = f"{saldo:>30.2f}-"
    print("=============================================")
    # Exibe o saldo final da conta
    print(f"SALDO\t{saldo}")
    input("\nPressione Enter para voltar ao menu pós-login.")

