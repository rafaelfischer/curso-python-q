import unittest
from unittest.mock import patch
import os
import json
import re
import bank_system
import bank_system_v2
from bank_common import (
    carregar_contas, salvar_contas, cadastrar_conta, fazer_login, depositar, verificar_saldo, gerar_extrato,
    ARQUIVO_DADOS, ARQUIVO_TIPOS_TRANSACAO
)

class TestBankSystem(unittest.TestCase):

    def setUp(self):
        # Configura um ambiente de teste limpo antes de cada teste
        self.test_data_dir = './data_test'
        os.makedirs(self.test_data_dir, exist_ok=True)
        self.test_arquivo_dados = os.path.join(self.test_data_dir, 'dataPorConta.json')
        self.test_arquivo_tipos_transacao = os.path.join(self.test_data_dir, 'transaction_types.json')

        # Redireciona as variáveis globais para os arquivos de teste
        global ARQUIVO_DADOS, ARQUIVO_TIPOS_TRANSACAO
        ARQUIVO_DADOS = self.test_arquivo_dados
        ARQUIVO_TIPOS_TRANSACAO = self.test_arquivo_tipos_transacao

        # Cria um arquivo de tipos de transação de teste
        tipos_transacao_data = [
            {"ID": "DEP", "Nome": "Depósito"},
            {"ID": "SAQ", "Nome": "Saque"}
        ]
        with open(self.test_arquivo_tipos_transacao, 'w', encoding='utf-8') as f:
            json.dump(tipos_transacao_data, f, indent=4, ensure_ascii=False)

        # Garante que o arquivo de contas esteja vazio no início de cada teste
        salvar_contas({})

    def tearDown(self):
        # Limpa o ambiente de teste após cada teste
        if os.path.exists(self.test_arquivo_dados):
            os.remove(self.test_arquivo_dados)
        if os.path.exists(self.test_arquivo_tipos_transacao):
            os.remove(self.test_arquivo_tipos_transacao)
        if os.path.exists(self.test_data_dir):
            os.rmdir(self.test_data_dir)

    @patch('builtins.input', side_effect=['11122233344', 'Teste Cliente'])
    def test_cadastrar_conta(self, mock_input):
        cadastrar_conta()
        contas = carregar_contas()
        self.assertIn('11122233344', contas)
        self.assertEqual(contas['11122233344']['nome'], 'Teste Cliente')
        self.assertEqual(contas['11122233344']['saldo'], 0.0)

    @patch('builtins.input', side_effect=['11122233344'])
    def test_fazer_login_success(self, mock_input):
        # Primeiro cadastra uma conta para poder fazer login
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        
        cpf_logado = fazer_login()
        self.assertEqual(cpf_logado, '11122233344')

    @patch('builtins.input', side_effect=['99999999999'])
    def test_fazer_login_failure(self, mock_input):
        cpf_logado = fazer_login()
        self.assertIsNone(cpf_logado)

    @patch('builtins.input', side_effect=['100'])
    def test_depositar(self, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        
        depositar('11122233344')
        contas = carregar_contas()
        self.assertEqual(contas['11122233344']['saldo'], 100.0)
        self.assertEqual(len(contas['11122233344']['transacoes']), 1)
        self.assertEqual(contas['11122233344']['transacoes'][0]['tipo'], 'DEP')
        self.assertEqual(contas['11122233344']['transacoes'][0]['valor'], 100.0)

    @patch('builtins.input', side_effect=['', '11122233344'])
    @patch('builtins.print')
    def test_verificar_saldo(self, mock_print, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        with patch('builtins.input', side_effect=['100']):
            depositar('11122233344')

        verificar_saldo('11122233344')
        mock_print.assert_any_call("\x1b[92m\nSeu saldo atual é: R$ 100.00\x1b[0m")
        mock_print.assert_any_call("\x1b[92mSeu limite de cheque especial é: R$ 0.00\x1b[0m")
        mock_print.assert_any_call("\x1b[92mSeu saldo total disponível (incluindo cheque especial) é: R$ 100.00\x1b[0m")

    @patch('builtins.input', side_effect=['', '11122233344'])
    @patch('builtins.print')
    def test_gerar_extrato(self, mock_print, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        with patch('builtins.input', side_effect=['100']):
            depositar('11122233344')
        
        gerar_extrato('11122233344')
        mock_print.assert_any_call("\n--- EXTRATO BANCÁRIO ---")
        mock_print.assert_any_call("=============================================")
        # Check if any call matches the SALDO line with a regex
        saldo_line_found = False
        for call_args in mock_print.call_args_list:
            if call_args.args and isinstance(call_args.args[0], str):
                if re.match(r"SALDO\s+100\.00", call_args.args[0]):
                    saldo_line_found = True
                    break
        self.assertTrue(saldo_line_found, "SALDO line not found or not correctly formatted")

    @patch('builtins.input', side_effect=['50'])
    def test_sacar_bank_system(self, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        with patch('builtins.input', side_effect=['100']):
            depositar('11122233344')
        
        bank_system.sacar('11122233344')
        contas = carregar_contas()
        self.assertEqual(contas['11122233344']['saldo'], 50.0)
        self.assertEqual(len(contas['11122233344']['transacoes']), 2)
        self.assertEqual(contas['11122233344']['transacoes'][1]['tipo'], 'SAQ')
        self.assertEqual(contas['11122233344']['transacoes'][1]['valor'], -50.0)

    @patch('builtins.input', side_effect=['150'])
    @patch('builtins.print')
    def test_sacar_bank_system_v2_with_cheque_especial(self, mock_print, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        with patch('builtins.input', side_effect=['100']):
            depositar('11122233344')
        
        # Adiciona um limite de cheque especial para o teste
        contas = carregar_contas()
        contas['11122233344']['limite_cheque_especial'] = 100.0
        salvar_contas(contas)

        bank_system_v2.sacar('11122233344')
        contas = carregar_contas()
        self.assertEqual(contas['11122233344']['saldo'], -50.0) # 100 (saldo) - 150 (saque) = -50
        self.assertEqual(len(contas['11122233344']['transacoes']), 3)
        self.assertEqual(contas['11122233344']['transacoes'][1]['tipo'], 'USO_CHEQUE_ESPECIAL')
        self.assertEqual(contas['11122233344']['transacoes'][1]['valor'], 50.0)
        self.assertEqual(contas['11122233344']['transacoes'][2]['tipo'], 'SAQ')
        self.assertEqual(contas['11122233344']['transacoes'][2]['valor'], 150.0)

    @patch('builtins.input', side_effect=['300'])
    def test_solicitar_limite_cheque_especial_bank_system_v2_auto_approve(self, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        
        bank_system_v2.solicitar_limite_cheque_especial('11122233344')
        contas = carregar_contas()
        self.assertEqual(contas['11122233344']['limite_cheque_especial'], 300.0)
        self.assertTrue(contas['11122233344']['limite_cheque_especial_solicitado'])

    @patch('builtins.input', side_effect=['600'])
    @patch('builtins.print')
    def test_solicitar_limite_cheque_especial_bank_system_v2_manual_analysis(self, mock_print, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        
        bank_system_v2.solicitar_limite_cheque_especial('11122233344')
        contas = carregar_contas()
        self.assertEqual(contas['11122233344']['limite_cheque_especial'], 0.0) # Não aprovado automaticamente
        self.assertTrue(contas['11122233344']['limite_cheque_especial_solicitado'])
        manual_analysis_message_found = False
        for call_args in mock_print.call_args_list:
            if call_args.args and isinstance(call_args.args[0], str):
                if re.search(r"Sua solicitação será analisada", call_args.args[0]):
                    manual_analysis_message_found = True
                    break
        self.assertTrue(manual_analysis_message_found, "Mensagem de análise manual não encontrada ou formatada incorretamente")

    @patch('builtins.input', side_effect=['200'])
    @patch('builtins.print')
    def test_solicitar_limite_cheque_especial_bank_system_v2_already_solicited(self, mock_print, mock_input):
        with patch('builtins.input', side_effect=['11122233344', 'Teste Cliente']):
            cadastrar_conta()
        
        # Simula uma solicitação já feita
        contas = carregar_contas()
        contas['11122233344']['limite_cheque_especial_solicitado'] = True
        salvar_contas(contas)

        bank_system_v2.solicitar_limite_cheque_especial('11122233344')
        contas = carregar_contas()
        self.assertTrue(contas['11122233344']['limite_cheque_especial_solicitado'])
        already_solicited_message_found = False
        for call_args in mock_print.call_args_list:
            if call_args.args and isinstance(call_args.args[0], str):
                if re.search(r"Você já solicitou um limite de cheque especial", call_args.args[0]):
                    already_solicited_message_found = True
                    break
        self.assertTrue(already_solicited_message_found, "Mensagem de solicitação já feita não encontrada ou formatada incorretamente")

if __name__ == '__main__':
    unittest.main()