"""
bank_system_v2.py

Este módulo implementa a versão 2 do sistema bancário BankFischer,
introduzindo funcionalidades avançadas como o cheque especial.
Ele se baseia em funções comuns definidas em `bank_common.py` para
operações básicas de conta e persistência de dados, focando na
lógica específica da interface do usuário e das novas funcionalidades.

Principais funcionalidades:
- Menu principal para cadastro de clientes e login.
- Menu pós-login com opções de depósito, saque, verificação de saldo,
  geração de extrato e solicitação de limite de cheque especial.
- Funcionalidade de saque aprimorada para utilizar o cheque especial.
- Simulação de solicitação e aprovação de limite de cheque especial.

Dependências:
- `os`: Para operações relacionadas ao sistema operacional (não diretamente usado aqui, mas comum em módulos Python).
- `datetime`: Para registrar a data e hora das transações.
- `bank_common`: Módulo que contém funções e constantes compartilhadas,
  como cores ANSI, funções de impressão formatada, carregamento/salvamento
  de contas, e operações bancárias básicas.
"""

import os
from datetime import datetime
from bank_common import (
    print_success, print_error, print_warning, print_info,
    carregar_contas, salvar_contas, cadastrar_conta, fazer_login, depositar, verificar_saldo, gerar_extrato
)


