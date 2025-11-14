"""
bank_system.py

Este módulo implementa a versão principal do sistema bancário BankFischer.
Ele gerencia a interação do usuário através de menus, permitindo o cadastro de clientes,
login, e acesso a operações bancárias como depósito, saque, verificação de saldo,
extrato e solicitação de limite de cheque especial.

As funcionalidades comuns e de persistência de dados são importadas de bank_common.py
para manter o código modular e facilitar a manutenção.
"""

from datetime import datetime

from bank_common import (
    print_success, print_error, print_warning, print_info,
    carregar_contas, salvar_contas,
    cadastrar_conta, fazer_login, depositar, verificar_saldo, gerar_extrato
)

def menu_principal():
    """
    Exibe o menu principal do sistema bancário, permitindo ao usuário cadastrar um novo cliente,
    fazer login em uma conta existente ou sair do sistema.
    """
    while True:
        print("\n" + "="*30)
        print_info("BEM-VINDO AO BANKFISCHER")
        print("="*30)
        print_warning("[1] Cadastrar cliente")
        print_info("[2] Fazer login")
        print_info("[3] Usuários") # Nova opção para gerenciar usuários
        print_info("[4] Sair")
        print("="*30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_conta()
        elif opcao == "2":
            cpf = fazer_login()
            if cpf:
                menu_pos_login(cpf)
        elif opcao == "3": # Nova opção para o menu de usuários
            menu_usuarios()
        elif opcao == "4":
            print_error("Saindo... Obrigado por usar o BankFischer!")
            break
        else:
            print_error("Opção inválida. Tente novamente.")


def menu_usuarios():
    """
    Exibe o menu de gerenciamento de usuários, permitindo listar, inativar ou reativar usuários.
    """
    while True:
        print("\n" + "="*30)
        print_info("GERENCIAMENTO DE USUÁRIOS")
        print("="*30)
        print_info("[1] Listar usuários")
        print_info("[2] Inativar usuário")
        print_info("[3] Reativar usuário")
        print_info("[4] Voltar ao Menu Principal")
        print("="*30)

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            listar_usuarios()
        elif opcao == "2":
            inativar_usuario_menu()
        elif opcao == "3":
            reativar_usuario_menu()
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

    print_info("\n--- LISTAGEM DE USUÁRIOS ---")
    for cpf, dados_conta in contas.items():
        print(f"CPF: {cpf}, Nome: {dados_conta['nome']}, Status: {dados_conta.get('status', 'Ativo')}")
    input("\nPressione Enter para voltar ao menu de usuários.")

def inativar_usuario_menu():
    """
    Permite inativar um usuário pelo CPF.
    """
    print_info("\n--- INATIVAR USUÁRIO ---")
    cpf = input("Informe o CPF do usuário a ser inativado: ")
    inativar_reativar_usuario(cpf, "Inativo", "INATIVACAO")

def reativar_usuario_menu():
    """
    Permite reativar um usuário pelo CPF.
    """
    print_info("\n--- REATIVAR USUÁRIO ---")
    cpf = input("Informe o CPF do usuário a ser reativado: ")
    inativar_reativar_usuario(cpf, "Ativo", "REATIVACAO")

def inativar_reativar_usuario(cpf, novo_status, tipo_transacao):
    """
    Função auxiliar para inativar ou reativar um usuário e registrar a transação.
    """
    contas = carregar_contas()
    if cpf not in contas:
        print_error("Usuário não encontrado.")
        return

    conta = contas[cpf]
    if conta.get('status', 'Ativo') == novo_status:
        print_warning(f"O usuário já está com o status {novo_status}.")
        return

    conta['status'] = novo_status
    data_hora = datetime.now().strftime("%d-%m-%Y %H:%M")
    conta['transacoes'].append({"data_hora": data_hora, "tipo": tipo_transacao, "valor": None})
    salvar_contas(contas)
    print_success(f"Usuário {cpf} {novo_status.lower()} com sucesso!")
    input("\nPressione Enter para continuar.")

def menu_pos_login(cpf):
    """
    Exibe o menu de opções bancárias para um cliente logado.
    Permite realizar depósitos, saques, verificar saldo, gerar extrato,
    solicitar limite de cheque especial ou fazer logout.

    Parâmetros:
        cpf (str): O CPF do cliente logado.
    """
    while True:
        contas = carregar_contas()
        conta = contas[cpf]
        print_info(f"\n--- BEM-VINDO, {conta['nome'].upper()} ---")
        print_info("1. Realizar depósito")
        print_info("2. Realizar saque")
        print_info("3. Verificar saldo")
        print_info("4. Emitir extrato")
        print_info("5. Solicitar Limite de Cheque Especial")
        print_info("6. Fazer logout")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            depositar(cpf)
        elif opcao == '2':
            sacar(cpf)
        elif opcao == '3':
            verificar_saldo(cpf)
        elif opcao == '4':
            gerar_extrato(cpf)
        elif opcao == '5':
            solicitar_limite_cheque_especial(cpf)
        elif opcao == '6':
            print_success("Fazendo logout...")
            break
        else:
            print_error("Opção inválida. Por favor, escolha novamente.")

def sacar(cpf):
    """
    Realiza a operação de saque para o cliente especificado.
    Verifica se o valor do saque é positivo e se há saldo suficiente (incluindo cheque especial).
    Atualiza o saldo da conta e registra a transação.

    Parâmetros:
        cpf (str): O CPF do cliente que realizará o saque.
    """
    contas = carregar_contas()
    conta = contas[cpf]
    while True:
        try:
            valor = float(input("Informe o valor a ser sacado: "))
            if valor <= 0:
                print_error("O valor do saque deve ser positivo.")
            # Verifica se o valor do saque excede o saldo disponível (saldo + limite de cheque especial)
            elif valor > (conta['saldo'] + conta['limite_cheque_especial']):
                print_error(f"Saldo insuficiente. Saldo disponível (incluindo cheque especial): R$ {(conta['saldo'] + conta['limite_cheque_especial']):.2f}")
                while True:
                    tentar_novamente = input("Deseja realizar saque de outro valor? (s/n): ").lower()
                    if tentar_novamente == 's':
                        break
                    elif tentar_novamente == 'n':
                        return # Retorna ao menu pós-login se o usuário não quiser tentar novamente
                    else:
                        print_error("Opção inválida. Digite 's' para sim ou 'n' para não.")
            else:
                break # Valor válido, sai do loop de validação
        except ValueError:
            print_error("Valor inválido. Por favor, digite um número.")

    conta['saldo'] -= valor # Deduz o valor do saque do saldo
    data_hora = datetime.now().strftime("%d-%m-%Y %H:%M")
    # Registra a transação de saque no histórico da conta
    conta['transacoes'].append({"data_hora": data_hora, "tipo": "SAQ", "valor": -valor})
    salvar_contas(contas) # Salva as alterações no arquivo
    print_success(f"Saque de R$ {valor:.2f} realizado com sucesso!")

def solicitar_limite_cheque_especial(cpf):
    """
    Permite ao cliente solicitar um novo limite de cheque especial.
    O valor é atualizado diretamente na conta do cliente.

    Parâmetros:
        cpf (str): O CPF do cliente que solicitará o limite.
    """
    contas = carregar_contas()
    conta = contas[cpf]
    print(f"\n--- SOLICITAR LIMITE DE CHEQUE ESPECIAL ---")
    print(f"Seu limite atual de cheque especial é: R$ {conta['limite_cheque_especial']:.2f}")
    while True:
        try:
            novo_limite = float(input("Informe o novo limite de cheque especial desejado: "))
            if novo_limite < 0:
                print_error("O limite de cheque especial não pode ser negativo.")
            else:
                break # Valor válido, sai do loop
        except ValueError:
            print_error("Valor inválido. Por favor, digite um número.")
    
    conta['limite_cheque_especial'] = novo_limite # Atualiza o limite de cheque especial
    salvar_contas(contas) # Salva as alterações no arquivo
    print_success(f"Seu novo limite de cheque especial foi definido para: R$ {novo_limite:.2f}")
    input("\nPressione Enter para voltar ao menu pós-login.")

if __name__ == "__main__":
    # Inicia o sistema bancário chamando o menu principal quando o script é executado diretamente.
    menu_principal()