def menu_principal():
    """
    Exibe o menu principal do sistema bancário BankFischer V2.
    Permite ao usuário cadastrar um novo cliente, fazer login em uma conta existente ou sair do sistema.
    A navegação é feita através de opções numéricas.
    """
    while True:
        print("\n" + "="*30)
        print_info("BEM-VINDO AO BANKFISCHER V2")
        print("="*30)
        print_warning("[1] Cadastrar cliente")
        print_info("[2] Fazer login")
        print_info("[3] Usuários")
        print_info("[4] Sair")
        print("="*30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Chama a função de cadastro de conta do módulo bank_common
            cadastrar_conta()
        elif opcao == "2":
            # Tenta fazer login e, se bem-sucedido, exibe o menu pós-login
            cpf = fazer_login()
            if cpf:
                menu_pos_login(cpf)
        elif opcao == "3":
            menu_usuarios()
        elif opcao == "4":
            print_error("Saindo... Obrigado por usar o BankFischer V2!")
            break
        else:
            print_error("Opção inválida. Tente novamente.")


def menu_pos_login(cpf):
    """
    Exibe o menu de opções para um usuário logado no sistema BankFischer V2.
    Permite realizar operações como depósito, saque, verificação de saldo,
    geração de extrato e solicitação de limite de cheque especial.

    Args:
        cpf (str): O CPF do cliente logado, usado para identificar a conta.
    """
    contas = carregar_contas()
    conta = contas.get(cpf)
    if not conta:
        # Caso a conta não seja encontrada (situação inesperada após login)
        print_error("Erro: Conta não encontrada após login.")
        return

    while True:
        print("\n" + "="*30)
        print_info(f"BEM-VINDO, {conta['nome'].upper()} (V2)")
        print("="*30)
        print_info("[1] Depositar")
        print_info("[2] Sacar")
        print_info("[3] Verificar Saldo")
        print_info("[4] Gerar Extrato")
        print_info("[5] Solicitar Limite Cheque Especial")
        print_info("[6] Sair")
        print("="*30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Chama a função de depósito do módulo bank_common
            depositar(cpf)
        elif opcao == "2":
            # Chama a função de saque específica desta versão (V2)
            sacar(cpf)
        elif opcao == "3":
            # Chama a função de verificação de saldo do módulo bank_common
            verificar_saldo(cpf)
        elif opcao == "4":
            # Chama a função de geração de extrato do módulo bank_common
            gerar_extrato(cpf)
        elif opcao == "5":
            # Chama a função de solicitação de cheque especial específica desta versão (V2)
            solicitar_limite_cheque_especial(cpf)
        elif opcao == "6":
            print_error("Saindo da conta...")
            break
        else:
            print_error("Opção inválida. Tente novamente.")


def sacar(cpf):
    """
    Realiza uma operação de saque para a conta especificada pelo CPF.
    Esta versão do saque permite a utilização do limite do cheque especial
    caso o saldo em conta seja insuficiente.

    Args:
        cpf (str): O CPF do cliente que está realizando o saque.
    """
    contas = carregar_contas()
    conta = contas.get(cpf)

    if not conta:
        print_error("Conta não encontrada.")
        return

    while True:
        try:
            valor = float(input("Informe o valor do saque: "))
            if valor <= 0:
                print_error("O valor do saque deve ser positivo.")
                continue

            # Calcula o saldo disponível, incluindo o limite do cheque especial
            saldo_disponivel = conta['saldo'] + conta['limite_cheque_especial']

            if valor > saldo_disponivel:
                # Verifica se o valor do saque excede o saldo total disponível
                print_error("Saldo insuficiente, incluindo o limite do cheque especial.")
                print_warning(f"Seu saldo disponível é de R$ {saldo_disponivel:.2f}.")
                continue

            # Alerta o usuário se o cheque especial será utilizado
            if valor > conta['saldo']:
                uso_cheque_especial = valor - conta['saldo']
                conta['cheque_especial_utilizado'] = conta.get('cheque_especial_utilizado', 0.0) + uso_cheque_especial
                if conta['saldo'] > 0:
                    print_warning(f"Seu saldo atual é de R$ {conta['saldo']:.2f}. Você utilizará R$ {uso_cheque_especial:.2f} do seu cheque especial.")
                else:
                    print_warning(f"Você utilizará R$ {uso_cheque_especial:.2f} do seu cheque especial.")
                
                # Registra a transação de uso do cheque especial
                conta['transacoes'].append({
                    "tipo": "USO_CHEQUE_ESPECIAL",
                    "valor": uso_cheque_especial,
                    "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

            # Atualiza o saldo da conta
            conta['saldo'] -= valor
            # Registra a transação de saque
            conta['transacoes'].append({
                "tipo": "SAQ",
                "valor": valor,
                "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            salvar_contas(contas)
            print_success(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            break

        except ValueError:
            print_error("Valor inválido. Por favor, digite um número.")

def solicitar_limite_cheque_especial(cpf):
    """
    Permite ao cliente solicitar um limite de cheque especial.
    Esta função simula uma análise de crédito básica:
    - Valores até R$ 500 são aprovados automaticamente.
    - Valores acima de R$ 500 são marcados para análise manual.
    Um cliente só pode fazer uma solicitação de limite por vez.

    Args:
        cpf (str): O CPF do cliente que está solicitando o limite.
    """
    contas = carregar_contas()
    conta = contas.get(cpf)

    if not conta:
        print_error("Conta não encontrada.")
        return

    # Inicializa o campo 'limite_cheque_especial_solicitado' se ele não existir
    if 'limite_cheque_especial_solicitado' not in conta:
        conta['limite_cheque_especial_solicitado'] = False
        salvar_contas(contas) # Salva para inicializar o campo no arquivo

    if conta['limite_cheque_especial_solicitado']:
        print_warning("Você já solicitou um limite de cheque especial. Aguarde a análise.")
        return

    while True:
        try:
            valor_solicitado = float(input("Informe o valor do limite de cheque especial desejado: "))
            if valor_solicitado <= 0:
                print_error("O valor solicitado deve ser positivo.")
                continue
            
            # Simulação de análise de crédito
            if valor_solicitado <= 500:
                conta['limite_cheque_especial'] = valor_solicitado
                conta['limite_cheque_especial_solicitado'] = True # Marca como solicitado
                salvar_contas(contas)
                print_success(f"Limite de cheque especial de R$ {valor_solicitado:.2f} aprovado e adicionado!")
            else:
                print_warning("Valor solicitado excede o limite máximo para aprovação automática (R$ 500.00). Sua solicitação será analisada.")
                conta['limite_cheque_especial_solicitado'] = True # Marca como solicitado
                salvar_contas(contas)
            break

        except ValueError:
            print_error("Valor inválido. Por favor, digite um número.")


def menu_usuarios():
    """
    Exibe o menu de opções relacionadas à gestão de usuários.
    Permite listar, inativar ou reativar usuários.
    """
    while True:
        print("\n" + "="*30)
        print_info("MENU DE USUÁRIOS")
        print("="*30)
        print_info("[1] Listar usuários")
        print_info("[2] Inativar usuário")
        print_info("[3] Reativar usuário")
        print_info("[4] Voltar ao menu principal")
        print("="*30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            inativar_reativar_usuario("inativar")
        elif opcao == "3":
            inativar_reativar_usuario("reativar")
        elif opcao == "4":
            break
        else:
            print_error("Opção inválida. Tente novamente.")

def listar_usuarios():
    """
    Lista todos os usuários cadastrados, mostrando CPF, Nome e Status.
    """
    contas = carregar_contas()
    if not contas:
        print_warning("Nenhum usuário cadastrado.")
        return

    print("\n" + "="*40)
    print_info("LISTAGEM DE USUÁRIOS")
    print("="*40)
    for cpf, conta in contas.items():
        status = conta.get('status', 'N/A') # Pega o status, padrão 'N/A' se não existir
        print_info(f"CPF: {cpf} | Nome: {conta['nome']} | Status: {status}")
    print("="*40)

def inativar_reativar_usuario(acao):
    """
    Inativa ou reativa um usuário com base na ação fornecida.
    Registra a transação de inativação/reativação no extrato do usuário.
    """
    contas = carregar_contas()
    cpf_alvo = input(f"Informe o CPF do usuário a ser {acao}do: ")

    conta_alvo = contas.get(cpf_alvo)
    if not conta_alvo:
        print_error("Usuário não encontrado.")
        return

    novo_status = "Inativo" if acao == "inativar" else "Ativo"
    mensagem_sucesso = "inativado" if acao == "inativar" else "reativado"
    tipo_transacao = "INATIVACAO" if acao == "inativar" else "REATIVACAO"

    if conta_alvo['status'] == novo_status:
        print_warning(f"Usuário já está {novo_status.lower()}.")
        return

    conta_alvo['status'] = novo_status
    conta_alvo['transacoes'].append({
        "tipo": tipo_transacao,
        "valor": 0.0, # Valor vazio para inativação/reativação
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    salvar_contas(contas)
    print_success(f"Usuário {conta_alvo['nome']} {mensagem_sucesso} com sucesso!")

if __name__ == "__main__":
    # Ponto de entrada principal do programa.
    # Inicia o menu principal quando o script é executado diretamente.
    menu_principal()

